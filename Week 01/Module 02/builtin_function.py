a = abs(5-9)
print(a)

numbers=[1,3,5,7,9]
#all() function that returns True if all elements in an iterable are True, and it returns False if at least one element in the iterable is False
all_func=all(num&1 for num in numbers) 
print(all_func)

nums = [1,3,5,8,7,9]
#any() function that returns True if at least one element in an iterable is True or evaluates to True. If all elements in the iterable are False, it returns False
any_func=any(num%2==0 for num in nums)
print(any_func)

print(complex(6))

lists = [2,5,3,7,9,4]
for i,val in enumerate(lists):
    print("Index:",i,"<-> Value:",val)

print(len(lists))

x = int(input('Give me value of x: '))
print(pow(x,2))