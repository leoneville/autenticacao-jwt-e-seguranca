from src.controllers.balance_editor import BalanceEditor
from src.models.repositories.user_repository import UserRepository
from src.models.settings.db_connection_handler import db_connection_handler
from src.views.balance_editor import BalanceEditorView


def balance_editor_composer():
    conn = db_connection_handler.get_connection()
    model = UserRepository(conn)
    controller = BalanceEditor(model)
    view = BalanceEditorView(controller)

    return view
