from random import *
from time import *

n = int(input("Numbers of perticipate: "))
name_lists = []

print("Lists of Perticipant: ")
for i in range(n):
    name = input()
    name_lists.append(name)

shuffle(name_lists)
winner=choice(name_lists)
sleep(2)
print("Winner is: ",winner)

