# in,not in,is,is not

#in
my_list = [1, 2, 3, 4, 5]
result = 3 in my_list  # This will be True
print(result)
ans = 6 in my_list  #This will be False
print(ans)

#not in
my_list = [1, 2, 3, 4, 5]
result2 = 6 not in my_list  # This will be True
print(result2)
ans2= 4 not in my_list #This will be False
print(ans2)


#is
x = [1, 2, 3]
y = x  # Both x and y refer to the same list in memory
result3 = x is y  # This will be True
print(result3)
z = [2, 4, 6]
ans3 = x is z #This will be False
print(ans3)


#is not
x = [1, 2, 3]
y = [1, 2, 3]  # A different list with the same contents
result4 = x is not y  # This will be True because x and y are different objects in memory
print(result4)
z = x
ans4 = x is not z # This will be True because x and z are same object in memory
print(ans4)