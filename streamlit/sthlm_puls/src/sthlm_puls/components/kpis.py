import duckdb
import pandas as pd
from datetime import datetime

def count_kpi(filtered: pd.DataFrame, column: str, value: str) -> int:
    if value != "All":
        return len(filtered[filtered[column].str.contains(value, case=False, na=False)])
    return len(filtered[column].dropna().unique()) if column == "venue_name" else len(filtered)


def total_events_this_month_kpi(df: pd.DataFrame) -> int:
    current_month = datetime.today().month
    current_year = datetime.today().year
    result = duckdb.sql(f"""--sql
    SELECT COUNT(*) as num_events_this_month
    FROM df
    WHERE MONTH(CAST(date as DATE)) = {current_month}
    AND YEAR(CAST(date as DATE)) = {current_year}
""").fetchone()
    return result[0] if result else 0


def total_events_today_kpi(df: pd.DataFrame) -> int:
    result = duckdb.sql("""--sql
    SELECT COUNT(*)
    FROM df
    WHERE CAST(date as DATE) = current_date
                        """).fetchone()
    return result[0] if result else 0