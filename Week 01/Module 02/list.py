nums = [5,3,8,1,9,2]

for i in range(0,len(nums)):
    print(nums[i],end=" ")

print()

for i in nums[::-1]: #reverse printing
    print(i,end=" ")
print()

print(nums[2:5])
print(nums[0:6:2])
print(nums[0:6:1])
print(nums[6:2:-1])
print(nums[6:1:-2])
print(nums[3:])
print(nums[:4])
print(nums[::])
