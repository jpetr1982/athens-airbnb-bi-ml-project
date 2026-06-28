import sqlite3
import pandas as pd
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

DATA_PROCESSED = PROJECT_ROOT / "data" / "processed"
SQL_DIR = PROJECT_ROOT / "sql"

input_file = DATA_PROCESSED / "cleaned_airbnb_athens.csv"
database_file = SQL_DIR / "athens_airbnb.db"

df = pd.read_csv(input_file)

conn = sqlite3.connect(database_file)

df.to_sql(
    "airbnb_listings",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print(f"SQLite database created successfully: {database_file}")
print(f"Rows inserted: {len(df)}")