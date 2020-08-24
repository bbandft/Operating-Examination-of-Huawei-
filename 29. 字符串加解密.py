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