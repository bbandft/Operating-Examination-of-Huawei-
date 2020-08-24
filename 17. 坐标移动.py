while True:
    try:
        i = input().split(";")
        x= [0,0]
        y = list(map(str,list(range(100))))
        for n in i:
            if len(n) < 4:
                if n[1:] in y:
                    if n[0] == "A":
                        x[0] -= int(n[1:])
                    elif n[0] == "D":
                        x[0] += int(n[1:])
                    elif n[0] == "W":
                        x[1] += int(n[1:])
                    elif n[0] == "S":
                        x[1] -= int(n[1:])
        print("{0},{1}".format(x[0], x[1]))
    except:
        break
        tuple([0,1])


