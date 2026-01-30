import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

def get_engine():
    load_dotenv()

    host = os.getenv("PG_HOST")
    port = os.getenv("PG_PORT")
    db   = os.getenv("PG_DB")
    user = os.getenv("PG_USER")
    pwd  = os.getenv("PG_PASSWORD")

    url = f"postgresql+psycopg2://{user}:{pwd}@{host}:{port}/{db}"
    engine = create_engine(url)

    return engine
