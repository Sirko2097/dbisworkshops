import datetime

import cx_Oracle
from flask import Flask, render_template, request, redirect, url_for, make_response, session

from DAO import User, Song, Play_List, Band
from wtf.forms.bandController import BandController
from wtf.forms.deleteSong import SongsDeleter
from wtf.forms.songController import SongsController
from wtf.forms.songsInPlayListController import SongsInPlayListController
from wtf.forms.inputBandNameForSearching import BandReader
from wtf.forms.login import LoginForm
from wtf.forms.registration import RegForm
from wtf.forms.updateUser import UpdateUser

app = Flask(__name__)
app.secret_key = "dev key"
username = "Sirko"
password = "S5116951169"
url = "XE"
connection = cx_Oracle.connect(username, password, url)

band_dictionary = {
    "band_name": "Slipknot",
    "music_label": "Roadrunner Records"
}
song_dictionary = {
    "song_name": "All Out Life",
    "duration": "5.11",
    "band": "Slipknot"
}
available_dictionary = dict.fromkeys(['song', 'band', 'all'], "dictionary_name")


@app.route('/radio/<action>', methods=['GET'])
def doGet(action):
    if action == "allSongs":
        songs = Song().__enter__().get_songs()
        table_body = ""
        for song in songs:
            table_body += """ 
                <tr>
                    <td>""" + song[1] + """</td>
                    <td>""" + str(song[2]) + """</td>
                    <td>""" + song[3] + """</td>
                    <td>""" + song[4] + """</td>
                </tr>
                                """
        return render_template('allSongs.html', table_body=table_body)

    else:
        return render_template("error.html", action_value=action, available=available_dictionary)


@app.route('/radio/addsong', methods=['GET', 'POST'])
def addSong():
    form = SongsController()

    if request.method == 'GET':
        return render_template("addSong.html", myForm=form)
    else:
        status = Song().__enter__().add_song(request.form['name'], request.form['duration'],
                                             request.form['band'], request.form['genre'])
        if status == '200 OK':
            return redirect('/radio/allSongs')
        elif status == '500 already existed':
            return render_template("allSongs.html")
        else:
            return redirect(url_for('addBand'))


@app.route('/radio/deletesong', methods=['GET', 'POST'])
def deleteSong():
    form = SongsDeleter()

    if request.method == 'GET':
        return render_template('deleteSong.html', myForm=form)
    else:
        # song_cur = Song().__enter__()
        # if (request.form['ID'] is None) and (request.form['name'] is not None):
        #     status = song_cur.delete_song(None, f)
        status = Song().__enter__().delete_song(request.form['ID'], request.form['name'], request.form['band'])

        if status == '200 OK':
            return redirect('/radio/allSongs')
        else:
            return render_template('error.html')


@app.route('/radio/getsongsbyband', methods=['GET', 'POST'])
def getSongByBand():
    form = BandReader()

    if request.method == 'GET':
        return render_template("inputBandNameForSongsSearching.html", myForm=form)
    elif request.method == 'POST':
        songs = Song().__enter__().get_band_song(request.form['name'])
        table_body = ""
        for song in songs:
            table_body += """ 
                       <tr>
                           <td>""" + song[1] + """</td>
                           <td>""" + str(song[2]) + """</td>
                           <td>""" + song[3] + """</td>
                           <td>""" + song[4] + """</td>
                       </tr>
                                       """
        return render_template('songsByBand.html', table_body=table_body)


@app.route('/radio/getmetalsongs', methods=['GET'])
def getMetalSongs():
    songs = Song().__enter__().get_songs_by_genre('Metal')
    table_body = ""
    for song in songs:
        table_body += """ 
                    <tr>
                        <td>""" + song[1] + """</td>
                        <td>""" + str(song[2]) + """</td>
                        <td>""" + song[3] + """</td>
                        <td>""" + song[4] + """</td>
                    </tr>
                                    """
    return render_template('allSongs.html', table_body=table_body)


@app.route('/radio/getrocksongs', methods=['GET'])
def getRockSongs():
    songs = Song().__enter__().get_songs_by_genre("Rock")
    table_body = ""
    for song in songs:
        table_body += """ 
                    <tr>
                        <td>""" + song[1] + """</td>
                        <td>""" + str(song[2]) + """</td>
                        <td>""" + song[3] + """</td>
                        <td>""" + song[4] + """</td>
                    </tr>
                                    """

    songs = Song().__enter__().get_songs_by_genre("Metal")
    for song in songs:
        table_body += """ 
                            <tr>
                                <td>""" + song[1] + """</td>
                                <td>""" + str(song[2]) + """</td>
                                <td>""" + song[3] + """</td>
                                <td>""" + song[4] + """</td>
                            </tr>
                                            """

    return render_template('allSongs.html', table_body=table_body)


@app.route('/radio/getpopsongs', methods=['GET'])
def getPopSongs():
    songs = Song().__enter__().get_songs_by_genre('Pop')
    table_body = ""
    for song in songs:
        table_body += """ 
                        <tr>
                            <td>""" + song[1] + """</td>
                            <td>""" + str(song[2]) + """</td>
                            <td>""" + song[3] + """</td>
                            <td>""" + song[4] + """</td>
                        </tr>
                                        """
    return render_template('allSongs.html', table_body=table_body)


@app.route('/radio/getrapsongs')
def getRapSongs():
    songs = Song().__enter__().get_songs_by_genre('Rap')
    table_body = ""
    for song in songs:
        table_body += """ 
                        <tr>
                            <td>""" + song[1] + """</td>
                            <td>""" + str(song[2]) + """</td>
                            <td>""" + song[3] + """</td>
                            <td>""" + song[4] + """</td>
                        </tr>
                                        """
    return render_template('allSongs.html', table_body=table_body)


@app.route('/radio/getallbands')
def getAllBands():
    bands = Band().__enter__().get_bands()
    table_body = ""
    for band in bands:
        table_body += """ 
                    <tr>
                        <td>""" + str(band[0]) + """</td>
                        <td>""" + str(band[1]) + """</td>
                    </tr>
                                    """
    return render_template('allBands.html', table_body=table_body)


@app.route('/radio/addband', methods=['GET', 'POST'])
def addBand():
    form = BandController()

    if request.method == 'GET':
        return render_template("addBand.html", myForm=form)
    else:
        status = Band().__enter__().add_band(request.form['name'], request.form['music_label'])

        if status == '200 OK':
            return redirect('/radio/getallbands')
        else:
            return render_template('error.html')


@app.route('/', methods=['GET', 'POST'])
def index():
    if 'login' not in session:
        login = request.cookies.get("loginCookie")
        if login is None:
            return redirect(url_for('signIn'))
    else:
        return render_template("index.html")


@app.route('/radio/signIn', methods=['POST', 'GET'])
def signIn():
    form = LoginForm()

    if request.method == 'GET':
        if 'login' not in session:
            login = request.cookies.get("loginCookie")
            if login is None:
                return render_template("login.html", myForm=form)
            else:
                response = make_response("by cookie")
                session['login'] = login
                redirect(url_for('index'))
                return response
        else:
            response = make_response("by session")
            return response

    if request.method == 'POST':
        if not form.validate():
            render_template("login.html", myForm=form)
        else:
            user = User()
            user.__enter__()
            var = user.sign_in(request.form['login'], request.form['password'])

            if var == 1:
                session['login'] = request.form["login"]
                response = make_response("logged in")

                expires_data = datetime.datetime.now()
                expires_data = expires_data + datetime.timedelta(minutes=5)
                response.set_cookie("loginCookie", request.form["login"], expires=expires_data)
                return redirect(url_for('index'))
                # return response
            else:
                return redirect(url_for('signUp'))


@app.route('/radio/signOut', methods=['GET', 'POST'])
def signOut():
    session.pop('login', None)
    response = make_response("Log out and no cookie")
    response.set_cookie("loginCookie", '', expires=0)
    return redirect(url_for('index'))
    # return response


@app.route('/radio/signUp', methods=['GET', 'POST'])
def signUp():
    form = RegForm()

    if request.method == 'GET':
        return render_template("registration.html", myForm=form)
    else:
        user = User()
        user.__enter__()
        status = user.sign_up(request.form['login'], request.form['password'], request.form['name'],
                              request.form['email'])

        if status == '200 OK':
            session['login'] = request.form["login"]
            response = make_response("logged in")

            expires_data = datetime.datetime.now()
            expires_data = expires_data + datetime.timedelta(minutes=5)
            response.set_cookie("loginCookie", request.form["login"], expires=expires_data)
            return response
        elif status == '500 already existed':
            return redirect(url_for('signUp'))
        else:
            return redirect(url_for('signUp'))


@app.route('/radio/updateuser', methods=['GET', 'POST'])
def updateUser():
    form = UpdateUser()

    if request.method == 'GET':
        return render_template("updateUser.html", myForm=form)
    else:
        user = User()
        user.__enter__()
        status = user.update_user_info(session['login'], str(request.form['password']), str(request.form['name']),
                                       str(request.form['email']))

        if status == '200 OK':
            return redirect('/')
        else:
            return render_template("error.html")


@app.route('/radio/playlistmenu', methods=['GET'])
def getPlayListMenu():
    return render_template('playlistmenu.html')


@app.route('/radio/playlist', methods=['GET'])
def getPlayList():
    songs = Play_List().__enter__().get_songs_from_play_list(session['login'])
    table_body = ""
    for song in songs:
        table_body += """ 
                           <tr>
                               <td>""" + str(song[0]) + """</td>
                               <td>""" + str(song[1]) + """</td>
                               <td>""" + str(song[2]) + """</td>
                               <td>""" + str(song[3]) + """</td>
                               <td>""" + str(song[4]) + """</td>
                           </tr>
                                           """
    return render_template('userPlayList.html', table_body=table_body)


@app.route('/radio/deletesongfromplaylist', methods=['GET', 'POST'])
def deleteSongFromPlayList():
    form = SongsInPlayListController()

    if request.method == 'GET':
        return render_template("deleteSongFromPlayList.html", myForm=form)
    else:
        status = Play_List().__enter__().delete_song_from_play_list(request.form['name'])
        if status == '200 OK':
            return redirect('/radio/playlist')
        else:
            return render_template("error.html")


@app.route('/radio/addsongtoplaylist', methods=['GET', 'POST'])
def addSongToPlayList():
    form = SongsInPlayListController()

    if request.method == 'GET':
        return render_template("addSongToPlayList.html", myForm=form)
    else:
        status = Play_List().__enter__().add_song_to_play_list(request.form['name'], session['login'])
        if status == '200 OK':
            return redirect('/radio/playlist')
        elif status == '500 already existed':
            return redirect('/radio/playlist')
        else:
            return render_template("error.html")


if __name__ == '__main__':
    app.run(debug=True)
