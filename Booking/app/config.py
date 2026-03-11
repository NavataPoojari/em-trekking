import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        "postgresql://postgres:root@localhost:5432/trekky-hub-db"
    )
    SECRET_KEY = os.getenv("SECRET_KEY", "treekyhub_secret")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 60

settings = Settings()