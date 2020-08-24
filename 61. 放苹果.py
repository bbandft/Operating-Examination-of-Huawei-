def f(i,j):
    '''
放苹果分为两种情况，一种是有盘子为空，一种是每个盘子上都有苹果。
令(m,n)表示将m个苹果放入n个盘子中的摆放方法总数。
1.假设有一个盘子为空，则(m,n)问题转化为将m个苹果放在n-1个盘子上，即求得(m,n-1)即可
2.假设所有盘子都装有苹果，则每个盘子上至少有一个苹果，即最多剩下m-n个苹果，问题转化为将m-n个苹果放到n个盘子上
即求(m-n，n)
    '''
    if i<0 or j<0:
        return 0
    elif i==1 or j==1:
        return 1
    else:
        return f(i,j-1)+f(i-j,j)

while True:
    try:
        i,j = list(map(int,input().split(" ")))
        print(f(i,j))
    except:
        break