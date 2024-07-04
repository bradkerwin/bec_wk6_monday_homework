import requests
import json

response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
#print(response.status_code) # Prints the status code. Which is 200.

poke_info = response.json()
#print(poke_info) # Printing our information using json.

print(poke_info["abilities"])#[0]["ability"]["name"])
print(poke_info["forms"][0]["name"])


def fetch_pokemon_data(pokemon_name):
    return response.json()

def calculate_average_weight(pokemon_list):
    return #average weight

pokemon_names = ["pikachu", "bulbasaur", "charmander"]