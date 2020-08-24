name=[]
n=[]
cou = []
c=[]
number=[]
while True:
    try:
        a, b = input().split(" ")
        name.append(a)
        n.append(b)
    except:
        break
for i in range(len(name)):
    na = name[i].split("\\")[-1]
    if len(na) > 16:
        na = na[len(name) - 16:]
        cou.append([na, n[i]])
    else:
        cou.append([na, n[i]])
for i in range(len(cou)):
    number.append(cou.count(cou[i]))
for i in range(len(cou)):
    cou[i].append(number[i])
for i in range(len(cou)):
    if not cou[i] in c:
        c.append(cou[i])
if len(c) > 8:
    d = sorted(c,key = lambda x:x[2],reverse=True)[:8]
    for i in d:
        for x in range(len(i)):
            print(i[x],end = " ")
else:
    d = sorted(c, key=lambda x: x[2], reverse=True)
    for i in d:
        for x in range(len(i)):
            print(i[x],end = " ")

