class Musician():
    def __str__(self):
          return f"My name is {self.name} and I play {self.get_instrument()}"
    
    def __repr__(self):
          return f"{self.play_solo()} instance. Name = {self.name}"


class Guitarist(Musician):
    def __init__(self, name ):
          self.name = name

    def get_instrument(cls):
         return "guitar"
    
    def play_solo (cls):
         return "Guitarist"


class Drummer(Musician):
    def __init__(self, name):
          self.name = name

    def get_instrument(cls):
        return "drums"
    
    def play_solo (cls):
         return "Drummer"


class Bassist(Musician):
    def __init__(self, name):
          self.name = name

    def get_instrument(cls):
        return "bass"

    def play_solo (cls):
         return "Bassist"


class Band(Musician):
      def __init__ (self, name = None, play_solos = None, members = []):
        self.name = name
        self.members = members
        self.play_solos = play_solos

    
   