n,m = map(int,input().split())
v = list(map(int,input().split()))

dict = {}
for val in v:
    if val in dict:
        dict[val] += 1
    else:
        dict[val] = 1

for i in range(1,m+1):
    if i not in dict:
        print(0)
    else:
        print(dict[i])