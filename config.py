from os import getenv

LOAD = getenv("LOAD", "").split()

NO_LOAD = getenv("NO_LOAD", "").split()

TOKEN = getenv("TOKEN","7817669190:AAFiCkLQAKItlA4uhbqO_hlpRfnDLr6my-Q")

MONGO_DB_URL = getenv(
    "MONGO_DB_URL",
    "mongodb+srv://moni:moni@cluster0.dcufenj.mongodb.net/?retryWrites=true&w=majority",
)
