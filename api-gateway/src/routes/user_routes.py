import requests
from flask import Blueprint, request, jsonify
from src.config import Config

user_bp = Blueprint('user', __name__)

@user_bp.route('/register', methods=['POST'])
def register():
    res = requests.post(f"{Config.USER_SERVICE_URL}/register", json=request.json)
    return jsonify(res.json()), res.status_code

@user_bp.route('/login', methods=['POST'])
def login():
    res = requests.post(f"{Config.USER_SERVICE_URL}/login", json=request.json)
    return jsonify(res.json()), res.status_code
