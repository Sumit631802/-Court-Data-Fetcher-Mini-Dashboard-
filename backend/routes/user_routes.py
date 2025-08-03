from flask import Blueprint, request, jsonify
from models import User, db

# bp = Blueprint("user_routes", __name__)

# @bp.route("/users", methods=["GET"])
# def get_users():
#     users = User.query.all()
#     return jsonify([{"id": u.id, "name": u.name} for u in users])