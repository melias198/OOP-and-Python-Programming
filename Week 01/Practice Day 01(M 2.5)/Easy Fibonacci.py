n = int(input())
a = 0
b = 1
if n==1:
    print(a)
elif n==2:
    print(a,end=" ")    
    print(b,end=" ")
else:
    print(a,end=" ")
    print(b,end=" ")
    for i in range(0,n-2):
        ans = a + b
        a = b
        b = ans
        print(ans,end=" ")
print()
  