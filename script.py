"""Scrpit para extraer los datos de los jugadores de la API FUT21."""

import requests
from datagetter.players_data import Players


def get_data(url: str =
             "https://www.easports.com/fifa/ultimate-team/api/fut/item",
             page: int = 1) -> None:

    players_data = Players()

    args = {'page': page} if page else {}

# listas con las propiedades de los jugadores
    player_names = []
    players_positions = []
    players_nations = []
    players_clubs = []

# Obtenemos la respuesta de la API y la serializamos a json
    response = requests.get(url, params=args).json()

# Iteramos sobre la estructura items del response para sacar
# los datos solicitados en el ejercicio
    for i in response['items']:

        player_names.append(i['firstName'] + ' ' + i['lastName'])
        players_positions.append(i['position'])
        players_nations.append(i['nation']['name'])
        players_clubs.append(i['club']['name'])

    players_data.insert_data(player_names, players_positions,
                             players_nations, players_clubs)

# Una vez extraidos los datos de la primera pagina, se nos pregunta
# si queremos continuar leyendo los datos de la siguiente pagina y guardarlos

    choice = input('Do you want to read the next page (Y/N): '.lower())
    page += 1
    if choice == 'y' and page <= 908:
        get_data(url, page)
        return


get_data()
