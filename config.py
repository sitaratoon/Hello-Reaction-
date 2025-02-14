from os import environ

API_HASH = environ.get("API_HASH", "c163d4e28e63196c3806cf3b9b2885de")
API_ID = int(environ.get("API_ID", "18946488"))
BOT_TOKEN = environ.get("BOT_TOKEN", "")
BOT_OWNER = int(environ.get("BOT_OWNER", "7475464684"))
BOT_USERNAME = environ.get("BOT_USERNAME", "Autoreaction08bot")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002425566477"))
AUTH_CHANNEL = int(environ.get("AUTH_CHANNEL", "-1002355394644"))
DATABASE_URL = environ.get("DATABASE_URL", "mongodb+srv://Renamest:Renamest@cluster0.prfhc.mongodb.net/?retryWrites=true&w=majority")

# Define default emojis list
EMOJIS = [
    "❤‍🔥", "🤗", "🔥", "🥰", "👏", "😁", "😘", "🥶", "🤩", "👍", "😎", "🙏", "😍", "💯"
]
