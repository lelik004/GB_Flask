from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from werkzeug.security import check_password_hash
from blog.models.users import User

auth = Blueprint('auth', __name__, url_prefix="/auth", static_folder="../static")

# @login_manager.user_loader
# def load_user(pk):
#     return User.query.filter_by(id=pk).one_or_none()
#
#
# @login_manager.unauthorized_handler
# def unauthorized():
#     return redirect(url_for('auth.login'))


@auth.route('/login', methods=('GET',))
def login():
    if current_user.is_authenticated:
        return redirect(url_for('users_app.details', pk=current_user.id))

    return render_template(
        'auth/login.html',
    )


@auth.route('/login', methods=('POST',))
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flash('Check your login details')
        return redirect(url_for('.login'))

    login_user(user, force=True)

    return redirect(url_for('index_app.index', pk=user.id))


@auth.route('/logout', endpoint='logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index_app.index'))


@auth.route('/secret')
@login_required
def secret_view():
    return 'Super secret data'


