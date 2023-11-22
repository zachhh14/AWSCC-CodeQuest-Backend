#I think I made a mistake in activating the virtual environment but this is what I did:

""" 
`source c:/Users/Zach/repos/AWSCC-CodeQuest-Backend/virtual_enviroment/Scripts/activate` 
installed the requests
`python -m pip install requests`
verify if the requests module is unstalled
`python -m pip list`
"""

# get the list of pokemons from PokeAPI
# reference: https://pokeapi.co/docs/v2
import requests

response = requests.get("https://pokeapi.co/api/v2/pokemon")
data = response.json()
for pokemon in data['results']:
    print(pokemon['name'])