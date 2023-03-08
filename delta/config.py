import os
from dotenv import load_dotenv

if os.path.isfile("config.env"):
    load_dotenv("config.env")


os.environ['__doc__'] = "Delta telegram bot."

class Config:
    BOT_TOKEN = os.environ.get('BOT_TOKEN')
    API_ID = int(os.environ.get('API_ID'))
    API_HASH = os.environ.get('API_HASH')
    MONGO_DB = os.environ.get('MONGO_DB')
    LOG_CHATS = int(os.environ.get('LOG_CHATS'))
    OWNER_ID = int(os.environ.get('OWNER_ID'))
    SUDO_USER = [int(user_id) for user_id in os.environ.get('SUDO_USER', '').split()]
    WORKERS = int(os.environ.get('WORKERS', '12'))

    @classmethod
    def validate(cls):
        for key, value in cls.__dict__.items():
            if value is None:
                raise ValueError(f'{key} must be set in the environment variables')

