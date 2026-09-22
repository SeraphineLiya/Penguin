import os

from dotenv import load_dotenv

load_dotenv()

# put your Discord bot token in .env, never hardcode it here
DISCORD_TOKEN = os.environ["DISCORD_TOKEN"]

DATABASE_PATH = os.environ.get("DATABASE_PATH", "penguin.db")
