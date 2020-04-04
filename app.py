from flask import Flask, render_template, request


app = Flask(__name__)
@app.route("/")
def index():
    note_file = open("notes.txt", "r", encoding="utf-8")
    lst_note = [line for line in note_file]
    note_file.close()
    return render_template("index.html", lst_note = lst_note)

@app.route("/hello/<string:user_name>")
def hello(user_name):
    user_name = user_name.capitalize()
    return render_template("hello.html", user_name = user_name)

@app.route("/add-note-form")
def add_note_form():
    return render_template("add_note_form.html")

@app.route("/add_note", methods=["POST"])
def add_note():
    data = request.form["dt"]
    print(data)
    note = request.form["new_note"]
    print(note)
    notes_file = open("notes.txt", "a+", encoding="utf-8")
    notes_file.write(str(data) + " " + str(note) + "\n")
    notes_file.close()
    return render_template("susses.html")

@app.route("/table")
def table():
    notes_file = open("notes.txt", "r", encoding="utf-8")
    rows = [[row[:10], row[10:].strip()] for row in notes_file]
    notes_file.close()
    return render_template("table.html", rows=rows)