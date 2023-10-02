x,y=map(int,input().split())
sum = 0
for i in range(2,y+1,2):
    sum+=x**i
print(sum)