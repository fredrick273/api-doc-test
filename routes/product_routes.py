from flask import Blueprint, request, jsonify
from services.product_service import create_product, get_all_products

product_bp = Blueprint("product", __name__)

@product_bp.route("/", methods=["POST"])
def create():
    data = request.json
    product = create_product(data["name"], data["price"])
    return jsonify(product), 201

@product_bp.route("/", methods=["GET"])
def list_products():
    return jsonify(get_all_products()), 200
