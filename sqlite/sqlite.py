import sqlite3  #   https://pythonru.com/biblioteki/vstavka-dannyh-v-tablicu-sqlite-v-python
import time_now

try:
    sqlite_connection = sqlite3.connect('tdata.db')
    sqlite_create_table_query = '''CREATE TABLE time (
                                id INTEGER PRIMARY KEY,
                                time timestamp);'''

    cursor = sqlite_connection.cursor()
    print("База данных подключена к SQLite")
    cursor.execute(sqlite_create_table_query)
    sqlite_connection.commit()
    print("Таблица SQLite создана")

    cursor.close()

except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)
finally:
    if (sqlite_connection):
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")

try:
    sqlite_connection = sqlite3.connect('tdata.db')
    cursor = sqlite_connection.cursor()
    print("Подключен к SQLite")
    #print(time_now.time())

    sqlite_insert_query = """INSERT INTO time
                          (id, time)
                          VALUES
                          (?, ?);"""
    data_tuple = (1, time_now.time())
    count = cursor.execute(sqlite_insert_query, (1,))
    sqlite_connection.commit()
    print("Запись успешно вставлена таблицу time ", cursor.rowcount)
    cursor.close()

except sqlite3.Error as error:
    print("Ошибка при работе с SQLite", error)
finally:
    if sqlite_connection:
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")