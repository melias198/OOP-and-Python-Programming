def sum(a,b,c=0): # Here is c is default perameter,if i don't pass 3value he is is taking 0
    return a+b+c

print(sum(3,4,6))


def all_num(*numbers): #Here is * is args,which represent the function to accept any number of positional arguments
    print(numbers)  #its return a touple

all_num(1,2,3,4,5,6,7,8,9,10)

# args is usally optional,means we pass value or not it's don't return error

def all_sum(*numbers):
    sum=0
    for val in numbers:
        sum+=val
    return sum

ans = all_sum(1,2,3,4,5,6,7,8,9,10)
print("Sum:",ans)


def summ(a,b,c,*args):
    sum=a+b+c
    for val in args:
        sum+=val
    return sum

res = summ(1,2,3,4,5,6,7,8,9,10)
print("Result:",res)
