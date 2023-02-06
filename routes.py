from app import db, app
from model import L2_classes, Archers, Warriors, Mages, Assassins
from flask import render_template

@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html', template_l2_classes = L2_classes.query.all())


@app.route('/Archers')
def archers():
    return render_template('classes.html', template_class_name = 'Archers', template_class = Archers.query.all())

@app.route('/Warriors')
def warriors():
    return render_template('classes.html', template_class_name = 'Warriors', template_class = Warriors.query.all())

@app.route('/Mages')
def mages():
    return render_template('classes.html', template_class_name = 'Mages', template_class = Mages.query.all())

@app.route('/Assassins')
def assassins():
    return render_template('classes.html', template_class_name = 'Assassins', template_class = Assassins.query.all())