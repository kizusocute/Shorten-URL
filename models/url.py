import random
import string
from datetime import datetime, timedelta
from models.database import urls_collection
from urllib.parse import urlparse

# Hàm sinh mã ngắn (short_code)
def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits  # a-zA-Z0-9
    return ''.join(random.choices(characters, k=length))

# Hàm kiểm tra URL hợp lệ
def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False

# Lưu URL mới vào DB (mặc định hết hạn sau 3 ngày)
def save_url(original_url):
    if not is_valid_url(original_url):
        return None

    existing = urls_collection.find_one({"original_url": original_url})
    if existing:
        return existing["short_code"]

    for _ in range(5):
        short_code = generate_short_code()
        if not urls_collection.find_one({"short_code": short_code}):
            break
    else:
        return None

    expires_at = datetime.utcnow() + timedelta(days=3)

    data = {
        "original_url": original_url,
        "short_code": short_code,
        "created_at": datetime.utcnow(),
        "expires_at": expires_at
    }

    urls_collection.insert_one(data)
    return short_code

# Truy xuất URL gốc từ mã rút gọn
def get_original_url(short_code):
    result = urls_collection.find_one({"short_code": short_code})
    if not result:
        return None

    expires_at = result.get("expires_at")
    if expires_at and expires_at < datetime.utcnow():
        return "EXPIRED"

    return result["original_url"]

