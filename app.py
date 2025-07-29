#test
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "ok"}), 200


@app.route("/users", methods=["POST"])
def create_user():
    token = request.headers.get("Authorization")
    if not token or not token.startswith("Bearer "):
        return jsonify({"error": "Unauthorized"}), 401

    data = request.json
    if "username" not in data or "email" not in data:
        return jsonify({"error": "Missing fields"}), 400

    return jsonify({"message": "User created", "user": data}), 201


@app.route("/users", methods=["GET"])
def list_users():
    page = request.args.get("page", default=1, type=int)
    limit = request.args.get("limit", default=10, type=int)
    return jsonify({
        "page": page,
        "limit": limit,
        "users": [{"id": 1, "username": "Alice"}, {"id": 2, "username": "Bob"}]
    }), 200


@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    token = request.headers.get("Authorization")
    if not token or not token.startswith("Bearer "):
        return jsonify({"error": "Unauthorized"}), 401

    return jsonify({"message": f"User {user_id} deleted"}), 200


if __name__ == "__main__":
    app.run(debug=True)
