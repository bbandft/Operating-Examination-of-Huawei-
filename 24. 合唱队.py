import bisect
def deal(height):
    d=[]
    count=[]
    for i in height:
        if not d:
            d.append(i)
            count.append(1)

        elif d[-1] < i:
            d.append(i)
            count.append(count[-1]+1)

        else:
            d[bisect.bisect_left(d,i)] = i
            count.append(count[-1])

    return count
n = int(input())
height = list(map(int,input().split(" ")))
forward = deal(height)
back = deal(height[::-1])[::-1]
print(forward)
result = max(forward[i]+back[i] for i in range(n))
print(n-result+1)
