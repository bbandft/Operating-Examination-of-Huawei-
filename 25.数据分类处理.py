i = input().split()
r = input().split()
x1 = i.pop(0)
x2 = r.pop(0)
r = list(map(str,sorted(list(map(int,set(r))))))
a = []
for x in r:
    b = []
    c = 0
    d = []
    for y in i:
        d.append(y)
        if x in y:
            index = len(d)-1
            b.append(index)
            b.append(y)
            c += 1
    if c > 0:
        a.append(x)
        a.append(c)
        a += b
a.insert(0,len(a))
a = list(map(str,a))
print(" ".join(a))