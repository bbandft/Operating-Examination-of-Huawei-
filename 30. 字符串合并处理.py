# 题目描述
    # 按照指定规则对输入的字符串进行处理。
# 详细描述：
    # 将输入的两个字符串合并。
# 对合并后的字符串进行排序，要求为：下标为奇数的字符和下标为偶数的字符分别从小到大排序。这里的下标意思是字符在字符串中的位置。
# 对排序后的字符串进行操作，如果字符为‘0’——‘9’或者‘A’——‘F’或者‘a’——‘f’，则对他们所代表的16进制的数进行BIT倒序的操作，并转换为相应的大写字符。如字符为‘4’，为0100b，则翻转后为0010b，也就是2。转换后的字符为‘2’； 如字符为‘7’，为0111b，则翻转后为1110b，也就是e。转换后的字符为大写‘E’。

# 举例：输入str1为"dec"，str2为"fab"，合并为“decfab”，分别对“dca”和“efb”进行排序，排序后为“abcedf”，转换后为“5D37BF”

while True:
    try:
        str = input().split()
        str = str[0] + str[1]
        str1 = []
        odd = []
        even = []
        for i in range(len(str)):
            if i % 2 == 0:
                even.append(str[i])
            else:
                odd.append(str[i])
        str1 = [0 for i in range(len(str))]
        odd = sorted(odd)
        even = sorted(even)
        for i in range(len(str1)):
            if i % 2 == 0:
                str1[i] = even.pop(0)
            else:
                str1[i] = odd.pop(0)
        final = []
        for i in str1:
            if i in '0123456789abcdefABCDEF':
                number_2 = bin(int(i, 16))
                number_2 = list(number_2)[2:]
                number_add = ["0" for i in range(4 - len(number_2))]
                number_2 = number_add + number_2
                number_2 = number_2[::-1]
                number_2 = "".join(number_2)
                result = hex(int(number_2, 2))[2:].upper()
                final.append(result)
            else:
                final.append(i)
        print("".join(final))
    except:
        break
