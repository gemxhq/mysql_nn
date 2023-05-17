from datetime import timedelta
import os

class BaseConfig:
    SECRET_KEY = "asdfasdfjasdfjasd;lf"
    JSON_AS_ASCII = False
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)
    UPLOAD_IMAGE_PATH = os.path.join(os.path.dirname(__file__), "media")

class DevelopmentConfig(BaseConfig):
    # 数据库的配置信息
    HOSTNAME = '127.0.0.1'
    PORT     = '3306'
    DATABASE = 'flask_env'
    USERNAME = 'root'
    PASSWORD = 'G.E.M0816'
    DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
    SQLALCHEMY_DATABASE_URI = DB_URI


    # 邮箱配置
    MAIL_SERVER = "smtp.qq.com"
    MAIL_USE_SSL = True
    MAIL_PORT = 465
    MAIL_USERNAME = "2826255613@qq.com"
    MAIL_PASSWORD = "acvctrhcfhcodddj"
    MAIL_DEFAULT_SENDER = "2826255613@qq.com"

    # 缓存配置
    CACHE_TYPE = "RedisCache"
    CACHE_REDIS_HOST = "127.0.0.1"
    CACHE_REDIS_PORT = 6379