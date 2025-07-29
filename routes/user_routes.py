from flask import Blueprint, request, jsonify
from services.user_service import create_user, get_all_users

user_bp = Blueprint("user", __name__)

@user_bp.route("/", methods=["POST"])
def create():
    data = request.json
    user = create_user(data["username"], data["email"])
    return jsonify(user), 201

@user_bp.route("/", methods=["GET"])
def list_users():
    return jsonify(get_all_users()), 200
