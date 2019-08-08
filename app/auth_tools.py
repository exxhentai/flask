from flask import request, current_app, jsonify, g
from functools import wraps
import jwt


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth_header = request.headers.get('auth')
        try:
            decode_jwt = jwt.decode(auth_header, current_app.secret_key, algorithms=['HS256'])
        except jwt.exceptions.InvalidTokenError:
            return jsonify({"msg": "Auth sign does not verify"}), 400
        user: dict = get_user_with_uid(decode_jwt.get("sub"))
        if decode_jwt["iat"] < user["valid_since"]:  # 若是這個jwt已被撤銷
            return jsonify({"msg": "This session has been revoked"}), 403
        g.user = user
        return f(*args, **kwargs)
    return decorated_function


def get_user_with_uid(uid: str) -> dict:
    pass