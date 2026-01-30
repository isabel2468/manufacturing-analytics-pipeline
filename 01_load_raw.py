import pandas as pd
from utils_db import get_engine
from pathlib import Path

# Projekt-Root automatisch bestimmen
BASE_DIR = Path(__file__).resolve().parents[1]

# Path
DATA_DIR = BASE_DIR / "data" / "raw"

FILES = [
    ("products_master_raw.csv", "raw", "products_master"),
    ("customers_raw.csv", "raw", "customers"),
    ("sales_orders_raw.csv", "raw", "sales_orders"),
    ("production_output_raw.csv", "raw", "production_output"),
]

def main():
    engine = get_engine()

    with engine.begin() as conn:
        conn.exec_driver_sql("TRUNCATE raw.products_master;")
        conn.exec_driver_sql("TRUNCATE raw.customers;")
        conn.exec_driver_sql("TRUNCATE raw.sales_orders;")
        conn.exec_driver_sql("TRUNCATE raw.production_output;")

    for filename, schema, table in FILES:
        path = DATA_DIR / filename

        # Debug-Ausgabe (nur temporär!)
        print(f"Reading file: {path}")

        df = pd.read_csv(path)

        df.to_sql(
            name=table,
            con=engine,
            schema=schema,
            if_exists="append",
            index=False
        )

        print(f"Loaded {filename} → {schema}.{table} ({len(df)} rows)")

if __name__ == "__main__":
    main()
