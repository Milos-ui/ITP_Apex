from flask import Flask, send_file
from flask import render_template
from flask import request
from markupsafe import escape
import json
app = Flask(__name__)
daten = {}

@app.post('/trainingsplan')
def trainingsplan_post():
    if(request.form.get('sportDrop') == None or request.form.get('timeInvest') == None or request.form.get('goal') == None or request.form.get('weight') == None
    or request.form.get('height') == None or request.form.get('age') == None or request.form.get('gender') == None or request.form.get('fitLevel') == None):
        print('Error: Nicht alle Felder ausgefüllt')
        return render_template('indexTest.html', error='Nicht alle Felder ausgefüllt')

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

    return send_file(filepath, as_attachment=True)


@app.get('/trainingsplan')
def trainingsplan_get():
    return json.dump(daten)
