# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "14221458"))
API_HASH = os.environ.get("API_HASH", "1f7501fbe413b29f98f12f2a8c1eae6d")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5865017616:AAEYBqXZHpKGwA2l1YDYV9804EldvatpTMU")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("1291288382")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "CyniteOfficial")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://Dipanshu_021:ad8920@cluster0.f7migc1.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "1291288382")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(1291288382)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001470575315")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "Film_Update_Official") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
