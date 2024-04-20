import requests

pokemon = input()

print(pokemon)

r = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")

pokemon_json = r.json()

moves = pokemon_json['moves']
print("=======moves========")
for move in moves[:10]:
    move_json = requests.get(move['move']['url']).json()
    
    print(move['move']['name'])
    move_acc = move_json['accuracy']
    move_class = move_json['damage_class']['name']
    move_type = move_json['type']['name']
    print(move_acc, move_class, move_type, sep=" | ")
    print()
