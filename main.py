import psycopg2
import matplotlib.pyplot as plt



# Створення VIEWs
query_1 = '''
CREATE OR REPLACE VIEW artist_song_count AS
SELECT artist.pseudonym, COUNT(song.song_id) AS song_count
FROM artist
LEFT JOIN artist_song ON artist.artist_id = artist_song.artist_id
LEFT JOIN song ON artist_song.song_id = song.song_id
GROUP BY artist.pseudonym;
'''

query_2 = '''
CREATE OR REPLACE VIEW artist_album_count AS
SELECT artist.pseudonym AS artist_name, COUNT(album.album_id) AS album_count
FROM artist
LEFT JOIN album ON artist.artist_id = album.artist_id
GROUP BY artist.pseudonym;
'''

query_3 = '''
CREATE OR REPLACE VIEW yearly_song_count AS
SELECT EXTRACT(YEAR FROM song.date) AS year, COUNT(*) AS song_count
FROM song
GROUP BY EXTRACT(YEAR FROM song.date)
ORDER BY year;
'''

conn = psycopg2.connect(
    dbname='db_lab3',
    user='Anton_Skakun',
    password='my_pass',
    host='localhost',
    port = '5432'
)

with conn:
    cur = conn.cursor()
    cur.execute('DROP VIEW IF EXISTS artist_song_count')
    cur.execute(query_1)
    cur.execute('SELECT * FROM artist_song_count')
    pseudonyms = []
    songs = []

    for row in cur:
        pseudonyms.append(row[0])
        songs.append(row[1])

    x_range = range(len(pseudonyms))

    figure, (bar_ax, pie_ax, graph_ax) = plt.subplots(1, 3)
    bar = bar_ax.bar(x_range, songs)
    bar_ax.bar_label(bar, label_type='center')
    bar_ax.set_xticks(x_range)
    bar_ax.set_xticklabels(pseudonyms, rotation=45, ha='right')
    bar_ax.set_xlabel('Псевдоними')
    bar_ax.set_ylabel('Кількість пісень')
    bar_ax.set_title('Кількість пісень кожного артиста')


    cur.execute('DROP VIEW IF EXISTS artist_album_count')
    cur.execute(query_2)
    cur.execute('SELECT * FROM artist_album_count')
    pseudonyms = []
    albums = []

    for row in cur:
        pseudonyms.append(row[0])
        albums.append(row[1])

    x_range = range(len(pseudonyms))
    pie_ax.pie(albums, labels=pseudonyms, autopct='%1.1f%%')
    pie_ax.set_title('Кількість альбомів кожного артиста')


    cur.execute('DROP VIEW IF EXISTS yearly_song_count')
    cur.execute(query_3)
    cur.execute('SELECT * FROM yearly_song_count')
    years = []
    songs = []

    for row in cur:
        years.append(row[0])
        songs.append(row[1])

    mark_color = 'blue'
    graph_ax.plot(years, songs, color=mark_color, marker='o')

    for qnt, price in zip(years, songs):
        graph_ax.annotate(price, xy=(qnt, price), color=mark_color,
                          xytext=(7, 2), textcoords='offset points')

    graph_ax.set_xlabel('Рік')
    graph_ax.set_ylabel('Кількість пісень')
    graph_ax.set_xticklabels(years, rotation=45, ha="right")
    graph_ax.plot(years, songs, color='blue', marker='o')
    graph_ax.set_title('Кількість пісень в році')


mng = plt.get_current_fig_manager()
mng.resize(1500, 800)


plt.show()
