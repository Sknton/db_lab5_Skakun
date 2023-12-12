import csv
import psycopg2

conn = psycopg2.connect(
    dbname='db_lab3',
    user='Anton_Skakun',
    password='my_pass',
    host='localhost',
    port = '5432'
)

tables = ['artist', 'album', 'song', 'artist_song']

cursor = conn.cursor()

for table in tables:
    cursor.execute(f'SELECT * FROM {table}')
    data = cursor.fetchall()


    with open(f'{table}.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)


conn.close()