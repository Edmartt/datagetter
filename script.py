"""Scrpit para extraer los datos de los jugadores de la API FUT21."""

import os
import requests
from datagetter.players_data import Players


class DataGetter:

    def __init__(self, query_gen: Players, base_url: str) -> None:
        self.query_gen = query_gen
        self.page = 1
        self.base_url = base_url

    def get_players_data(self) -> dict:

        args = {'pageCurrent': self.page} if self.page else {}
        headers = {'X-AUTH-TOKEN':os.environ.get('X_AUTH_TOKEN')}
        response = requests.get(url=self.base_url+'/players', params=args, headers=headers).json()

        return response


    def save_data_to_db(self, data_object: dict) -> None:

        player_names = []
        players_positions = []
        players_nations = []
        players_clubs = []

        for i in data_object['items']:
            player_names.append(i['name'])
            players_positions.append(i['position'])
            players_nations.append(i['nation'])
            players_clubs.append(i['club'])
        self.query_gen.insert_data(player_names, players_positions, players_nations, players_clubs)
    
    def go_to_next_page(self):
        while True:
            choice = input('Do you want to read the next page (Y/N): '.lower())

            if choice == 'y' and data_getter.page <= 908: 
                data_getter.page += 1
                data = data_getter.get_players_data()
                data_getter.save_data_to_db(data_object=data)
            else:
                break


# Una vez extraidos los datos de la primera pagina, se nos pregunta
# si queremos continuar leyendo los datos de la siguiente pagina y guardarlos


data_getter = DataGetter(Players(), os.environ.get('BASE_URL'))

data = data_getter.get_players_data()

data_getter.save_data_to_db(data_object=data)

data_getter.go_to_next_page()
