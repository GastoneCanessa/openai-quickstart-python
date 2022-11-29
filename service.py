import sqlite3
from sqlite3 import Error
from query import *


def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

connection = create_connection("C:\\Users\\Utente\\Desktop\\openai_esercitazione\\openai-quickstart-python\\sqlite_db")
execute_query(connection, str(create_generations_table))

def execute_query(connection, query):
    connection = create_connection("C:\\Users\\Utente\\Desktop\\openai_esercitazione\\openai-quickstart-python\\sqlite_db")
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def execute_read_query(connection, query):
    connection = create_connection("C:\\Users\\Utente\\Desktop\\openai_esercitazione\\openai-quickstart-python\\sqlite_db")
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


def insert_generation( create_generations):
    connection = create_connection("C:\\Users\\Utente\\Desktop\\openai_esercitazione\\openai-quickstart-python\\sqlite_db")
    execute_query(connection, str(create_generations))


def get_generations():
    connection = create_connection("C:\\Users\\Utente\\Desktop\\openai_esercitazione\\openai-quickstart-python\\sqlite_db")
    select_users = "SELECT * from generations "
    users = execute_read_query(connection, select_users)

    for user in users:
        print(user)

















#
