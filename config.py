from os import getenv

from dotenv import load_dotenv

load_dotenv()

TOKEN = str(getenv("BOT_TOKEN"))

PG_DATABASE = str(getenv("PG_DATABASE"))
PG_USER = str(getenv("PG_USER"))
PG_PASSWORD = str(getenv("PG_PASSWORD"))
PG_HOST = str(getenv("PG_HOST"))
