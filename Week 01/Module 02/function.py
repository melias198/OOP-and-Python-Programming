def summ(a,b,c):
    sum = a+b+c
    return sum

ans = summ(3,6,9)
if __name__ == "__main__": #Using if __name__ == "__main__": ensures that the code inside the if block only runs when the script is executed directly and not when it's imported as a module.
    print(ans)

def print_it(name,age,DOB):
    print(f"Name: {name}\nAge: {age}\nDOB: {DOB}")

if __name__ == "__main__":
    print_it("Mohammad Elias",22,"10-03-2000")