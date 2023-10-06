# mutable means changeable 
# immutable means unchangeable
# string is sequence of character
# we can acces string value with index but we cannot reassign value thats why its immutable

name = "Mohammad Elias"
print(name[4])
print(name[:])
print(name[::-1])
print(name[-4])

# name[4]='r' we can't do this

if 'amma' in name:
    print("Yes")
else:
    print("No")