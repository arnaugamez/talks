import r2pipe
r2 = r2pipe.open("Defender.exe")
r2.cmd("aaa")
r2.cmd("s fcn.004033d1")
r2.cmd("e io.cache = 1")
r2.cmd("aeim")
r2.cmd("aeip")
r2.cmd("aesu 0x004034db")
