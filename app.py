from flask import Flask
from routes.url_routes import url_bp

# Nếu muốn hỗ trợ CORS (khi có frontend riêng)
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Cho phép CORS nếu cần

# Đăng ký Blueprint
app.register_blueprint(url_bp)

if __name__ == '__main__':
    app.run(debug=True)

