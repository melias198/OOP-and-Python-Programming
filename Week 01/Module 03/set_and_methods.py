# Unique item collection
new_set = {1,2,3,3,4,5,5,6}
print(new_set)

vowel_set = {'a','e','i','o','u'}
print(vowel_set)

mix_set = {5,"Dhaka",7.3}
print(mix_set)


empty_set =set() # using just carly braces its known as empty dictionary

init_set = {2,4,6,8}
init_set.add(10)
print(init_set)

student = {'Karin','Rahim','Kalam','Shafiq'}
new_student = ['Rafith','Jahin','Shahin']

student.update(new_student) # update used to update the set with items other collection types(list,tuple,set,etc.)
print(student)


remove_val = student.discard('Kalam') # discard used to remove value
print(student)


lang_set = {'C','C++','Python'}
for item in lang_set:
    print(item)

print(len(lang_set))


A = {1,3,5,4}
B = {0,2,4,5}

# Perform union using '|' or union()
print(A|B)
print(A.union(B))

# Perform intersection using '&' or intersection()
print(A&B)
print(A.intersection(B))

# Perform difference operation using '-' or difference()
print(A-B)
print(A.difference(B))

# The symmetric difference between two sets A and B includes all elements of A and B without the common elements.
# Perform symmetric difference using '^' or symmetric_difference()
print(A^B)
print(A.symmetric_difference(B))