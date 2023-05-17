# exts.py：这个文件存在的意义就是为了解决循环引用的问题

# flask-sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_caching import Cache
from flask_wtf import CSRFProtect
from flask_avatars import Avatars

db = SQLAlchemy()
mail = Mail()
cache = Cache()
csrf = CSRFProtect()
avatars = Avatars()
