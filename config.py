import os
from dotenv import load_dotenv

# .env file se data load karne ke liye
load_dotenv()

# --- Telegram API Details ---
API_ID = int(os.getenv("API_ID", "20106942"))
API_HASH = os.getenv("API_HASH", "3bfe2013e4399af96d78640db6dcd601")
BOT_TOKEN = os.getenv("BOT_TOKEN") # Ye environment variable se lega

# --- Assistant & Session ---
# Aapne jo string session diya hai use yahan variable mein rakha jayega
STRING_SESSION = os.getenv("BQFYxG8AiWLC6RJZ_RT7PDDjWbGXQChpwzd1F0B8b6XmYjh-G0_pp_adu0cboUGPbu_JLABAQOadfDzIXouJ_B2NdAZF-eD0E6ETTNUO89Cds2cuPLNdSa5qORDcZGQek8rnNcgzavSA5kkBh-pOO--Szskm1M547vUSnsQec-iws1wZmB-j4YU7lt-e1NfRf3gb_kB5dMA94i6A3_seyiaVKzQggg7Clf-CREpRPul4dtUnAscgH10-re-Xr9LL-gu_EPotRYea0V4HL5WMr5a-XBPCm4ull9sT6iPt23Pgi10gQChc58Jh3UZPxekNzQKaxKunko_3084hIowU779hJ3fotAAAAAHYWpZnAA")

# --- Database & Owner ---
MONGO_DB_URI = os.getenv("MONGO_DB_URI", "mongodb+srv://flexiblecrabqxbc_db_user:VP1hYN2TmFAQ9bCy@nobita.brx3tzs.mongodb.net/?retryWrites=true&w=majority&appName=Nobita")
OWNER_ID = int(os.getenv("OWNER_ID", "7081885854"))

# --- NexGenBots API Settings ---
API_KEY = os.getenv("API_KEY", "NxGBNexGenBots3e0ca1")
API_URL = os.getenv("API_URL", "https://api.nexgenbots.xyz")
VIDEO_API_URL = os.getenv("VIDEO_API_URL", "https://api.video.nexgenbots.xyz")

# --- Bot Customization ---
MUSIC_BOT_NAME = os.getenv("MUSIC_BOT_NAME", "Nobitahu")
START_IMG_URL = os.getenv("START_IMG_URL", "https://telegra.ph/file/your-image-link.jpg")
