CREATE TABLE SuperUser (
  login    VARCHAR2(30 CHAR) PRIMARY KEY,
  password VARCHAR2(30 CHAR) NOT NULL,
  name     VARCHAR2(30 CHAR) NOT NULL,
  email    VARCHAR2(30 CHAR) UNIQUE
);

CREATE TABLE Song (
  id       NUMBER,
  name     VARCHAR2(30 CHAR) NOT NULL,
  duration BINARY_DOUBLE     NOT NULL,
  band     VARCHAR2(30 CHAR)
);

CREATE TABLE Band (
  name_of_band VARCHAR2(30 CHAR) NOT NULL,
  music_label  VARCHAR2(30 CHAR)
);

CREATE TABLE Playlist (
  songID  NUMBER NOT NULL,
  loginSU VARCHAR2(30 CHAR)
);


ALTER TABLE Song
  ADD CONSTRAINT song_pk PRIMARY KEY (id);
CREATE SEQUENCE song_seq
  START WITH 1;
CREATE OR REPLACE TRIGGER song_tr
  BEFORE INSERT
  ON Song
  FOR EACH ROW
  BEGIN
    SELECT song_seq.nextval
    INTO :NEW.id
    FROM dual;
  end;
/

ALTER TABLE Band
  ADD CONSTRAINT band_pk PRIMARY KEY (name_of_band);
ALTER TABLE Song
  ADD CONSTRAINT song_band_fk FOREIGN KEY (band) REFERENCES Band (name_of_band);

ALTER TABLE Playlist
  ADD CONSTRAINT playlist_pk PRIMARY KEY (songID, loginSU);

ALTER TABLE Playlist
  ADD CONSTRAINT playlist_song_fk FOREIGN KEY (songID) REFERENCES Song (id) ON DELETE CASCADE;
ALTER TABLE Playlist
  drop constraint playlist_song_fk;
ALTER TABLE Playlist
  ADD CONSTRAINT playlist_user_fk FOREIGN KEY (loginSU) REFERENCES SuperUser (login);

ALTER TABLE Song
  ADD CONSTRAINT duration_length CHECK (duration > 0);
ALTER TABLE SuperUser
  ADD CONSTRAINT pass_len CHECK (length(password) > 4);