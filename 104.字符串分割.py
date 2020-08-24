i = int(input())
j = []
for x in range(i):
    j.append(input())
for x in j:
    x = list(x)
    while len(x)>8:
        print("".join(x[:8]))
        del x[:8]
    add = ["0" for i in range(8-len(x))]
    x += add
    print("".join(x))