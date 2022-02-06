# SQL Connect Program

import sqlite3 as sq


def connect_db(dbname):
    conn = sq.connect("Oyo.db")
    conn.execute("CREATE TABLE IF NOT EXISTS OYO_HOTELS (NAME TEXT, ADDRESS TEXT, PRICE INT, RATINGS TEXT, AMENITIES TEXT)")
    print('Table created successfully')
    conn.close()


def insert_into_table(dbname, values):
    conn = sq.connect("Oyo.db")
    print('Inserted into table:', values)
    insert_sql = 'INSERT INTO OYO_HOTELS (NAME, ADDRESS, PRICE, RATINGS, AMENITIES) VALUES (?, ?, ?, ?, ?)'
    conn.execute(insert_sql, values)
    conn.commit()
    conn.close()


def get_hotel_info(dbname):
    conn = sq.connect("Oyo.db")
    cur = conn.cursor()
    cur.execute('SELECT * FROM OYO_HOTELS')
    table_data = cur.fetchall()
    for record in table_data:
        print(record)
    conn.close()
