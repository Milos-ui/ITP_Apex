from flask import Flask, send_file
from flask import render_template
from flask import request
from markupsafe import escape
app = Flask(__name__)

@app.post('/trainingsplan')
def trainingsplan_post():
    sportDrop = request.form['sportDrop']
    timeInvest = request.form['timeInvest']

    filepath = 'daten/Trainingsplan.pdf'
    return send_file(filepath, as_attachment=True)


@app.get('/trainingsplan')
def trainingsplan_get():
    filepath = 'daten/Trainingsplan.pdf'
    return send_file(filepath, as_attachment=True)