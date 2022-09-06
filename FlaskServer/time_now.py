import sqlite3
from datetime import datetime

conn = sqlite3.connect('orders.db')
cur = conn.cursor() #conn = sqlite3.connect(:memory:) в памяти
cur.execute("""CREATE TABLE IF NOT EXISTS data(
   id INT PRIMARY KEY,
   time TEXT;
""")
conn.commit()

def time():
    time_now = datetime.now()
    current = time_now.strftime("%H:%M:%S")
    print(current)  # Запланировать выполнение этой же функции через 100 миллисекунд
    cur.execute("""INSERT INTO data(id, time) 
       VALUES('00001', current);""")
    conn.commit()
