def all_in_one(a,b,c):
    sum = a+b+c
    mul = a*b*c
    rem = a-b-c
    return sum,mul,rem # its return a touple
# if I return list then [sum,mul,rem]

ans = all_in_one(10,2,5)
print(ans)