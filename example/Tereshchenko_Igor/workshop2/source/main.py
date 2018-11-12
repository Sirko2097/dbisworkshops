from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

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


@app.route('/api/<action>', methods=['GET'])
def doGet(action):
    if action == "song":
        return render_template("song.html", song=song_dictionary)
    elif action == "band":
        return render_template("band.html", band=band_dictionary)
    elif action == "all":
        return render_template("all.html", song=song_dictionary, band=band_dictionary)
    else:
        return render_template("error.html", action_value=action, available=available_dictionary)


@app.route('/api', methods=['POST'])
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


if __name__ == '__main__':
    app.run()
