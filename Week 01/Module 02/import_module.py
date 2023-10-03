from function import print_it #import print_it function from function.py file

# Using 'if __name__ == "__main__":' ensures that the code inside the if block only runs when the script is executed directly and not when it's imported as a module.

print_it("Runa",22,"07-12-1999")


from function import * #using * import all from function.py file
ans = summ(3,3,3)
print(ans)