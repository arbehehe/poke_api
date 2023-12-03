import requests
from PIL import Image
from io import BytesIO

poke_type_id = {
    "normal": 1,
    "fighting": 2,
    "flying": 3,
    "poison": 4,
    "ground": 5,
    "rock": 6,
    "bug": 7,
    "ghost": 8,
    "steel": 9,
    "fire": 10,
    "water": 11,
    "grass": 12,
    "electric": 13,
    "psychic": 14,
    "ice": 15,
    "dragon": 16,
    "dark": 17,
    "fairy": 18
}

class api_handle:
    _BASE_URL = 'https://pokeapi.co/api/v2/'
    _SPRITE_BASE_URL = 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/'
    
    def __make_request(self, api: str)->requests.Response:
        try:
            response = requests.get(api)
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx status codes)
            return response
        except requests.RequestException as e:
            raise Exception(f"Request to {api} failed: {str(e)}")
    
    def get_request_pokemon(self, pokemon)->requests.Response:
        api = f'{self._BASE_URL}pokemon/{pokemon}/'
        return self.__make_request(api)
    
    def get_request_type(self, type: str)->requests.Response:
        api = f'{self._BASE_URL}type/{poke_type_id[type]}'
        return self.__make_request(api)
    
    def get_request_sprite(self, id: int, back_sprite: bool, shiny: bool)->Image.Image:
        api = f'{self._SPRITE_BASE_URL}{"back/" if back_sprite else ""}{"shiny/" if shiny else ""}{id}.png'
        response = self.__make_request(api)
            
        response = Image.open(BytesIO(response.content))
        return response
        
queried_type_storage_dict = {}

class pokemonInfo:  
    
    api = api_handle()
    
    def __init__(self, pokemon_name):
        self.data = self.api.get_request_pokemon(pokemon_name).json()
            # Access specific information from the JSON
        for key, value in self.data.items():
            setattr(self, key, value)
        
    def get_type_name(self):
        types = self.data.get('types', [])
        return [type_data['type']['name'] for type_data in types]
    
    def get_sprite(self, back_view = False, shiny = False):
        return self.api.get_request_sprite(self.data.get('id'), back_view, shiny)
        
    def __process_pokemon_type_weakness(self):
        
        type_weakness = {}
        for poke_type in self.get_type_name():
            if poke_type not in queried_type_storage_dict:
                response = self.api.get_request_type(poke_type).json()
                double_damage_from = [type_data['name'] for type_data in response['damage_relations']['double_damage_from']]
                half_damage_from = [type_data['name'] for type_data in response['damage_relations']['half_damage_from']]
                no_damage_from = [type_data['name'] for type_data in response['damage_relations']['no_damage_from']]

                type_weakness[poke_type] = {
                    'double_damage_from': double_damage_from,
                    'half_damage_from': half_damage_from,
                    'no_damage_from': no_damage_from
                }
            else:
                type_weakness[poke_type] = queried_type_storage_dict[poke_type]
        return type_weakness
                
    def check_type_weakness(self):
        type_relation = {
            "normal": 1,
            "fighting": 1,
            "flying": 1,
            "poison": 1,
            "ground": 1,
            "rock": 1,
            "bug": 1,
            "ghost": 1,
            "steel": 1,
            "fire": 1,
            "water": 1,
            "grass": 1,
            "electric": 1,
            "psychic": 1,
            "ice": 1,
            "dragon": 1,
            "dark": 1,
            "fairy": 1
        }
        data = self.__process_pokemon_type_weakness()
        for type_name, weaknesses in data.items():
            for key in type_relation.keys():
                if key in weaknesses['double_damage_from']:
                    type_relation[key] *= 2
                if key in weaknesses['half_damage_from']:
                    type_relation[key] *= 0.5
                if key in weaknesses['no_damage_from']:
                    type_relation[key] *= 0 
        return type_relation
                    
        
            
            
            
        
        
        
        


          

        
        
            