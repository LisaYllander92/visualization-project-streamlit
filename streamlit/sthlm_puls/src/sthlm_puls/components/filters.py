import streamlit as st
import pandas as pd

def venue_filter(df: pd.DataFrame) -> str:
    venues = ["All"] + sorted(df["venue_name"].dropna().unique().tolist())
    return st.selectbox(label="Venue", options=venues)

def genre_filter(df: pd.DataFrame) -> str:
    genres = ["All"] + sorted(df["genre"].dropna().unique().tolist())
    return st.selectbox(label="Genre", options=genres)

def date_filter(df: pd.DataFrame):
    min_date = df["date"].min().date()
    max_date = df["date"].max().date()
    return st.date_input(
        label="Date",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date
    )