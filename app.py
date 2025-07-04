from flask import Flask
from routes.url_routes import url_bp

# Nếu muốn hỗ trợ CORS (khi có frontend riêng)
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Cho phép CORS nếu cần

# Đăng ký Blueprint
app.register_blueprint(url_bp)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Railway sẽ cấp PORT tự động
    app.run(debug=False, host='0.0.0.0', port=port)
