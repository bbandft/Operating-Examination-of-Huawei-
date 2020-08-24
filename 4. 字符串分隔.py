## 题目描述
      # 连续输入字符串，请按长度为8拆分每个字符串后输出到新的字符串数组； 
      # 长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。 
## 输入描述:
      # 连续输入字符串(输入2次,每个字符串长度小于100)
## 输出描述:
      # 输出到长度为8的新字符串数组

    
while True:
    try:
        i = input()
        j = input()
        while len(i)>8:
            if type(i) is str:
                print(i[:8])
            else:
                print("".join(i[:8]))
            i = list(i)
            del (i[:8])
        for n in range(8-len(i)):
            i += "0"
        print("".join(i))
        while len(j)>8:
            if type(j) is str:
                print(j[:8])
            else:
                print("".join(j[:8]))
            j = list(j)
            del (j[:8])
        for n in range(8-len(j)):
            j += "0"
        print("".join(j))
    except:
        break
