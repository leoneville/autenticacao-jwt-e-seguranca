from flask import Blueprint, jsonify

bank_routes_bp = Blueprint("bank_routes", __name__)


@bank_routes_bp.get("/")
def hello():
    return jsonify(Hello="World"), 200
