import json
import psycopg2
from datetime import date

conn = psycopg2.connect(
    dbname='db_lab3',
    user='Anton_Skakun',
    password='my_pass',
    host='localhost',
    port = '5432'
)

tables = ['artist', 'album', 'song', 'artist_song']

cursor = conn.cursor()

data = {}

for table in tables:
    cursor.execute(f'SELECT * FROM {table}')
    rows = cursor.fetchall()
    data[table] = rows


def json_serial(obj):
    if isinstance(obj, date):
        return obj.isoformat()
    raise TypeError ("Type not serializable")


with open('data.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4, default=json_serial)


conn.close()