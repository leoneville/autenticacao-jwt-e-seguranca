from flask import request

from src.drivers.jwt_handler import JwtHandler
from src.errors.http_exception import HttpException


def auth_jwt_verify():
    jwt_handler = JwtHandler()
    raw_token = request.headers.get("Authorization")
    user_id = request.headers.get("uid")

    if not raw_token or not user_id:
        raise HttpException(
            message="Invalid Auth informations", name="Unauthorized", status_code=401
        )

    token = raw_token.split()[1]
    token_information = jwt_handler.decode_jwt_token(token)
    token_uid = token_information["user_id"]

    if user_id and token_uid and (int(token_uid) == int(user_id)):
        return token_information

    raise HttpException(
        message="User Unauthorized", name="Unauthorized", status_code=401
    )
