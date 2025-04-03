import os

DATABASE_URL = os.getenv("DATABASE_URL", "mysql+pymysql://root:password@db/flaskapp")

