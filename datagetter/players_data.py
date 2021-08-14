import logging
from datagetter.database import Database


class Players:

    def insert_data(self, names: list, positions: list,
                    nations: list, clubs: list) -> None:

        connection, cursor = Database.create_connection()
        query = '''INSERT INTO playersdata (name, position, nation, club)
            VALUES(%s, %s, %s, %s)'''

        try:
            cursor.executemany(query, zip(names, positions, nations, clubs))
            connection.commit()

            print('Datos agregados a la base de datos')
            return

        except Exception as ex:
            logging.exception('Exception in: ')
        finally:
            connection.close()
