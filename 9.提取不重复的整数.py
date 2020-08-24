## 题目描述
      # 输入一个int型整数，按照从右向左的阅读顺序，返回一个不含重复数字的新的整数。
## 输入描述:
      # 输入一个int型整数
## 输出描述:
      # 按照从右向左的阅读顺序，返回一个不含重复数字的新的整数


i = input()
i = i[::-1]
x=[]
for n in range(len(i)):
    y = i[n]
    if y not in x:
        x.append(i[n])
print("".join(x))
