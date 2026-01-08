import os
from dotenv import load_dotenv

load_dotenv()

# Basic Details
API_ID = int(os.getenv("API_ID", "0"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Database & Session
MONGO_DB_URI = os.getenv("MONGO_DB_URI")
STRING_SESSION = os.getenv("STRING_SESSION")

# Owner & Bot Name
OWNER_ID = int(os.getenv("OWNER_ID", "12345678"))
MUSIC_BOT_NAME = os.getenv("MUSIC_BOT_NAME", "Nobita Music")

# Images (Yahan aap Nobita ki image link dal sakte hain)
START_IMG_URL = os.getenv("START_IMG_URL", "https://telegra.ph/file/your-image.jpg")

