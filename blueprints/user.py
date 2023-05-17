from flask import Blueprint, render_template, request, current_app, redirect, url_for, flash, session
from exts import mail, cache, db
import string
import random
from utils import restful
from forms.user import RegisterForm, LoginForm
from models.user import UserModel
from werkzeug.security import check_password_hash

bp = Blueprint("user", __name__, url_prefix="/user")

@bp.route('/')
def index():
    return redirect(url_for("user.register"))

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template("front/register.html")
    else:
        form = RegisterForm(request.form)
        if form.validate():
            email = form.email.data
            username = form.username.data
            password = form.password.data
            # 添加至数据库
            user = UserModel(username=username, password=password, email=email)
            db.session.add(user)
            db.session.commit()

            return redirect(url_for("user.login"))
        else:
            for message in form.messages:
                flash(message)
            return redirect(url_for("user.register"))

@bp.route('/mail/captcha')
def mail_captcha():
    try:
        email = request.args.get("email")
        # 生成验证码
        digits = string.digits * 4
        sample = random.sample(digits, 4)
        captcha = "".join(sample)
        # 发送验证码
        current_app.celery.send_task("send_mail", ("验证码", email, captcha))
        #
        cache.set(email, captcha, timeout=100)

        return restful.ok(message="验证码发送成功")
    except Exception as e:
        print(e)

        return restful.server_error()

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('front/login.html')
    else:
        form = LoginForm(request.form)
        email = form.email.data
        password = form.password.data
        remember = form.remember.data
        if form.validate():
            # 判断邮箱是否注册过
            user = UserModel.query.filter_by(email=email).first()
            if not user:
                flash(message="邮箱未注册")
                return redirect(url_for("user.register"))
            else:
                # 判断密码是否正确
                if check_password_hash(user.password, password):
                    # 判断用户是否被禁用
                    if not user.is_active:
                        flash(message="该账号已禁用")
                        return redirect(url_for("user.login"))

                    # 登录成功
                    session["user_id"] = user.id
                    # 延长cookie时间
                    if remember:
                        session.permanent = True

                    return redirect("/")
                else:
                    flash(message="密码错误，请重新输入")
                    return redirect(url_for("user.login"))
        else:
            messages = form.messages
            for message in messages:
                flash(message)
            return redirect(url_for("user.login"))



