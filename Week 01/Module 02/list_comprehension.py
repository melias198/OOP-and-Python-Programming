numbers = [3,5,4,9,15,20,25,17,2]

odds = []
for num in numbers:
    if num&1 and num%5==0:
        odds.append(num)
print(odds)

comprehension_odds = [num for num in numbers if num&1 if num%5==0] #comprehension, kind of shortcut
print(comprehension_odds)


x_axis = [1,2,3]
y_axis = [1,2,3]

coor = []
for x in x_axis:
    for y in y_axis:
        coor.append((x,y))
print(coor)

coordinate = [(x,y) for x in x_axis for y in y_axis] #Comprehension
print(coordinate)