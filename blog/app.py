from flask import Flask, render_template

from blog.articles.views import articles_app
from blog.users.views import users_app


# @app.route('/')
# def index():
#     return render_template('index.html')


def create_app() -> Flask:
    app = Flask(__name__)
    register_blueprints(app)
    return app


def register_blueprints(app: Flask):
    app.register_blueprint(users_app)
    app.register_blueprint(articles_app)










'''
Lesson 1
'''
# from time import time
# from flask import request, g
#
# @app.route('/<string:some_var>')
# def index(some_var: str):
#     return f'Hello, {some_var}'
#
#
# @app.route('/query_string/')
# def query_string():
#     first_var = request.args.get('first')
#     second_var = request.args.get('second')
#     return f'{first_var} and {second_var}'
#
#
# @app.route('/custom_status/', methods=['GET', 'POST'])
# def custom_status_code():
#     if request.method == 'GET':
#         return
#         '''\
#         Чтобы получить ответ с кастомным статусом
#         отправь запрос использую миетод POST и передай "code" в JSON/FormData
#         '''
#
#     print('raw data:', request.data)
#
#     if request.form and 'code' in request.form:
#         return 'code from form', request.form['code']
#
#     if request.json and 'code' in request.json:
#         return 'code from json', request.json['code']
#
#     return "", 204
#
# @app.before_request
# def process_before_request():
#     g.start_time = time()
#
# @app.after_request
# def process_after_request(response):
#     if hasattr(g, 'start_time'):
#         response.headers['process-time'] = time() - g.start_time
#
#     return response
#
# @app.errorhandler(404)
# def handler_404(error):
#     app.logger.error(error)
#     return 'Error 404'
#
