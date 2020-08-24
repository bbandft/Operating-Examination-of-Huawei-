## 题目描述
      # 功能:输入一个正整数，按照从小到大的顺序输出它的所有质因子（重复的也要列举）（如180的质因子为2 2 3 3 5 ）
      # 最后一个数后面也要有空格

## 输入描述:
      # 输入一个long型整数
## 输出描述:
      # 按照从小到大的顺序输出它的所有质数的因子，以空格隔开。最后一个数后面也要有空格。


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
