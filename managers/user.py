from db import db
from models.user import ApproverModel, ComplainerModel
from werkzeug.exceptions import BadRequest
from werkzeug.security import check_password_hash, generate_password_hash


class UserManager:
    @staticmethod
    def register(user_data):
        user_data["password"] = generate_password_hash(user_data["password"])
        user = ComplainerModel(**user_data)
        db.session.add(user)
        db.session.flush()
        return user

    @staticmethod
    def login(user_data):
        user = ComplainerModel.query.filter_by(email=user_data["email"]).first()

        if not user:
            raise BadRequest("Wrong email or password")

        if not check_password_hash(user.password, user_data["password"]):
            raise BadRequest("Wrong email or password")

        return user

    @staticmethod
    def login_approver(user_data):
        user = ApproverModel.query.filter_by(email=user_data["email"]).first()

        if not user:
            raise BadRequest("Wrong email or password")

        if not check_password_hash(user.password, user_data["password"]):
            raise BadRequest("Wrong email or password")

        return user
