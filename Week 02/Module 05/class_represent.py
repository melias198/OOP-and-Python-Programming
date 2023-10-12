class Bio:
    name = 'Mohammad Elias'
    dist = 'Coxs Bazar'
    div = 'Chittagong'
    country = 'Bangladesh'

    def __repr__(self) -> str:
        otp = f'Name is {self.name}. Home District is {self.dist}. Home Division is {self.div}. Country is {self.country}.'
        return otp


print(Bio())