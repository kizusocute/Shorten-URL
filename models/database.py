# models/database.py
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Tải biến môi trường từ file .env (chỉ hoạt động local)
load_dotenv()

# Lấy URI từ biến môi trường, không dùng mặc định localhost
MONGO_URI = os.getenv("MONGO_URI")

if not MONGO_URI:
    raise Exception("❌ MONGO_URI chưa được thiết lập!")

# Tạo MongoDB client
client = MongoClient(MONGO_URI)

# Database và collection
db = client["url_shortener_db"]
urls_collection = db["urls"]

