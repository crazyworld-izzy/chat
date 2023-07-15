from os import getenv

LOAD = getenv("LOAD", "").split()

NO_LOAD = getenv("NO_LOAD", "").split()

TOKEN = getenv("TOKEN", "5995538130:AAEN9hTOGr0P_zYBsRWjmwq1g35uUS4ef_8")

MONGO_DB_URL = getenv(
    "MONGO_DB_URL",
    "mongodb+srv://moni1:ammu@cluster0.lmgyalw.mongodb.net/?retryWrites=true&w=majority",
)
