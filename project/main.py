from flask import Blueprint, render_template
from flask_login import login_required, current_user
from . import db
import datetime
main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

@main.route('/uploads')
@login_required
def uploads():
    now = datetime.datetime.now()
    next_day = now.strftime("%Y-%m-{}".format(now.day+1))
    return render_template('upload.html', name=current_user.name, next_day=next_day)
