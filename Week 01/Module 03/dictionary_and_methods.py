person = {
    'Name' : 'Elias',
    'Age' : 22,
    'Birth Place' : 'Cox,s Bazar',
    'Nationality' : 'Bangladesh'
}

print(person)
print(person['Name'])
person['Name'] = 'Mohammad Elias' #Change 
print(person)
person['Address'] = 'Chawk Bazar' #Add item
print(person)

del person['Age'] #Delete
print(person)


num = {
    1: 100,
    2: 200,
    3: 300,
    4: 400
}
print(num)


#Key Print
for key in num:
    print(key)

#Value Print
for key in num:
    val = num[key]
    print(val)

#Key and Value Print
for key,val in num.items():
    print(key,"-->",val)