from flask import Flask, send_file
from flask import render_template
from flask import request
from markupsafe import escape
app = Flask(__name__)
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form['username']
        return f'Hello {escape (username)}!'
    else:
        return render_template('login.html')
    
@app.route("/Trainingsplan", methods=["GET", "POST"])
def Trainingsplan():
     filepath = '/Users/johnyhamsik12/Desktop/Entschuldigungen Tomi_freitag.pdf'
     return send_file(filepath, as_attachment=True)