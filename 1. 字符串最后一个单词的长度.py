## 题目描述
      # 计算字符串最后一个单词的长度，单词以空格隔开。 
## 输入描述:
      # 一行字符串，非空，长度小于5000。
## 输出描述:
      # 整数N，最后一个单词的长度。

      
# 方法一
def word_len():
    i = input()
    if len(i)== 0 or len(i)>5000:
        return "输入有误"
    else:
        return len(i.split(" ")[-1])
print(word_len())

# 方法二
import sys
i = sys.stdin.readline() #sys.stdin.readline( )会将标准输入全部获取，包括末尾的'\n'，input()会把‘\n’忽略
print(len(i.split(" ")[-1])-1)
