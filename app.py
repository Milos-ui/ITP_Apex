from flask import Flask, send_file
from flask import render_template
from flask import request
from markupsafe import escape
import json
app = Flask(__name__)
daten = {}

@app.post('/trainingsplan')
def trainingsplan_post():
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
    
    filepath = 'daten/Trainingsplan.pdf'
    return send_file(filepath, as_attachment=True)


@app.get('/trainingsplan')
def trainingsplan_get():
    return json.dump(daten)
