i = input()
result= []
for x in range(len(i)-1):
    if i[x] == i[x+1]:
        count = 2
        result.append(count)
        a = x-1
        b = x+2
        while a >= 0 and b <= len(i)-1 and i[a] == i[b]:
            count += 2
            a -= 1
            b += 1
        result.append(count)
    if i[x+1] == i[x-1] and x > 0:
        count = 2
        result.append(count+1)
        a = x - 2
        b = x + 2
        while a >= 0 and b <= len(i)-1 and i[a] == i[b]:
            count += 2
            a -= 1
            b += 1
        result.append(count+1)
print(max(result))
