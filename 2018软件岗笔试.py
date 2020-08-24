#输入两个字母串，将两个字母串都包含的字母用’_'替换后，输出两个字母串的剩余部分。
#输入描述:输入两个字符串，字符串最大长度为100。字符串只包含字母，不可能为空串，区分大小写。
#输出描述:按字符串顺序输出处理后的字符串
#示例：
 #输入
   #abcd
   #bdef
 #输出
   #a_c_
   #__ef
i = list(input())
j = list(input())
i1 = []
j1 = []
for n1 in i:
    if n1 in j:
        i1.append("_")
    else:
        i1.append(n1)
for n2 in j:
    if n2 in i:
        j1.append("_")
    else:
        j1.append(n2)
print("".join(i1))
print("".join(j1))