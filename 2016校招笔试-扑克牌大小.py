i,j = input().split("-")
if i == "joker JOKER" or j =="joker JOKER":
    print("joker JOKER")
else:
    a = i.split(" ")
    b = j.split(" ")
    x = ['3','4','5','6','7','8','9','10','J','Q','K','A','2','joker','JOKER']
    if len(a) == len(b):
        c=0
        d=0
        for m in a:
            c += x.index(m)
        for m in b:
            d += x.index(m)
        if c > d:
            print(i)
        elif c < d:
            print(j)
        else:
            print("ERROR")
    elif len(a) == 4:
        print(i)
    elif len(b) ==4:
        print(j)
    else:
        print("ERROR")