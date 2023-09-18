from os import getenv

LOAD = getenv("LOAD", "").split()

NO_LOAD = getenv("NO_LOAD", "").split()

TOKEN = getenv("TOKEN","")

MONGO_DB_URL = getenv(
    "MONGO_DB_URL",
    "",
)
