import click
from flask import Flask
import config
from exts import db, mail, cache, csrf, avatars
from flask_migrate import Migrate
from blueprints.user import bp as user_bp
from blueprints.cms import bp as cms_bp
from blueprints.front import bp as front_bp
from models.user import *
from models.post import *
from commands import create_permission, create_role, create_test_user, create_admin, create_board
from bbs_celery import make_celery
from flask_wtf import CSRFProtect
from hooks import bbs_before_request
from filters import sub10

app = Flask(__name__)

app.config.from_object(config.DevelopmentConfig)

#
db.init_app(app)
mail.init_app(app)
cache.init_app(app)
csrf.init_app(app)
avatars.init_app(app)


migrate = Migrate(app, db)
celery = make_celery(app)
# CSRFProtect(app)

#
app.register_blueprint(user_bp)
app.register_blueprint(cms_bp)
app.register_blueprint(front_bp)


@app.cli.command("my-command")
def my_command():
    click.echo("this is my command")

#
app.cli.command("create-permission")(create_permission)
app.cli.command("create-role")(create_role)
app.cli.command("create-test-user")(create_test_user)
app.cli.command("create-admin")(create_admin)
app.cli.command("create-board")(create_board)

#
app.before_request(bbs_before_request)

# 过滤器
app.template_filter("sub10")(sub10)

if __name__ == '__main__':
    app.run()
