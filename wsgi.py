from blog.app import create_app, db
from werkzeug.security import generate_password_hash


app = create_app()


@app.cli.command("init-db", help="create all db")
def init_db():
    db.create_all()


@app.cli.command("create-user", help="create user")
def create_user():
    from blog.models.users import User
    is_staff = False
    for i in range(8):
        if i % 2 == 0:
            is_staff = True
        db.session.add(
            User(username=f'user{i}',
                 email=f'name{i}@email.com',
                 password=generate_password_hash(f'user{i}'),
                 is_staff=is_staff)
        )
        db.session.commit()
        is_staff = False

