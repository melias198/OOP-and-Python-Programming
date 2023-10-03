def full_name(first,last):
    name = f"My name is: {first} {last}"
    return name

name = full_name(last="Hossen",first="Sohrab") #For doing this we can pass value in unordered
print(name)



def biodata(first,last,**addition): # Here is ** is called kargs. It is used in function definitions to allow a variable number of keyword arguments to be passed to a function, which are then collected into a dictionary. 
    bio = f"My Name is {first} {last}. I'm {addition['age']} years old. My Father name is {addition['father']}. My Birthdate is {addition['DOB']}."
    return bio

bio = biodata(first="Mohammad",last="Elias",age=22,father="Ahmed Hossen",DOB="10-03-2000")
print(bio)



def data(**addition): # Here is ** is called kargs. It is used in function definitions to allow a variable number of keyword arguments to be passed to a function, which are then collected into a dictionary. 
    for key,val in addition.items():
        print("Key:",key,"-> Value:",val)
    

data(first="Mohammad",last="Elias",age=22,father="Ahmed Hossen",DOB="10-03-2000")

    