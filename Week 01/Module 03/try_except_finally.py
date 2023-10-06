try:
    result = 50/0
    print(result)
except:
    print("Result is Infinity")
finally:
    print("This is finally Block")