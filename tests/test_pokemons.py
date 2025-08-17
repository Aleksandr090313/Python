import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'

TOKEN = 'c6e6ac35110058aee065ab63e8ddb0ef'
HEADER ={'Conten-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '42215'

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params= {'trainer_id': TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["name"] == 'mudsdale'


@pytest.mark.parametrize('key, value', [('name', 'mudsdale'),('trainer_id', TRAINER_ID),('id', '376293')])
def test_parametrize(key, value):
    response_parametrize = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response_parametrize.json()["data"][0][key] == value