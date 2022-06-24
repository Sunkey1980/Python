import psycopg2
from psycopg2 import Error

postgrees_password = input('Ввести пароль доступа Potgres ')


def create_db(db_name):
    try:
        conn = psycopg2.connect(user="postgres", password=postgrees_password)
        conn.autocommit = True
        cursor = conn.cursor()
        sql_create_database = f'CREATE DATABASE {db_name}'
        cursor.execute(sql_create_database)
    except (Exception, Error) as error:
        print(error)
    else:
        print(f'Создана база данных {db_name}')
    finally:
        if conn:
            cursor.close()
            conn.close()


def create_tbl():
    with psycopg2.connect(database="clients_db", user="postgres", password=postgrees_password) as conn:
        conn.autocommit = True
        cursor = conn.cursor()
        sql_create_table_client = 'CREATE TABLE client(id_client SERIAL PRIMARY KEY, first_name VARCHAR(30),' \
                                  'last_name VARCHAR(30), email VARCHAR(30))'
        sql_create_table_phone = 'CREATE TABLE phone(id_phone SERIAL PRIMARY KEY, id_client INTEGER, phone VARCHAR(11), FOREIGN KEY (id_client) REFERENCES client (id_client) ON DELETE CASCADE)'
        try:
            cursor.execute(sql_create_table_client)
            cursor.execute(sql_create_table_phone)
        except (Exception, Error) as error:
            print(error)
        else:
            print('Отношения созданы')


def add_client(first_name, last_name, email):
    sql_add_client = f'INSERT INTO client (first_name, last_name, email) VALUES ({first_name}, {last_name}, {email})'
    cursor.execute(sql_add_client)


def add_phone(conn, add_client_id, phone_number):
    sql_insert_phone = f'INSERT INTO phone(client_id, phone) VALUES({add_client_id}, {phone_number})'
    cursor.execute(sql_insert_phone)


def change_client(conn, client_id, new_first_name=None, new_last_name=None, new_email=None):
    sql_change_client = f'UPDATE client SET first_name = {new_first_name} , last_name = {new_last_name},\
                        email = {new_email} WHERE id_client = {client_id})'
    cursor.execute(sql_change_client)


def delete_phone(conn, client_id):
    sql_delete_phone = f'DELETE FROM phone WHERE id_client = {client_id})'
    cursor.execute(sql_delete_phone)


def delete_client(conn, client_id):
    sql_delete_client = f'DELETE FROM client WHERE id_client = {client_id})'
    cursor.execute(sql_delete_client)


def find_client(conn, first_name=None, last_name=None, email=None, phone=None):
    sql_find_client = f'SELECT * FROM client WHERE first_name = {first_name} OR last_name = {last_name} OR' \
                      f'email = {email} OR id_client = (SELECT id_client FROM phone WHERE phone ={phone} )'
    cursor.execute(sql_find_client)


create_db('clients_db')
create_tbl()

with psycopg2.connect(database="clients_db", user="postgres", password=postgrees_password) as conn:
    cursor = conn.cursor()
    add_client('Мицук', 'Александр', 'sunkey@inbox.ru')

