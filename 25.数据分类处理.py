## 题目描述
      # 信息社会，有海量的数据需要分析处理，比如公安局分析身份证号码、 QQ 用户、手机号码、银行帐号等信息及活动记录。  
      # 采集输入大数据和分类规则，通过大数据分类处理程序，将大数据分类输出。
## 输入描述:
      # 一组输入整数序列I和一组规则整数序列R，I和R序列的第一个整数为序列的个数（个数不包含第一个整数）；整数范围为0~0xFFFFFFFF，序列个数不限


while True:
    try:
        i = input().split()
        r = input().split()
        x1 = i.pop(0)
        x2 = r.pop(0)
        r = list(map(str,sorted(list(map(int,set(r))))))
        a = []
        for x in r:
            b = []
            c = 0
            d = []
            for y in i:
                d.append(y)
                if x in y:
                    index = len(d)-1
                    b.append(index)
                    b.append(y)
                    c += 1
            if c > 0:
                a.append(x)
                a.append(c)
                a += b
        a.insert(0,len(a))
        a = list(map(str,a))
        print(" ".join(a))        
    except:
        break
