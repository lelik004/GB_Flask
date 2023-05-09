
from blog.extension import db, login_manager
# from blog.extension import db
from blog.models.users import User
from blog.views.articles import articles_app
from flask import Flask
from blog.views.users import users_app
from blog.views.auth import auth
from blog.views.index import index_app

CONFIG_PATH = 'blog.config'


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(CONFIG_PATH)
    register_extension(app)
    register_blueprints(app)
    return app


def register_extension(app):
    db.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


def register_blueprints(app: Flask):
    app.register_blueprint(users_app)
    app.register_blueprint(articles_app)
    app.register_blueprint(auth)
    app.register_blueprint(index_app)

