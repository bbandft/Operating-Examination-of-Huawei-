while True:
    try:
        import sys
        n=int(sys.stdin.readline().strip())
        inputArray = []
        for i in range(n):
            inputArray.append(int(sys.stdin.readline().strip()))
        result = sorted(list(set(inputArray)))
        for c in result:
            print(c)
    except:
        break
