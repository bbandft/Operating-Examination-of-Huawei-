i = input()
if "." in i:
    if len(i)-i.index(".") > 2:
        print("请输入到小数点后一位")
    else:
        if int(i[i.index(".")+1]) >= 5:
            print(int(float(i))+1)
        else:
            print(int(float(i)))
else:
    print(i)