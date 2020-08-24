i = list(map(int,input().split(".")))
j = int(input())
a = []

for x in i:
    b = bin(x)[2:]
    if len(b) < 8:
        add = "".join(["0" for i in range(8 - len(b))])
        a.append(add+b)
    elif len(b) == 8:
        a.append(b)
print(int("".join(a),2))

c = bin(j)[2:]
e = []
if len(c) < 32:
    add = "".join(["0" for i in range(32 - len(c))])
    c = add +c
e.append(c[:8])
e.append(c[8:16])
e.append(c[16:24])
e.append(c[-8:])

for i in range(len(e)):
    if i < 3:
        print(int(e[i],2),end = ".")
    else:
        print(int(e[i],2))


