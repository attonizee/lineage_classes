from flask import Blueprint
from .model import L2_classes, Archers, Warriors, Mages, Assassins
from flask import render_template



bp = Blueprint('routes', __name__, url_prefix='/')

@bp.route('/index')
@bp.route('/')
def index():
    return render_template('index.html', template_l2_classes = L2_classes.query.all())


@bp.route('/Archers')
def archers():
    return render_template('classes.html', template_class_name = 'Archers', template_class = Archers.query.all())

@bp.route('/Warriors')
def warriors():
    return render_template('classes.html', template_class_name = 'Warriors', template_class = Warriors.query.all())

@bp.route('/Mages')
def mages():
    return render_template('classes.html', template_class_name = 'Mages', template_class = Mages.query.all())

@bp.route('/Assassins')
def assassins():
    return render_template('classes.html', template_class_name = 'Assassins', template_class = Assassins.query.all())