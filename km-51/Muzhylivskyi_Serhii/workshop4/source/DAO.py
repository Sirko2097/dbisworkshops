import cx_Oracle


class Song:
    def __enter__(self):
        self.__db = cx_Oracle.connect("Sirko", "S5116951169", "XE")
        self.__cursor = self.__db.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__cursor.close()
        self.__db.close()

    def add_song(self, song_name, song_duration, song_band):
        self.__cursor.callproc("SONG_PACKAGE.ADD_SONG", [song_name, song_duration, song_band])

    def get_song(self, song_number):
        query = 'select * from table ( SONG_PACKAGE.GET_SONG(:song_number) )'
        var = self.__cursor.execute(query, song_number=song_number)
        return var.fetchall()

    def get_songs(self):
        query = 'select * from table (SONG_PACKAGE.GET_SONGS())'
        var = self.__cursor.execute(query)
        return var.fetchall()

    def get_band_song(self, band):
        query = 'select * from table ( SONG_PACKAGE.GET_BAND_SONG(:band_name) )'
        var = self.__cursor.execute(query, band_name=band)
        return var.fetchall()


class Play_List:
    def __enter__(self):
        self.__db = cx_Oracle.connect("Sirko", "S5116951169", "XE")
        self.__cursor = self.__db.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__cursor.close()
        self.__db.close()

    def add_song_to_play_list(self, song_number, user_login):
        self.__cursor.callproc("PLAY_LIST_PACKAGE.ADD_SONG", [song_number, user_login])

    def get_songs_from_play_list(self):
        query = 'select * from table (PLAY_LIST_PACKAGE.GET_PLAY_LIST())'
        var = self.__cursor.execute(query)
        return var.fetchall()


class Band:
    def __enter__(self):
        self.__db = cx_Oracle.connect("Sirko", "S5116951169", "XE")
        self.__cursor = self.__db.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__cursor.close()
        self.__db.close()

    def add_band(self, band_name, music_label):
        self.__cursor.callproc("BAND_PACKAGE.ADD_BAND", [band_name, music_label])

    def get_bands(self):
        self.__cursor.callfunc("BAND_PACKAGE.GET_BANDS")

    def get_band(self, name):
        query = 'select * from table ( BAND_PACKAGE.GET_BAND(:band_name) )'
        var = self.__cursor.execute(query, band_name=name)
        return var.fetchall()


class User:
    def __enter__(self):
        self.__db = cx_Oracle.connect("Sirko", "S5116951169", "XE")
        self.__cursor = self.__db.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__cursor.close()
        self.__db.close()

    def sign_in(self, login, password):
        result = self.__cursor.callfunc("USER_PACKAGE.LOG_IN", cx_Oracle.NUMBER, [login, password])
        return result

    def sign_up(self, logIn, password, name, email):
        self.__cursor.callproc("USER_PACKAGE.REGISTRATION", [logIn, password, name, email])


# temp = Song()
# temp.__enter__()
# temp.add_song("Bother", 5.10, "Corey Taylor")
# temp = Song()
# temp.__enter__()
# print(temp.get_songs())
# temp = Band()
# temp.__enter__()
# temp.add_band("Any Given Day", "dd")
# temp = User()
# temp.__enter__()
# print(temp.sign_in("Gray", "1"))
# temp = Play_List()
# temp.__enter__()
# temp.add_song_to_play_list(28, "Gray")
# print(temp.get_songs_from_play_list())
