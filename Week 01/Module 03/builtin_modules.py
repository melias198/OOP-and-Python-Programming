from math import *

print(pi)
print(ceil(4.3))
print(floor(4.3))
print(factorial(5))
print(isqrt(20)) #floor square value


from random import *

my_list = [1,2,3,4,5,6]
shuffle(my_list)
print(choice(my_list))

print(random()) #random value 0-1
print(randint(1,100)) #random value


from time import *

sleep(1)
print(localtime())


from datetime import *

now = datetime.now()
print(now)
current_date = date.today()
print(current_date) 

