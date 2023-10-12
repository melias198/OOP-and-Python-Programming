class Phone:
    Model = "Infinix Hot 30"
    Brand = "Infinix"
    Produced = "Bangladesh"

    #Function is a Method
    def print_info(self): #self is Instance Method
        data = f"Model : {self.Model}. Brand : {self.Brand}. Made By : {self.Produced}"
        print(data)

New_Phone = Phone()
New_Phone.print_info()