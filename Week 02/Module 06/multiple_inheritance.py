class Family:
    def __init__(self,type,member) -> None:
        self.type = type
        self.member = member

class Sports:
    def __init__(self,game,when) -> None:
        self.game = game
        self.when = when

class Club:
    def __init__(self,club_name,member_type) -> None:
        self.club = club_name
        self.member = member_type

class Student(Family,Sports,Club):
     def __init__(self, type, member,game,time,club,member_type) -> None:
         Family.__init__(self,type,member)
         Sports.__init__(self,game,time)
         Club.__init__(self,club,member_type)

     def __repr__(self) -> str:
         return f'Family type is {self.type} and his club is {self.club} and his favorite game {self.game}'

Kafi = Student('Single',10,'Cricket',10,'Student Club','Gold')
print(Kafi)
