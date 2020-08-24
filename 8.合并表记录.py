i = int(input())
a = {}
for n in range(i):
    index,value = list(map(int,input().split(" ")))
    if a.__contains__(index):
        a[index] = a[index]+value
    else:
        a[index] = value
for x in a.keys():
    print(str(x),str(a[x]))