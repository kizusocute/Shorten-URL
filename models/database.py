from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Tải biến môi trường từ file .env
load_dotenv()

# Lấy URI từ file .env
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")

# Tạo client MongoDB
client = MongoClient(MONGO_URI)

# Chọn database tên "url_shortener_db"
db = client["url_shortener_db"]

# Lấy collection "urls" trong DB
urls_collection = db["urls"]
