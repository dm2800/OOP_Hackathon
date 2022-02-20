class Pirate:

    def __init__( self , name ):
        self.name = name
        self.strength = 15
        self.speed = 3
        self.health = 100

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")
        if self.health < 0:
            print(f'GAME OVER: NINJA VICTORY.')

    def attack ( self , ninja ):
        ninja.health -= (self.strength * 3)
        print(f'Sparrow attacks!\nSparrow: I will end you, Ninja!')
        return self

    @classmethod
    def pirate_introduce(cls):
        print(f"Pirate: Arrr. You're going down, Ninja.")

