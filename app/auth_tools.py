from flask import request, current_app, jsonify, g
from functools import wraps
import jwt
from bson.objectid import ObjectId


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth_header = request.headers.get('auth')
        try:
            decode_jwt = jwt.decode(auth_header, current_app.secret_key, algorithms=['HS256'])
        except jwt.exceptions.InvalidTokenError:
            return jsonify({"msg": "Auth sign does not verify"}), 400
        user: dict = get_user_with_uid(decode_jwt.get("sub"))
        if user is None:
            return jsonify({"msg": "Can not find user data"}), 403
        if decode_jwt["iat"] < user["valid_since"]:  # 若是這個jwt已被撤銷
            return jsonify({"msg": "This session has been revoked"}), 403
        g.user = user
        return f(*args, **kwargs)
    return decorated_function


def get_user_with_uid(uid: str) -> dict:
    return g.db.users.find_one({"_id": ObjectId(uid)})


def sign(json_: dict) -> str:
    return jwt.encode(json_, current_app.secret_key, algorithm='HS256').decode()


def verify_sing(signed: str) -> dict:
    return jwt.decode(signed.encode(), current_app.secret_key, algorithms=['HS256'])


def is_username_exist(username: str) -> bool:
    result = g.db.users.find_one({"username": username})
    if result is None:
        return False
    else:
        return True


def get_user_with_username(username: str):
    return g.db.users.find_one({"username": username})