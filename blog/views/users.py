from werkzeug.exceptions import NotFound
from flask import Blueprint, render_template
from flask_login import login_required

from blog.models.users import User

users_app = Blueprint('users_app', __name__, url_prefix='/users', static_folder='../static')
# USERS = {
#     1: 'Ivan',
#     2: 'Oleg',
#     3: 'Anna',
# }


@users_app.route('/', endpoint='list')
def users_list():
    _users = User.query.all()
    return render_template('users/list.html', users=_users)


@users_app.route('/<int:pk>', endpoint='details')
@login_required
def profile(pk: int):
    from blog.models.users import User

    _user = User.query.filter_by(id=pk).one_or_none()

    if _user is None:
        raise NotFound(f'Пользователь с ID {pk} не существует')

    return render_template('users/details.html', user=_user)
