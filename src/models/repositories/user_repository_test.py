from src.models.settings.db_connection_handler import db_connection_handler
from .user_repository import UserRepository


def test_repository():
    db_connection_handler.connect()
    conn = db_connection_handler.get_connection()
    repo = UserRepository(conn)

    username = "Bob Esponja"
    password = "123rocket!"

    user = repo.get_user_by_username(username)
    print(user, password)
