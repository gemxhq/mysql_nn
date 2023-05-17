import os.path

from flask import Blueprint, render_template, redirect, request, jsonify, current_app, url_for
from utils.restful import params_error
from werkzeug.utils import secure_filename
from exts import csrf
import hashlib

bp = Blueprint("front", __name__, url_prefix="")

@bp.route('/')
def index():
    return "hello!"

@bp.route('/post/public', methods=['GET', 'POST'])
def public_post():
    if request.method == 'GET':
        return render_template("front/public_post.html")
    else:
        pass

@bp.post('/upload/image')
@csrf.exempt
def upload_image():
    f = request.files.get('images')
    # 判断图片格式
    extension = f.filename.split('.')[-1].lower()
    if extension not in ['jpg', 'gif', 'png', 'jpeg']:
        return jsonify({
            "errno": 400,
            "data": [{}]
        })

    #
    filename = secure_filename(f.filename)
    f.save(os.path.join(current_app.config.get("UPLOAD_IMAGE_PATH"), filename))
    url = url_for('media.media_file', filename=filename)
    return jsonify({
        "errno": 0,
        "data": [{
            "url": url,
            "alt": "",
            "href": ""
        }]
    })

def email_hash(email):
    return hashlib.md5(email.encode('utf-8')).hexdigest()

@bp.route('/test/avatar/<string:email>')
def test_avatar(email):
    email_hash_data = email_hash(email)
    return render_template("front/test_upload.html", email_hash_data=email_hash_data)

