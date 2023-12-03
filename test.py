from pokemon import pokemonInfo

#test pokemon type data
def test_weakness_calculation(obj: pokemonInfo):
    print(f'{obj.id}:pokemon:{obj.name}\nheight:{obj.height}\nweight:{obj.weight}')
    print("\nTypes:")
    for pokemon_type in obj.get_type_name():
        print(f"Type Name: {pokemon_type}")

    #test calculation for weakness. Can cross check with https://bulbapedia.bulbagarden.net/
    print("Weakness:")
    weak = obj.check_type_weakness()
    for key, value in weak.items():
        print(key + ":" + str(value))

#test get sprite image
def test_get_sprite(obj: pokemonInfo):
    img = obj.get_sprite(False,True)
    img.show()

    
input_poke = input("What pokemon do you want to search for?")
my_pokemon = pokemonInfo(input_poke)

test_weakness_calculation(my_pokemon)
test_get_sprite(my_pokemon)
