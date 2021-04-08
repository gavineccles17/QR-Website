#db.py
import os
import pymysql
from flask import jsonify

db_user = os.environ.get('CLOUD_SQL_USERNAME')
db_password = os.environ.get('CLOUD_SQL_PASSWORD')
db_name = os.environ.get('CLOUD_SQL_DATABASE_NAME')
db_connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')


def open_connection():
    unix_socket = '/cloudsql/{}'.format(db_connection_name)
    try:
        print("here")
        if os.environ.get('GAE_ENV') == 'standard':
            conn = pymysql.connect(user=db_user, password=db_password,
                                unix_socket=unix_socket, db=db_name,
                                cursorclass=pymysql.cursors.DictCursor
                                )
            print("got here")
    except pymysql.MySQLError as e:
        print(e)

    return conn


def get_customers():
    conn = open_connection()
    with conn.cursor() as cursor:
        customers = cursor.execute('SELECT * FROM customers;').fetchall()
    conn.close()
    return customers

def add_customers(name, email, url_business, url_short):
    conn = open_connection()
    with conn.cursor() as cursor:
        cursor.execute('INSERT INTO customers (name, url_business, url_short, email) VALUES (%s, %s, %s, %s)', (name, url_business, url_short, email))
    conn.commit()
    conn.close()