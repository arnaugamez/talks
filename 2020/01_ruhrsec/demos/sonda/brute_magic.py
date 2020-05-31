import r2pipe
r2 = r2pipe.open("./sonda")

r2.cmd("aei")

for i in range(0x14 + 1):
    r2.cmd("aer ecx = " + str(i))
    r2.cmd("s 0x90e")
    r2.cmd("aeip")
    r2.cmd("aesu 0x92c")
    if (r2.cmd("aer eax") == r2.cmd("aer edx")):
        print("Candidate magic number: " + str(i))

r2.quit()
