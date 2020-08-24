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