from flask import Flask
from routes.user_routes import user_bp
from routes.product_routes import product_bp

app = Flask(__name__)
app.register_blueprint(user_bp, url_prefix="/users")
app.register_blueprint(product_bp, url_prefix="/products")

if __name__ == "__main__":
    app.run(debug=True)
