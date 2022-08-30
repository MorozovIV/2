#   https://proglib.io/p/kak-podruzhit-python-i-bazy-dannyh-sql-podrobnoe-rukovodstvo-2020-02-27
import sqlite3
from sqlite3 import Error

path = "db.sqllite"
def create_connection():
    connection = None
    try:
        connection = sqlite3.connect(path) #connection = create_connection("E:\\sm_app.sqlite")
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection
create_connection() #  создание базы данных slqlite