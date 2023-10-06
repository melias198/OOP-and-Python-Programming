# def double_it(x):
#     return 2*x
# print(double_it(5))


double_it = lambda x: x*2
print(double_it(5))

# def squared(x):
#     return x*x
# print(squared(2))


squared = lambda x: x*x
print(squared(5))


numbers = [2,4,6,8,10]
# result = map(double_it,numbers)
# print(numbers)
# print(list(result))

result = map(lambda x: x*2,numbers)
print(numbers)
print(list(result))


actres = [
    {'Name': 'Mehzabin', 'Age': 30},
    {'Name': 'Sabila', 'Age': 31},
    {'Name': 'Tisha', 'Age': 35},
    {'Name': 'Totini', 'Age': 25},
    {'Name': 'Sadia', 'Age': 26},
]

youngers = filter(lambda actor: actor['Age']<30,actres)
print(list(youngers))

fivers = filter(lambda actor: actor['Age']%5==0,actres)
print(list(fivers))
