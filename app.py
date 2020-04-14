from flask import Flask, render_template, request
from datetime import datetime


app = Flask(__name__)
@app.route("/")
@app.route("/<string:user_name>")
def index(user_name = ""):
    user_name = user_name.capitalize()
    note_file = open("notes.txt", "r", encoding="utf-8")
    lst_note = [line for line in note_file]
    note_file.close()
    return render_template("index.html", lst_note = lst_note, user_name = user_name)

@app.route("/form", methods=["POST", "GET"])
def form():
    if request.method == "POST":
        data = request.form.get("dt")
        note = request.form.get("new_note")
        notes_file = open("notes.txt", "a+", encoding="utf-8")
        notes_file.write(str(data) + " " + str(note) + "\n")
        notes_file.close()
        return render_template("susses.html")

    notes_file = open("notes.txt", "r", encoding="utf-8")
    rows = [[datetime.strptime(row[:10], "%Y-%m-%d"), row[10:].strip()] for row in notes_file]
    notes_file.close()
    return render_template("form.html", rows=rows)