## 题目描述
      # Catcher是MCA国的情报员，他工作时发现敌国会用一些对称的密码进行通信，比如像这些ABBA，ABA，A，123321，但是他们有时会在开始或结束时加入一些无关的字符以防止别国破解。比如进行下列变化 ABBA->12ABBA,ABA->ABAKK,123321->51233214　。因为截获的串太长了，而且存在多种可能的情况（abaaab可看作是aba,或baaab的加密形式），Cathcer的工作量实在是太大了，他只能向电脑高手求助，你能帮Catcher找出最长的有效密码串吗？
## 输入描述:
      # 输入一个字符串
## 输出描述:
      # 返回有效密码串的最大长度

while True:
    try:
        i = input()
        result= []
        for x in range(len(i)-1):
            if i[x] == i[x+1]:
                count = 2
                result.append(count)
                a = x-1
                b = x+2
                while a >= 0 and b <= len(i)-1 and i[a] == i[b]:
                    count += 2
                    a -= 1
                    b += 1
                result.append(count)
            if i[x+1] == i[x-1] and x > 0:
                count = 2
                result.append(count+1)
                a = x - 2
                b = x + 2
                while a >= 0 and b <= len(i)-1 and i[a] == i[b]:
                    count += 2
                    a -= 1
                    b += 1
                result.append(count+1)
        print(max(result))
    except:
        break
