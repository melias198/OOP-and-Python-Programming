t = int(input())
while t:
    x,y=map(int,input().split())
    a=min(x,y)
    b=max(x,y)
    sum = 0
    for val in range(a+1,b):
        if val&1:
            sum+=val
    print(sum)
    t-=1