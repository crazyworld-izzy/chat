from os import getenv

LOAD = getenv("LOAD", "").split()

NO_LOAD = getenv("NO_LOAD", "").split()

TOKEN = getenv("TOKEN", "6009759960:AAHUnDKep8-A9uuIKmEAnPIFrneaOIUsVGk")

MONGO_DB_URL = getenv(
    "MONGO_DB_URL",
    "mongodb+srv://Dada:izzyyir@143@cluster0.r3nby2c.mongodb.net/?retryWrites=true&w=majority",
)
