import sys
minus = 0
plus = 0
a = 0
for n in sys.stdin.readline().split():
    if int(n) <= 0:
        minus+= 1
    else:
        plus += 1
        a += int(n)
print(minus)
print(round(a/plus,1))