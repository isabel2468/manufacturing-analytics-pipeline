from pathlib import Path
from sqlalchemy import text
from utils_db import get_engine

BASE_DIR = Path(__file__).resolve().parents[1]
SQL_PATH = BASE_DIR / "sql" / "transform_core.sql"

def main():
    engine = get_engine()
    sql = SQL_PATH.read_text(encoding="utf-8")

    with engine.begin() as conn:
        conn.execute(text(sql))

    print("✅ Transformation finished: raw → core")
if __name__ == "__main__":
    main()

