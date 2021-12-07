from datetime import datetime, timedelta

import jwt
from decouple import config
from flask_httpauth import HTTPTokenAuth
from models.user import AdministratorModel, ApproverModel, ComplainerModel
from werkzeug.exceptions import BadRequest

mapper = {
    "AdministratorModel": lambda x: AdministratorModel.query.filter_by(id=x).first(),
    "ApproverModel": lambda x: ApproverModel.query.filter_by(id=x).first(),
    "ComplainerModel": lambda x: ComplainerModel.query.filter_by(id=x).first(),
}


class AuthManager:
    @staticmethod
    def encode_token(user):
        payload = {
            "sub": user.id,
            "exp": datetime.utcnow() + timedelta(days=100),
            "role": user.__class__.__name__,
        }

        return jwt.encode(payload, key=config("JWT_key"), algorithm="HS256")

    @staticmethod
    def decode_token(token):
        try:
            data = jwt.decode(token, key=config("JWT_key"), algorithms=["HS256"])
            return data["sub"], data["role"]
        except jwt.ExpiredSignatureError:
            raise BadRequest("Token is expired")
        except jwt.InvalidTokenError:
            raise BadRequest("Ivalid token")


auth = HTTPTokenAuth(scheme="Bearer")


@auth.verify_token
def verify_token(token):
    user_id, role = AuthManager.decode_token(token)
    user = mapper[role](user_id)
    # user = eval(f"{role}.query.filter_by(id={user_id}).first()")
    return user
