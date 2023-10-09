## Theory Question

### Write the difference between List and Dictionary of Python.
```
List:
1. List is a collection of ordered elements.
2. List is created by putting the elements within the square brackets.
3. Elements in a List are accessed using indices.
4. The order of elements entered in a List is always maintained.
5. Lists are used as an ordered collection of items where the order or the position of elements matters.

Dictionary: 
1. Dictionary is a hash structure comprising key-value pairs.
2. Dictionaries are created by putting the key-value pair within the curly brackets.
3. Elements in a Dictionary are accessed using key-values.
4. Dictionaries are unordered, so there is no specific order to the key-value pairs.
5. Dictionaries are used when associate values with unique keys.
```

### Write about *args and **kwargs of Python with proper examples.
```
*args:
In Python, *args is commonly used to pass a variable number of arguments to a function. It is used to pass a non-keyworded, variable length argument list. We use the syntax *args with the single star.
Example:
def all_sum(*numbers):
    sum=0
    for val in numbers:
        sum+=val
    return sum


ans = all_sum(1,2,3,4,5,6,7,8,9,10)
print("Sum:",ans)


**kwargs:
In Python, *kwargs is used to pass a keyworded, variable length argument list.Keyword argument is provided the keys are the argument names and the values are the corresponding argument values. We use the syntax **kwargs with the double star.
Example:
def data(**addition):
    for key,val in addition.items():
        print("Key:",key,"-> Value:",val)
   


data(first="Mohammad",last="Elias",age=22,father="Ahmed Hossen",DOB="10-03-2001")
```