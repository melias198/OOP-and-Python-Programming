n = int(input())
v = list(map(int, input().split()))

dict = {}
for val in v:
    if val in dict:
        dict[val] += 1
    else:
        dict[val] = 1

ans = 0
for key, value in dict.items():
    if key <= value:
        ans += value - key
    else:
        ans += value

print(ans)
