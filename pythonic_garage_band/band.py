class Musician():
    def __str__(self):
          return f"My name is {self.name} and I play {self.get_instrument()}"
    
    def __repr__(self):
          return f"{self.role()} instance. Name = {self.name}"


class Guitarist(Musician):
    def __init__(self, name ):
          self.name = name

    def get_instrument(cls):
         return "guitar"
    
    def role (cls):
         return "Guitarist"
    
    def play_solo(cls):
         return "face melting guitar solo"


class Drummer(Musician):
    def __init__(self, name):
          self.name = name

    def get_instrument(cls):
        return "drums"
    
    def role (cls):
         return "Drummer"
    
    def play_solo(cls):
        return "rattle boom crash"


class Bassist(Musician):
    def __init__(self, name):
          self.name = name

    def get_instrument(cls):
        return "bass"

    def role (cls):
         return "Bassist"
    
    def play_solo(cls):
        return "bom bom buh bom"

class Band(Musician):

    def __init__ (self, name = None, members = [] ):
        self.name = name
        self.members = members
        
    def __str__(self):
        return f"The band name is {self.name} and the musicians are {self.members()}"
    
    def __repr__(self):
        return f"Name = {self.name}"
    
    def __len__(self):
        return len(self.instances)
    
    def role(self):
        if self.name == "guitar": return "face melting guitar solo"
        return f"Band instance.Name = {self.name}"
    
    def play_solos (self):
        solos = []
        for person in self.members:
             solos.append(person.play_solo())
        return solos
    






