from os import environ
import mysql.connector


class Database():
    __host = environ.get('MYSQL_HOST')
    __user = environ.get('MYSQL_USER')
    __password = environ.get('MYSQL_PASSWORD')
    __database = environ.get('MYSQL_DATABASE')
    __port = environ.get('MYSQL_PORT')

    @staticmethod
    def create_connection() -> mysql.connector.MySQLConnection:
        '''Creates database connection.

        Takes the class variables as parameters to return a
        successful database connection.
        '''
        connection = mysql.connector.connect(
            host=Database.__host,
            user=Database.__user,
            password=Database.__password,
            database=Database.__database,
            port=Database.__port
            )
        cursor = connection.cursor(prepared=True)

        return connection, cursor
