from os import environ

API_HASH = environ.get("API_HASH", "29bf447b916a795191046a91317869fb")
API_ID = int(environ.get("API_ID", "28918271"))
BOT_TOKEN = environ.get("BOT_TOKEN", "")
BOT_OWNER = int(environ.get("BOT_OWNER", ""))
BOT_USERNAME = environ.get("BOT_USERNAME", "Autoreaction02bot")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002425566477"))
AUTH_CHANNEL = int(environ.get("AUTH_CHANNEL", "-1002355394644"))
DATABASE_URL = environ.get("DATABASE_URL", "mongodb+srv://sitaratoons:sitaratoons@cluster0.98nq3.mongodb.net/?retryWrites=true&w=majority")

# Define default emojis list
EMOJIS = [
    "👍", "🤷‍♂", "❤", "🔥", "🥰", "👏", "😁", "🤔", "🤯", "😱", "🤬", "😢", 
    "🥶", "🤩", "🥳", "😎", "🙏", "👌", "🤣", "😇", "🥱", "🥴", "😍", "🤓", 
    "❤‍🔥", "🌚", "😐", "💯", "🦄", "⚡", "👾", "🏆", "💔", "🤨", "🌟", "😡", 
    "👅", "🆒", "😘", "😈", "😴", "😭", "👻", "🌈", "👨‍💻", "👀", "🎃", "🙄", 
    "🤧", "😨", "🤝", "🤐", "🤗", "🫡", "🤭", "🥸", "🤫", "😶‍🌫", "🤪", "😏"
]
