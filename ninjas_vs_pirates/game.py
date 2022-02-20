from classes.ninja import Ninja, Blue_Ninja
from classes.pirate import Pirate

michelangelo = Ninja("Michelanglo")
leonardo = Blue_Ninja("Leonardo")


Ninja.ninja_introduce()
Pirate.pirate_introduce()

jack_sparrow = Pirate("Jack Sparrow")
jack_sparrow.show_stats()
leonardo.show_stats()
leonardo.attack(jack_sparrow)
jack_sparrow.show_stats()


jack_sparrow.attack(leonardo)
leonardo.show_stats()

leonardo.attack(jack_sparrow)
jack_sparrow.show_stats()

leonardo.attack(jack_sparrow)
jack_sparrow.show_stats()

jack_sparrow.attack(leonardo)
leonardo.show_stats()

leonardo.attack(jack_sparrow)
jack_sparrow.show_stats()


