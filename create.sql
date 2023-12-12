DROP TABLE IF EXISTS artist CASCADE;
DROP TABLE IF EXISTS album CASCADE;
DROP TABLE IF EXISTS song CASCADE;
DROP TABLE IF EXISTS artist_song CASCADE;

CREATE TABLE artist
(
  pseudonym VARCHAR(50) NOT NULL,
  artist_id INT NOT NULL,
  PRIMARY KEY (artist_id)
);



CREATE TABLE album
(
  name VARCHAR(200) NOT NULL,
  album_id INT NOT NULL,
  date DATE NOT NULL,
  artist_id INT NOT NULL,
  PRIMARY KEY (album_id),
  FOREIGN KEY (artist_id) REFERENCES artist(artist_id)
);



CREATE TABLE song
(
  song_id INT NOT NULL,
  name VARCHAR(200) NOT NULL,
  date DATE NOT NULL,
  album_id INT NOT NULL,
  PRIMARY KEY (song_id),
  FOREIGN KEY (album_id) REFERENCES album(album_id)
);



CREATE TABLE artist_song
(
  artist_id INT NOT NULL,
  song_id INT NOT NULL,
  PRIMARY KEY (artist_id, song_id),
  FOREIGN KEY (artist_id) REFERENCES artist(artist_id),
  FOREIGN KEY (song_id) REFERENCES song(song_id)
);
