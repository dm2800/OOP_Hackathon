class Ninja:

    def __init__( self , name ):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 100
    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")
        if self.health < 0:
            print(f'GAME OVER: PIRATE VICTORY.')

    def attack( self , pirate ):
        pirate.health -= (self.strength * 2)
        print(f'Ninja attacks!\nNinja: Take that, Sparrow!')
        return self

    @classmethod
    def ninja_introduce(cls):
        print('Ninja: In the name of the Ninja code, I will defeat you.')

class Blue_Ninja(Ninja):
    
    def __init__( self, name ):
        super().__init__(name)
    def show_stats( self ):
        super().show_stats()
        return self
    def attack( self, pirate):
        pirate.health -= (self.strength * 3)
        print(f"Leonardo attacks!\nLeonardo: You're finished, Sparrow!")
        return self
    @classmethod
    def ninja_introduce(cls):
        super().ninja_introduce()
