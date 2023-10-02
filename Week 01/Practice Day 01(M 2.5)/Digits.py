t = int(input())
while t:
    n = input()
    reversed_n = n[::-1]
    for val in reversed_n:
        print(val,end=" ")
    print()
    t-=1