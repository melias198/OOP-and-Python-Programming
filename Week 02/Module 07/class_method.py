class MyClass:
    Name = 'Karim'
    def __init__(self,name):
        self.name = name

    @classmethod
    def MyInstance(self,address):
        self.address = address

MyClass.MyInstance('Dhaka')
MyClass.address = 'Pekua'
print(MyClass.address)

