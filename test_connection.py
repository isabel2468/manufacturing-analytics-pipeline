from sqlalchemy import text
from utils_db import get_engine

engine = get_engine()

with engine.connect() as conn:
    result = conn.execute(text("SELECT 1;"))
    print("DB connection OK:", result.scalar())
