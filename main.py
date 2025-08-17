import requests

URL = 'https://api.pokemonbattle.ru/v2'

TOKEN = 'c6e6ac35110058aee065ab63e8ddb0ef'
HEADER ={'Content-Type' : 'application/json', 'trainer_token' : f'{TOKEN}'}
body_registration = {
    "email": "name",
    "password": "password",
    "trainer_token": "c6e6ac35110058aee065ab63e8ddb0ef",
    "password_re": "09SASA03irisha"  
}
body_confirmation = {
    "trainer_token": TOKEN
} 

body_create = {
    "name": "Бэтмен",
    "photo_id": 1
}

add_pokeball = {
    "pokemon_id": "376293"
}

change_pokemon = {
    "pokemon_id": "376293",
    "name": "generate",
    "photo_id": 8
}


'''Создание покемона'''
response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create )
print(response_create.json())

'''Поймать покемона в покебол'''
response_create = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = add_pokeball)
print(response_create.json())

'''Смена имени покемона'''
response_create = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = change_pokemon)
print(response_create.json())

'''response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(response.text)''' 

'''response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation)
print(response_confirmation.text)'''


'''pokemon_id = response_create.json()['id']
print(pokemon_id)'''



