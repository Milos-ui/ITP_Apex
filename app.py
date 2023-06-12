from flask import Flask, jsonify, send_file
from flask import render_template
from flask import request
from flask import redirect, url_for
from markupsafe import escape
import json


import bcrypt
import mysql.connector

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
    return jsonify(daten)




# MySQL Verbindung herstellen
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin',
    database='Login'
)

@app.route('/', methods=['GET', 'POST'])
def login_or_register():
    error_message = None
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'login':
            # Logik für den Login-Prozess
            # Daten aus dem Formular abrufen
            username = request.form['username']
            password = request.form['password']

            # Daten aus der Datenbank abrufen
            cursor = db.cursor()
            cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
            user = cursor.fetchall()
            cursor.close()

            if user:
                stored_password = user[0][2]  # Gespeichertes bcrypt-verschlüsseltes Passwort aus der Datenbank
                entered_password = password.encode('utf-8')  # Eingegebenes Klartext-Passwort als bytes

                if bcrypt.hashpw(entered_password, bytes(stored_password)) == stored_password:
                    # Passwörter stimmen überein, erfolgreicher Login
                    return render_template('trainingsplan.html')
                else:
                    error_message = 'Benutzername oder Passwort ist falsch'
                    return render_template('login.html', error=error_message)
            else:
                error_message = 'Benutzername oder Passwort ist falsch'
                return render_template('login.html', error=error_message)
        elif action == 'registrieren':
            # Daten aus dem Formular abrufen
            username = request.form['username']
            password = request.form['password']

            salt = bcrypt.gensalt()
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bytes(salt))

            # Daten in der Datenbank speichern
            query = "INSERT INTO users (username, password) VALUES (%s, %s)"
            values = (username, hashed_password)

            # Datenbankabfrage ausführen
            cursor = db.cursor()
            cursor.execute(query, values)
            db.commit()
            cursor.close()

    
    # HTML-Formular anzeigen und Fehlermeldung übergeben
    return render_template('login.html', error=error_message)

@app.route('/login')
def render_login():
    return render_template('login.html')

@app.route('/download_pdf')
def download_pdf():
    dropBox = request.form['sportDrop']
    filepath = ''
    print(dropBox)
    if(dropBox == 'Kraftsport'):
        filepath = '../daten/Kraftsport.pdf'
    elif(dropBox == 'HIIT'):
        filepath = '../daten/HIIT.pdf'
    elif(dropBox == 'Kraftausdauer'):
        filepath = '../daten/Kraftausdauer.pdf'
    elif(dropBox == 'Anderes'):
        filepath = '../daten/Trainingsplan1.pdf'
    else:
        print('Error: Sportart nicht angegeben')
        return 'Error: Sportart nicht angegeben'
    return send_file(filepath, as_attachment=True)
