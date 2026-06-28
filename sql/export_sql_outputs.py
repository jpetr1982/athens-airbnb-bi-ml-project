import sqlite3
import pandas as pd
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

SQL_DIR = PROJECT_ROOT / "sql"
EXCEL_DIR = PROJECT_ROOT / "excel"
OUTPUT_DIR = EXCEL_DIR / "sql_exports"

database_file = SQL_DIR / "athens_airbnb.db"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

queries = {
    "market_overview": "01_market_overview.sql",
    "neighbourhood_summary": "02_neighbourhood_summary.sql",
    "room_type_summary": "03_room_type_summary.sql",
    "high_price_segments": "04_high_price_segments.sql",
    "price_capacity_analysis": "05_price_capacity_analysis.sql",
    "excel_analytical_table": "06_excel_export_queries.sql"
}

conn = sqlite3.connect(database_file)

for output_name, sql_filename in queries.items():
    sql_path = SQL_DIR / sql_filename

    with open(sql_path, "r", encoding="utf-8") as file:
        query = file.read()

    result = pd.read_sql_query(query, conn)

    output_file = OUTPUT_DIR / f"{output_name}.csv"
    result.to_csv(output_file, index=False, encoding="utf-8-sig")

    print(f"Exported: {output_file}")

conn.close()

print("All SQL query outputs exported successfully.")