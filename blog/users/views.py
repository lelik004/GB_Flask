from werkzeug.exceptions import NotFound
from flask import Blueprint, render_template

users_app = Blueprint('users_app', __name__, url_prefix='/users', static_folder='../static')
USERS = {
    1: 'Ivan',
    2: 'Oleg',
    3: 'Anna',
}


@users_app.route('/', endpoint='list')
def users_list():
    return render_template('users/list.html', users=USERS)


@users_app.route('/<int:user_id>/', endpoint='details')
def user_details(user_id: int):
    try:
        user_name = USERS[user_id]
    except KeyError:
        raise NotFound(f'Пользователь с ID {user_id} не существует')
    return render_template('users/details.html', user_id=user_id, user_name=user_name)
