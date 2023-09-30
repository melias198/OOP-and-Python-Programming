# newline separated input

n = int(input())
v = []

for i in range(n):
    val = int(input())
    v.append(val)

# sum = 0
# for val in v:
#     sum+=val

sum=sum(v)
print(sum)



# space separated input

# Take the entire input line as a space-separated string
input_line = input("Enter the elements separated by spaces: ")

# Split the input line into a list of strings
elements = input_line.split()

# Convert the list of strings to a list of integers
v = [int(element) for element in elements]

# Calculate the sum of the elements in the list
sum_val = sum(v)

print("Sum of elements:", sum_val)

