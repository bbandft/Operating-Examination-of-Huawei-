## 题目描述
## 密码要求:
      # 1.长度超过8位
      # 2.包括大小写字母.数字.其它符号,以上四种至少三种
      # 3.不能有相同长度大于2的子串重复
## 输入描述:
      # 一组或多组长度超过2的子符串。每组占一行
## 输出描述:
      # 如果符合要求输出：OK，否则输出NG


while True:
    try:
        i = input()
        has_number = 0
        has_lower  = 0
        has_upper = 0
        has_symbols = 0
        if len(i) >8:
            for n in i:
                if "a" <= n <= "z":
                    has_lower = 1
                elif "A" <= n <= "Z":
                    has_upper = 1
                elif "0" <= n <= "9":
                    has_number =1
                else:
                    has_symbols =1
            e = True
            for m in range(len(i) - 2):
                if i.count(i[m:m + 3])>=2:
                    e = False
            if has_lower+has_upper+has_number+has_symbols >= 3 and e:
                print("OK")
            else:
                print("NG")
        else:
            print("NG")
    except:
        break
