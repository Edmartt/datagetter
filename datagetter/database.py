from os import environ
import mysql.connector


class Database():

    @staticmethod
    def create_connection() -> mysql.connector.MySQLConnection:
        connection = mysql.connector.connect(
            host=environ.get('MYSQL_HOST'),
            user=environ.get('MYSQL_USER'),
            password=environ.get('MYSQL_PASSWORD'),
            database=environ.get('MYSQL_DATABASE'),
            port=environ.get('MYSQL_PORT')
            )
        cursor = connection.cursor(prepared=True)

        return connection, cursor
