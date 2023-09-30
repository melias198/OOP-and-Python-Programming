lists = [1,2,3,4,5,6,7,8,9,10]
for val in lists:
    print(val)

for i,val in enumerate(lists): #enumerate function iterate over the array and get both index and element
    print(f'Index: {i} and Value: {val}')


for i,val in enumerate(lists,1): #changing indexing
    print(f'Index: {i} and Value: {val}')

for i in range(1,10,2):
    print(i)


for i,val in enumerate(range(1,10,2)):
    print(f'Index: {i} and Value: {val}')


text = 'Hello Python'
for char in text:
    print(char)