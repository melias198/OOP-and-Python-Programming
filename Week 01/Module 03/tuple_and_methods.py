# Tuple in immutable

my_tuple = (1,3,4,5,6,7,8)
print(my_tuple)


mix_tuple = (1,2,"Dhaka",10.5)
print(mix_tuple)


nestes_tuple = ((1,2,3),[4,5,6],"Chittagong")
print(nestes_tuple)


new_tuple = 1,2,3,4,5,6,7,8,8
print(new_tuple[3])
print(new_tuple[-7])
print(new_tuple[::])
print(new_tuple[::-1])
print(new_tuple[:4])
print(new_tuple[4:])
print(new_tuple[::2])

print(new_tuple.count(8))

lang_tuple = "C","C++","Python"
print(lang_tuple)

for item in lang_tuple:
    print(item)


print("Python" in lang_tuple)
