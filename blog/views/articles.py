from flask import Blueprint, render_template
from flask_login import login_required
from werkzeug.exceptions import NotFound

articles_app = Blueprint('articles_app', __name__, url_prefix='/articles', static_folder='../static')

ARTICLES = {1: {'title': 'FLASK',
                'body': 'FLASK_body'},
            2: {'title': 'DJANGO',
                'body': 'DJANGO_body'},
            3: {'title': 'PYTHON',
                'body': 'PYTHON_body'},
            4: {'title': 'HTML/CSS',
                'body': 'HTML/CSS_body'}
            }


@articles_app.route('/', endpoint='list')
@login_required
def articles_list():
    return render_template('articles/list.html', articles=ARTICLES)


@articles_app.route('/<int:article_id>/', endpoint='details')
@login_required
def article_detail(article_id: int):
    try:
        article = ARTICLES[article_id]
    except KeyError:
        raise NotFound(f'Статья с ID {article_id} не существует')
    return render_template('articles/details.html', article_id=article_id, article=article)
