numbers = [2,5,7,3,9,10,15,7,3]

numbers.append(20)
print(numbers)

numbers.insert(0,1)
print(numbers)

cnt = numbers.count(7)
print("Count:",cnt)

if 7 in numbers:
    numbers.remove(7)
print(numbers)

if 3 in numbers:
    index = numbers.index(3)
    print("Index =",index)

delete = numbers.pop(numbers[3])
print(numbers)

last = numbers.pop()
print(numbers)

numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

sorted_list = sorted(numbers,reverse=True)
print(sorted_list)
