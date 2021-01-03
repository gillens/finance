import sqlite3

def create_db(conn):
    c = conn.cursor()
    c.execute('''CREATE TABLE stocks
                (date text, trans text, symbol text, qty real, price real)''')

    c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
    conn.commit()

def get_db_info(conn):
    c = conn.cursor()
    t = ('RHAT',)
    c.execute('SELECT * FROM stocks WHERE symbol=?', t)
    print(c.fetchone())

conn = sqlite3.connect('example.db')
# create_db(conn)
get_db_info(conn)

conn.close()