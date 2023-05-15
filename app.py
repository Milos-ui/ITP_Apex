from flask import Flask, send_file
from flask import render_template
from flask import request
from markupsafe import escape
import json

import mysqlx
app = Flask(__name__)
daten = {}

@app.post('/trainingsplan')
def trainingsplan_post():
    # Überprüfen, ob alle Formulardaten vorhanden sind
    if(request.form.get('sportDrop') == None or request.form.get('timeInvest') == None or request.form.get('goal') == None or request.form.get('weight') == None
    or request.form.get('height') == None or request.form.get('age') == None or request.form.get('gender') == None or request.form.get('fitLevel') == None):
        print('Error: Nicht alle Felder ausgefüllt')
        return 'Error: Nicht alle Felder ausgefüllt'
    
    # Speichern der Formulardaten im "daten" Dictionary
    daten = {
        'sportDrop': request.form['sportDrop'],
        'timeInvest': request.form['timeInvest'],
        'goal': request.form['goal'],
        'weight': request.form['weight'],
        'height': request.form['height'],
        'age': request.form['age'],
        'gender': request.form['gender'],
        'fitLevel': request.form['fitLevel']
    }

    # Festlegen des Dateipfads basierend auf der ausgewählten Sportart
    if(daten['sportDrop'] == 'Laufen'):
        filepath = 'daten/Trainingsplan1.pdf'
    elif(daten['sportDrop'] == 'Radfahren'):
        filepath = 'daten/Trainingsplan2.pdf'
    elif(daten['sportDrop'] == 'Schwimmen'):
        filepath = 'daten/Trainingsplan3.pdf'
    elif(daten['sportDrop'] == 'Kraftsport'):
        filepath = 'daten/Trainingsplan4.pdf'
    else:
        print('Error: Sportart nicht angegeben')
        return 'Error: Sportart nicht angegeben'

    # Datei als Anhang zurückgeben
    return send_file(filepath, as_attachment=True)


@app.get('/trainingsplan')
def trainingsplan_get():
    return json.dump(daten)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'root'  # Benutzername der Datenbank
app.config['MYSQL_PASSWORD'] = 'admin'  # Passwort der Datenbank
app.config['MYSQL_DB'] = 'Login'  # Name der Datenbank
mysql = mysqlx(app)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Daten aus dem Formular abrufen
        username = request.form['username']
        password = request.form['password']

        # Daten in der Datenbank speichern
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        mysql.connection.commit()
        cursor.close()

        # Erfolgsmeldung anzeigen
        return 'Registrierung erfolgreich'

    # HTML-Formular anzeigen
    return render_template('login.html')
