from dojopet_ninja import ninja
from dojopet_mascot import doggy, kitty

#Pets
Snowy = doggy("Snowy","Berries",100, 100)
Pippin = kitty("Pippin", "Puffins", 100, 100)

#Ninjas
Lily = ninja ("Lily",[Snowy, Pippin], "Puffins","Pokeblocks")

#Execution
Lily.walk().bathe().feed()