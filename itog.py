import requests
import json
def GetInfo(ID):
    try:
        pokemonInfoJS = requests.get(f'https://pokeapi.co/api/v2/pokemon/{ID}')
        if "name" not in pokemonInfoJS.text:
            raise NameError("Отсутствует информация о имени")
        elif "ability" not in pokemonInfoJS.text:
            raise NameError("Отсутствует информация о способностях")
        elif pokemonInfoJS.headers['Content-Type'] != 'application/json; charset=utf-8':
            raise TypeError("Файл имеет не JSON формат")
        pokemonInfoDC = json.loads(pokemonInfoJS.content)
        ab = list()
        for it in pokemonInfoDC['abilities']:
            ab.append(it['ability']['name'])
        return (f"Имя покемона: {pokemonInfoDC['name']}, его способности: {ab}")
    except Exception as e:
        raise Exception("Покемона с таким ID нет")
if __name__ == '__main__':
    print(GetInfo("56"))  
