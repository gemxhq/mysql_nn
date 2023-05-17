from flask import jsonify

class HttpCode:
    # 响应正常
    ok = 200
    # 没有登陆错误
    unloginerror = 401
    # 没有权限错误
    permissionerror = 403
    # 客户端参数错误
    paramserror = 400
    # 服务器错误
    servererror = 500

def _restful_result(code, message, data):
    return jsonify({"message": message or "", "data": data or {}}), code

def ok(message=None, data=None):
    return _restful_result(HttpCode.ok, message, data)

def unlogin_error(message="没有登录"):
    return _restful_result(HttpCode.ok, message=message, data=None)

def permission_error(message="没有权限反问"):
    return _restful_result(HttpCode.permissionerror, message, data=None)

def params_error(message="参数错误"):
    return _restful_result(HttpCode.paramserror, message, data=None)

def server_error(message="服务器错误"):
    return _restful_result(HttpCode.servererror, message, data=None)



