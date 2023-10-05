import z3

from miasm.core.locationdb import LocationDB
from miasm.analysis.binary import Container
from miasm.analysis.machine import Machine
from miasm.ir.symbexec import SymbolicExecutionEngine
from miasm.ir.translators.z3_ir import TranslatorZ3


# Check whether expr and target path constraints are compatible
def cannot_branch(expr, target):
    solver = z3.Solver()
    translator = TranslatorZ3() # convert miasm ir into z3

    c1 = translator.from_expr(expr)
    c2 = translator.from_expr(target)

    solver.add(c1 == c2)
    return solver.check() == z3.unsat


# File path
xtunnel = "./XTunnel.bin"

# Setup miasm context for XTunnel.bin file
loc_db = LocationDB()
container = Container.from_stream(open(xtunnel, 'rb'), loc_db)
machine = Machine(container.arch)
dis_engine = machine.dis_engine(container.bin_stream, loc_db=loc_db)

# Define function start address and construct asmcfg and ircfg
f_addr = 0x491AA0
asmcfg = dis_engine.dis_multiblock(f_addr)
lifter = machine.lifter_model_call(dis_engine.loc_db)
ircfg = lifter.new_ircfg_from_asmcfg(asmcfg)

# Load the file as raw bytes
xtunnel_bytes = bytearray(open(xtunnel, 'rb').read())

# Iterate over function basic blocks
for bb in asmcfg.blocks:
    # Extract address of current basic block
    bb_addr = bb.lines[0].offset

    # Initialize the symbolic execution engine
    symex_engine = SymbolicExecutionEngine(lifter)

    # Execute basic block
    expr = symex_engine.run_block_at(ircfg, bb_addr)

    # Check if the basic block branches (conditional expression)
    if expr.is_cond():
        # Check if it CANNOT branch to the TRUE branch
        if cannot_branch(expr, expr.src1):
            # Get the virtual offset of the jump
            jump_inst             = bb.lines[-1]
            jump_virtual_offset   = jump_inst.offset

            # Get the initial and end file offsets for the jump basic 
block
            jump_file_offset_init = 
container.bin_stream.bin.virt2off(jump_virtual_offset)
            jump_file_offset_end  = jump_file_offset_init + 
len(jump_inst.b)

            # Patch with NOPs
            for byte in range(jump_file_offset_init, 
jump_file_offset_end):
                xtunnel_bytes[byte] = 0x90 # NOP

open("XTunnel_patched.bin", 'wb').write(xtunnel_bytes)

