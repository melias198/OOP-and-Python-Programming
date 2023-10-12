class BioData:
    def __init__(self,name,age,address,subject): #Constructor
        self.Name = name
        self.Age = age
        self.Address = address
        self.Subject = subject
    
    def __repr__(self) -> str: #Class Representor
        return f"Applicant Details:\nName : {self.Name}\nAge : {self.Age}\nAddress : {self.Address}\nSubject : {self.Subject}"
        
Alif = BioData("Alif Shah",25,"Dhaka","Bio Chemistry")
print(Alif)

print()

Shahi = BioData("Muntasir Sahi",24,"Chittagong","Phermacy")
print(Shahi)