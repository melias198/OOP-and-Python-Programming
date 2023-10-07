n = int(input())
v = list(map(int,input().split()))

flag = False
ans = 0

for val in v:
    if val%2==1:
        flag = True

if flag:
    print(0)
else:
    while True:
        check = False
        for i in range(n):
            if v[i]%2==1:
                check = True
                break
            else:
                v[i] = v[i]/2
        if check:
            break
        else:
            ans += 1
    print(ans)
