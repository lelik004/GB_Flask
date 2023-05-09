from flask import Blueprint, render_template

index_app = Blueprint('index_app', __name__, url_prefix='/', static_folder='../static')


@index_app.route('/',  endpoint='index')
def index_page():
    return render_template('index.html')
