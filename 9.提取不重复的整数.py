i = input()
i = i[::-1]
x=[]
for n in range(len(i)):
    y = i[n]
    if y not in x:
        x.append(i[n])
print("".join(x))
