import streamlit as st
import pandas as pd

def column_filter(df: pd.DataFrame, column: str, label: str, key: str) -> str:
    options = ["All"] + sorted(df[column].dropna().unique().tolist())
    return st.selectbox(label=label, options=options, key=key)

def venue_filter(df: pd.DataFrame) -> str:
    return column_filter(df, "venue_name", "Venue", "venue_filter")

def genre_filter(df: pd.DataFrame) -> str:
    return column_filter(df, "genre", "Genre", "genre_filter")

def date_filter(df: pd.DataFrame):
    min_date = df["date"].min().date()
    max_date = df["date"].max().date()
    return st.date_input(
        label="Date",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date,
        key="date_filter",
    )
