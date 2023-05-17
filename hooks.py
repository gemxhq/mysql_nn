from flask import g, session
from models.user import UserModel

def bbs_before_request():
    if "user_id" in session:
        user_id = session.get("user_id")
        user = UserModel.query.filter_by(id=user_id).first()
        setattr(g, "user", user)
    else:
        setattr(g, "user", None)
