## 题目描述
      # 1、对输入的字符串进行加解密，并输出。
      # 2加密方法为：
            # 当内容是英文字母时则用该英文字母的后一个字母替换，同时字母变换大小写,如字母a时则替换为B；字母Z时则替换为a；
            # 当内容是数字时则把该数字加1，如0替换1，1替换2，9替换0；
            # 其他字符不做变化。
      # 3、解密方法为加密的逆过程。
## 说明：
      # 1、字符串以\0结尾。
      # 2、字符串最长100个字符。
      # int unEncrypt (char result[], char password[])：在该函数中实现字符串解密并输出
## 说明：
      # 1、字符串以\0结尾。
      # 2、字符串最长100个字符。
## 输入描述:
      # 输入说明
      # 输入一串要加密的密码
      # 输入一串加过密的密码
## 输出描述:
      # 输出说明
      # 输出加密后的字符
      # 输出解密后的字符


while True:
    try:
        i = input()
        j = input()
        def Encrypt(input):
            a = []
            for x in input:
                if x.isupper():
                    if x == "Z":
                        a.append("a")
                    else:
                        a.append(chr(ord(x)+1).lower())
                elif x.islower():
                    if x == "z":
                        a.append("A")
                    else:
                        a.append(chr(ord(x)+1).upper())
                elif x.isdigit():
                    if x == "9":
                        a.append(str(0))
                    else:
                        a.append(str(int(x)+1))
            print("".join(a))
        
        def unEncrypt(input):
            a = []
            for x in input:
                if x.isupper():
                    if x == "A":
                        a.append("z")
                    else:
                        a.append(chr(ord(x)-1).lower())
                elif x.islower():
                    if x == "a":
                        a.append("Z")
                    else:
                        a.append(chr(ord(x)-1).upper())
                elif x.isdigit():
                    if x == "0":
                        a.append(str(9))
                    else:
                        a.append(str(int(x)-1))
            print("".join(a))
        Encrypt(i)
        unEncrypt(j)
    except:
        break
