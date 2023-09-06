from os import getenv

LOAD = getenv("LOAD", "").split()

NO_LOAD = getenv("NO_LOAD", "").split()

TOKEN = getenv("6009759960:AAFc2FI60Yveaa3X3_ITUyl50PkRSpKngLo")

MONGO_DB_URL = getenv(
    "MONGO_DB_URL",
    "mongodb+srv://moni:moni@cluster0.m7vwjn8.mongodb.net/?retryWrites=true&w=majority",
)
