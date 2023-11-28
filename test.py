import pokemon

input_poke = input("What pokemon do you want to search for?")
my_pokemon = pokemon.pokemonInfo(input_poke)

#test print basic data from api
print(f'{my_pokemon.id}:pokemon:{my_pokemon.name}\nheight:{my_pokemon.height}\nweight:{my_pokemon.weight}')

#test get type
print("\nTypes:")
for pokemon_type in my_pokemon.get_type_name():
    print(f"Type Name: {pokemon_type}")

#test calculation for weakness. Can cross check with https://bulbapedia.bulbagarden.net/
print("Weakness:")
weak = my_pokemon.check_type_weakness()
for key, value in weak.items():
    print(key + ":" + str(value))

#test get sprite image
img = my_pokemon.get_sprite(False,True)
img.show()
