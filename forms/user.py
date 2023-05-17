from wtforms import Form, StringField, ValidationError, BooleanField
from wtforms.validators import Email, EqualTo, Length
from models.user import UserModel
from exts import cache
from .baseform import BaseForm

class RegisterForm(BaseForm):
    email = StringField(validators=[Email(message="请输入正确格式的邮箱!")])
    email_captcha = StringField(validators=[Length(message="验证码格式错误", min=4, max=4)])
    username = StringField(validators=[Length(message="请输入正确长度的用户名2-20长度", min=2, max=20)])
    password = StringField(validators=[Length(message="请输入正确长度的密码", min=6, max=20)])
    confirm_password = StringField(validators=[EqualTo(fieldname="password", message="两次密码不一致")])

    def validate_email(self, field):
        # 查看是否已注册
        email = field.data
        if UserModel.query.filter_by(email=email).first():
            raise ValidationError(message="邮箱已注册")

    def validate_captcha(self, field):
        #
        captcha = field.data
        email = self.email.data
        cache_captcha = cache.get(email)
        if not cache_captcha or captcha != cache_captcha:
            raise ValidationError(message="验证码错误")

class LoginForm(BaseForm):
    email = StringField(validators=[Email(message="邮箱格式错误")])
    password = StringField(validators=[Length(message="请输入正确长度的密码", min=6, max=20)])
    remember = BooleanField()

    # # 判断是否是已注册用户
    # def validate_email(self, field):
    #     email = field.data
    #     user = UserModel.query.filter_by(email=email).first()
    #     if not user:
    #         raise ValidationError(message="邮箱未注册")



