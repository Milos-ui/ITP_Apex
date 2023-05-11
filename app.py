from flask import Flask, send_file
from flask import render_template
from flask import request
from markupsafe import escape
app = Flask(__name__)
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form['username']
        benutzer = {
            'Alter': request.form['alter'],
            'Geschlecht': request.form['geschlecht']
        }
        return f'Hello {escape (username)}!'
    else:
        return render_template('login.html')
    
@app.route("/Trainingsplan", methods=["GET", "POST", "DOWNLOAD"])
def Trainingsplan():
     if request.method == "DOWNLOAD":
        filepath = 'daten/Trainingsplan.pdf'
        return send_file(filepath, as_attachment=True)