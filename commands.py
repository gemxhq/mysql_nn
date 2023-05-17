import click

from exts import db
from models.user import RoleModel, PermissionModel, Permission, UserModel
from models.post import BoardModel

def create_permission():
    for permission_name in dir(Permission):
        if permission_name.startswith("__"):
            continue
        p = getattr(Permission, permission_name)
        model = PermissionModel(name=p)
        db.session.add(model)
    db.session.commit()
    click.echo("权限添加成功")

def create_role():
    # 稽查
    inspector = RoleModel(name="稽查", desc="负责审核帖子和评论是否合法合规！")
    inspector.permission = PermissionModel.query.filter(PermissionModel.name.in_([Permission.POST, Permission.COMMENT])).all()

    # 运营
    operator = RoleModel(name="运营", desc="负责网站持续正常运营！")
    operator.permission = PermissionModel.query.filter(PermissionModel.name.in_([
        Permission.POST,
        Permission.COMMENT,
        Permission.BOARD,
        Permission.FRONT_USER
    ])).all()

    # 管理员
    administator = RoleModel(name="管理员", desc="负责整个网站所有工作！")
    administator.permission = PermissionModel.query.all()

    db.session.add_all([inspector, operator, administator])
    db.session.commit()
    click.echo("权限添加成功！")

def create_test_user():
    admin_role = RoleModel.query.filter_by(name="管理员").first()
    zhangsan = UserModel(username="张三", email="zhangsan@zlkt.net", password="111111", is_staff=True, role=admin_role)

    operator_role = RoleModel.query.filter_by(name="运营").first()
    lisi = UserModel(username="李四", email="lisi@zlkt.net", password="111111", is_staff=True, role=operator_role)

    inspector_role = RoleModel.query.filter_by(name="稽查").first()
    wangwu = UserModel(username="王五", email="wangwu@zlkt.net", password="111111", is_staff=True, role=inspector_role)

    db.session.add_all([zhangsan, lisi, wangwu])
    db.session.commit()
    click.echo("测试用户添加成功！")

@click.option("--username", '-u')
@click.option("--password", '-p')
@click.option("--email", '-e')
def create_admin(name, password, email):
    admin_role = RoleModel.query.filter_by(name="管理员").first()
    model = UserModel(name=name, password=password, email=email, is_staff=True, role=admin_role)
    db.session.add(model)
    db.session.commit()
    click.echo("管理员添加成功")

def create_board():
    board_names = ['Python语法', 'web开发', '数据分析', '测试开发', '运维开发']
    for board_name in board_names:
        model = BoardModel(name=board_name)
        db.session.add(model)
    db.session.commit()
    click.echo("添加板块成功")
