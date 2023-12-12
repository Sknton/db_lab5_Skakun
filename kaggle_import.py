import csv
import psycopg2

username = 'Anton_Skakun'
password = 'my_pass'
database = 'db_lab3'
host = 'localhost'
port = '5432'

csv_file = 'spotify_songs.csv'

query_4 = '''
DELETE FROM  artist
'''

query_3 = '''
DELETE FROM album 
'''

query_2 = '''
DELETE FROM song 
'''

query_1 = '''
DELETE FROM artist_song 
'''

data_list = []

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

cursor = conn.cursor()

with open(csv_file, 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    cursor.execute(query_1)
    cursor.execute(query_2)
    cursor.execute(query_3)
    cursor.execute(query_4)
    for row in csv_reader:
        data_list.append(row)


cursor.execute("""
               INSERT INTO artist (pseudonym, artist_id)
               VALUES (%s, %s),
                      (%s, %s),
                      (%s, %s),
                      (%s, %s),
                      (%s, %s)
           """, 
           (data_list[0][2], 1,
           data_list[1][2], 2,
           data_list[17][2], 3,
           data_list[3][2], 4,
           data_list[4][2], 5))

cursor.execute("""
               INSERT INTO album (name, date, artist_id, album_id)
               VALUES (%s, %s, %s, %s),
                      (%s, %s, %s, %s),
                      (%s, %s, %s, %s),
                      (%s, %s, %s, %s),
                      (%s, %s, %s, %s)
           """, 
           (data_list[0][5], data_list[0][6], 1, 1,
           data_list[1][5], data_list[1][6], 2, 2,
           data_list[17][5], data_list[17][6], 3, 3,
           data_list[3][5], data_list[3][6], 4, 4,
           data_list[4][5], data_list[4][6], 5, 5))


cursor.execute("""
               INSERT INTO song (name, date, song_id, album_id)
               VALUES (%s, %s, %s, %s),
                      (%s, %s, %s, %s),
                      (%s, %s, %s, %s),
                      (%s, %s, %s, %s),
                      (%s, %s, %s, %s)
           """, 
           (data_list[0][1], data_list[0][6], 1, 1,
           data_list[1][1], data_list[1][6], 2, 2,
           data_list[17][1], data_list[17][6], 3, 3,
           data_list[3][1], data_list[3][6], 4, 4,
           data_list[4][1], data_list[4][6], 5, 5))


cursor.execute("""
                INSERT INTO artist_song (artist_id, song_id)
                VALUES (%s,%s),
                       (%s,%s),
                       (%s,%s),
                       (%s,%s),
                       (%s,%s)
            """, 
            (1, 1,
            2, 2,
            3, 3,
            4, 4,
            5, 5))


conn.commit()