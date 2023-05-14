import mysql.connector
import os


class Database():

    def __init__(self) -> None:
        self.host = os.environ.get('MYSQL_HOST')
        self.user = os.environ.get('MYSQL_USER')
        self.password = os.environ.get('MYSQL_PASSWORD')
        self.database = os.environ.get('MYSQL_DATABASE')
        self.port = os.environ.get('MYSQL_PORT')

    def create_connection(self) -> tuple:
        '''Creates database connection.

        Takes the class variables as parameters to return a
        successful database connection.
        '''
        try:
            connection = mysql.connector.connect(
                    host=self.host,
                    user=self.user,
                    password=self.password,
                    database=self.database,
                    port=self.port
                    )
            cursor = connection.cursor(prepared=True)
            return connection, cursor
        except Exception as ex:
            return (ex,)
