import os

class Config:
    API_ID = int(os.environ.get("API_ID", "0"))
    API_HASH = os.environ.get("API_HASH", "")
    TOKEN = os.environ.get("TOKEN", "")
    
    OWNER_ID = int(os.environ.get("OWNER_ID", "0"))
    SUDO = [OWNER_ID] if OWNER_ID else []
    
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    BOT_NAME = os.environ.get("BOT_NAME", BOT_USERNAME)
    BOT_ID = int(TOKEN.split(":")[0]) if TOKEN and ":" in TOKEN else 0

    DATABASE_URL = os.environ.get("DATABASE_URL", "")
    FORCE_SUB_CHANNEL = os.environ.get("FORCE_SUB_CHANNEL", "")
    START_IMG = os.environ.get("START_IMG_URL", "")
    
    PORT = int(os.environ.get("PORT", "8080"))
