while True:
    try:
        i = int(input())
        n = 2
        j = []
        while i!=1:
            if i%n==0:
                j.append(n)
                i = i/n
            else:
                n +=1
        i = " ".join(str(i) for i in j)+" "
        print(i)
    except:
        break