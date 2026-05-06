from sthlm_puls.utils.helpers import get_events_df
import duckdb
import streamlit as st
import pandas as pd
from datetime import datetime

df = get_events_df()

def total_events_kpi(filtered, genre):
    if genre != "All":
        genre_escaped = genre.replace("'", "''")
        count = duckdb.sql(f"""
            SELECT COUNT(*) as num_events
            FROM filtered
            WHERE genre ILIKE '%{genre_escaped}%'
        """).fetchone()[0]
    else:
        count = len(filtered)
    return count

def unique_venues_kpi(filtered, venue):
    if venue != "All":
        count = duckdb.sql(f"""
            SELECT COUNT(DISTINCT venue_name)
            FROM filtered
            WHERE venue_name ILIKE '%{venue}%'
        """).fetchone()[0]
    else:
        count = duckdb.sql("""
                           SELECT COUNT(DISTINCT venue_name)
                           FROM filtered
                           """).fetchone()[0]
    return count

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
    result = duckdb.sql(f"""--sql
    SELECT COUNT(*)
    FROM df
    WHERE CAST(date as DATE) = current_date
""").fetchone()

    return result[0] if result else 0
