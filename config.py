from os import getenv

LOAD = getenv("LOAD", "").split()

NO_LOAD = getenv("NO_LOAD", "").split()

TOKEN = getenv("TOKEN", "6009759960:AAEMrabQKJcYXvw3QwNLDHryQ0IGniDYkJU")

MONGO_DB_URL = getenv(
    "MONGO_DB_URL",
    "mongodb+srv://King098:king098@cluster0.lhmvji8.mongodb.net/?retryWrites=true&w=majority",
)
