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