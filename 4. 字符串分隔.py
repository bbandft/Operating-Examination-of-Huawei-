i = input()
j = input()
while len(i)>8:
    if type(i) is str:
        print(i[:8])
    else:
        print("".join(i[:8]))
    i = list(i)
    del (i[:8])
for n in range(8-len(i)):
    i += "0"
print("".join(i))
while len(j)>8:
    if type(j) is str:
        print(j[:8])
    else:
        print("".join(j[:8]))
    j = list(j)
    del (j[:8])
for n in range(8-len(j)):
    j += "0"
print("".join(j))
