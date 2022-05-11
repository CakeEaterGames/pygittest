from time import sleep
mem = [int(i) for i in open("input.txt").read().split(' ')]
pc = 0
buf = ""
while True:
    if pc < 0 or len(mem) < pc + 3:
        break
    A = mem[pc + 0]
    B = mem[pc + 1]
    C = mem[pc + 2]
    if B == -1:
        buf+=chr(mem[A])
        pc+=3
    elif A == -1:
        print(buf)
        buf=""
        sleep(1.0/60.0)
    else:
        mem[B] -= mem[A] 
    if B != -1:
        if mem[B] <= 0:
            pc=C
        else:
            pc+=3
