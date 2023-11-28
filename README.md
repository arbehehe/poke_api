<h1 style="font-size: 24px;">poke_api</h1>
Get api from (https://pokeapi.co/) and process your pokemon type weakness

**Installation**

pip install -r requirements.txt

**Usage**
```python
from pokemon import pokemonInfo

#Example usage
my_pokemon = pokemonInfo("pikachu")
type_weakness = my_pokemon.check_type_weakness()
print(type_weakness)
```

**API Handle**

Methods

get_request_pokemon(pokemon: str) -> requests.Response: Get information about a specific Pokémon.

get_request_type(type: str) -> requests.Response: Get information about a Pokémon type.

get_request_sprite(id: int, back_sprite: bool, shiny: bool) -> Image.Image: Get a Pokémon sprite.

**Pokemon Info**

Methods

__init__(pokemon_name: str) -> None: Initialize a PokemonInfo instance with the given Pokemon name.

get_type_name() -> List[str]: Get a list of Pokemon types.

get_sprite(back_view: bool = False, shiny: bool = False) -> Image.Image: Get a Pokemon sprite.

check_type_weakness() -> Dict[str, float]: Check type weaknesses of the Pokemon.

Type Relations
calculate pokemon weakness based on type return from api



