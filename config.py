from os import getenv

LOAD = getenv("LOAD", "").split()

NO_LOAD = getenv("NO_LOAD", "").split()

TOKEN = getenv("TOKEN", "6009759960:AAH3DReD9SHORYZIqpV3fvP5iX8iwEb8xUg")

MONGO_DB_URL = getenv(
    "MONGO_DB_URL",
    "mongodb+srv://moni:moni@cluster0.m7vwjn8.mongodb.net/?retryWrites=true&w=majority",
)
