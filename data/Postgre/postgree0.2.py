from psycopg2 import OperationalError
import psycopg2


db_name = 'postgre'
db_user = 'user'
db_password = 'password'
db_host = '127.0.0.1'
db_port = '5432'

def create_connection():
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection

connection = create_connection()    #создание базы данных Postgree

def create_database(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executed successfully")
    except OperationalError as e:
        print(f"The error '{e}' occurred")

create_database_query = "CREATE DATABASE sm_app"
create_database(connection, create_database_query)

#create_connection("sm_app", "user", "password", "127.0.0.1", "5432")