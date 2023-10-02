k,s=map(int,input().split())
cnt = 0
for i in range(k+1):
    for j in range(k+1):
        rem_sum=s-i-j 
        if rem_sum >=0 and rem_sum<=k:
            cnt+=1
print(cnt)