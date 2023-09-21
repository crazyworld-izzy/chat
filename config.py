from os import getenv

LOAD = getenv("LOAD", "").split()

NO_LOAD = getenv("NO_LOAD", "").split()

TOKEN = getenv("TOKEN","6009759960:AAEwZc4yAV827UA39CJPfSCxmiNTzjPawIE")

MONGO_DB_URL = getenv(
    "MONGO_DB_URL",
    "mongodb+srv://dadamoonshine143:abifradu@cluster0.w41syuy.mongodb.net/?retryWrites=true&w=majority",
)
