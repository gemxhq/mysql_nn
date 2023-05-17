from celery import Celery
import celeryconfig
from celeryconfig import broker_url
from flask_mail import Message
from exts import mail

# 传入app，创建celery对象
def make_celery(app):
  	# 创建celery对象
    celery = Celery(app.import_name, broker=broker_url)
    #导入配置文件
    celery.config_from_object(celeryconfig)

    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask
    app.celery = celery

    # 添加任务
    celery.task(name="send_mail")(send_mail)

    return celery

# 任务实现的具体功能
def send_mail(subject, recipients, body):
    message = Message(subject, [recipients], body)
    mail.send(message)
    print('正在发送邮件')