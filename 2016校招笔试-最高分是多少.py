id, n = list(map(int,input().split(" ")))
grade = list(map(int,input().split(" ")))
action = []
for i in range(n):
    action.append(input().split(" "))
for i in action:
    i = list(i)
    if i[0] == "Q":
        if int(i[1])>int(i[2]):
            print(max(grade[int(i[2]) - 1:int(i[1])]))
        else:
            print(max(grade[int(i[1])-1:int(i[2])]))
    elif i[0] == "U":
        grade[int(i[1])-1]=int(i[2])
