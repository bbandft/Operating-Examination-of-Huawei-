while True:
    try:
        i = input()
        count = []
        result = []
        for n in i:
            count.append(i.count(n))
        #count 全部填完后才能得到真正的最小值
        for n in i:
            if i.count(n) != min(count):
                result.append(n)
        print("".join(result))
    except:
        break