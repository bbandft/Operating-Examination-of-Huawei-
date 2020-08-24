i = int(input())
j = list(range(i))
b = []
if i > 1000:
    j = j[:1000]
count = 0
while len(j)>1:
    temp = j.pop(0)
    count+=1
    if count == 3:
        count = 0
        continue
    j.append(temp)
print(j[0])
