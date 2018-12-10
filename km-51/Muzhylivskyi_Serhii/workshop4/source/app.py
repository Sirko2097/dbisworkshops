import datetime

import cx_Oracle
from flask import Flask, render_template, request, redirect, url_for, make_response, session

from DAO import User
from wtf.forms.login import LoginForm
from wtf.forms.registration import RegForm

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
    if action == "song":
        return render_template("song.html", song=song_dictionary)
    elif action == "band":
        return render_template("band.html", band=band_dictionary)
    elif action == "all":
        return render_template("all.html", song=song_dictionary, band=band_dictionary)
    elif action == "allSongs":
        song_cursor = connection.cursor()

        song_cursor.execute("""
                    SELECT name, duration, band FROM SONG
                """)

        table_body = ""
        for name, duration, band in song_cursor:
            table_body += """ 
                    <tr>
                        <td>""" + name + """</td>
                        <td>""" + str(duration) + """</td>
                        <td>""" + band + """</td>
                    </tr>
                    """

        song_cursor.close()

        print(table_body)
        return render_template('allSongs.html', table_body=table_body)

    else:
        return render_template("error.html", action_value=action, available=available_dictionary)


@app.route('/radio', methods=['POST'])
def doPost():
    if request.form["action"] == "song_update":
        song_dictionary["song_name"] = request.form["song_name"]
        song_dictionary["duration"] = request.form["duration"]
        song_dictionary["band"] = request.form["band"]

        return redirect(url_for('doGet', action="all"))

    elif request.form["action"] == "band_update":
        band_dictionary["band_name"] = request.form["band_name"]
        band_dictionary["music_label"] = request.form["label"]

        return redirect(url_for('doGet', action="all"))


@app.route('/', methods=['GET', 'POST'])
def index():
    if 'login' not in session:
        login = request.cookies.get("loginCookie")
        if login is None:
            return redirect(url_for('signIn'))


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
                return response
            else:
                return redirect(url_for('signUp'))


@app.route('/radio/signOut', methods=['GET', 'POST'])
def signOut():
    session.pop('login', None)
    response = make_response("Log out and no cookie")
    response.set_cookie("loginCookie", '', expires=0)
    return response


@app.route('/radio/signUp', methods=['GET', 'POST'])
def signUp():
    form = RegForm()

    if request.method == 'GET':
        return render_template("registration.html", myForm=form)
    else:
        user = User()
        user.__enter__()
        user.sign_up(request.form['login'], request.form['password'], request.form['name'], request.form['email'])

        session['login'] = request.form["login"]
        response = make_response("logged in")

        expires_data = datetime.datetime.now()
        expires_data = expires_data + datetime.timedelta(minutes=5)
        response.set_cookie("loginCookie", request.form["login"], expires=expires_data)
        return response


if __name__ == '__main__':
    app.run(debug=True)
