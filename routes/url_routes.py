from flask import Blueprint, request, jsonify, redirect
from models.url import save_url, get_original_url
from flask import render_template


url_bp = Blueprint("url_bp", __name__)

@url_bp.route('/shorten', methods=['POST'])
def shorten_url():
    try:
        data = request.get_json()
        if not data or "url" not in data:
            return jsonify({"error": "Thiếu trường 'url' trong dữ liệu gửi lên"}), 400

        original_url = data["url"].strip()
        if not original_url:
            return jsonify({"error": "URL không được để trống"}), 400

        short_code = save_url(original_url)
        if not short_code:
            return jsonify({"error": "URL không hợp lệ hoặc tạo mã thất bại"}), 422

        short_url = request.host_url + short_code
        return jsonify({"short_url": short_url})

    except Exception as e:
        print("Lỗi khi xử lý /shorten:", e)
        return jsonify({"error": "Đã xảy ra lỗi phía máy chủ"}), 500

@url_bp.route('/<short_code>')
def redirect_url(short_code):
    original_url = get_original_url(short_code)
    if not original_url:
    	return jsonify({"error": "Missing 'url' in request body"}), 400
    return redirect(original_url)
    
@url_bp.route('/')
def index():
    return render_template("index.html")


