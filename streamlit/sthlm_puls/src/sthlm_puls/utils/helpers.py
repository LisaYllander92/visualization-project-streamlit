from sthlm_puls.utils.constants import DATA_PATH
import pandas as pd
import streamlit as st

def read_textfile(path) -> str:
    with open(path, "r", encoding="utf-8") as file:
        return file.read()


@st.cache_data
def get_events_df(future_only: bool = True) -> pd.DataFrame:
    df = pd.read_csv(DATA_PATH / "events_combined.csv")
    df["date"] = pd.to_datetime(df["date"])
    if future_only:
        df = df[df["date"] >= pd.Timestamp.today().normalize()]
    return df


def read_css(path):
    css = read_textfile(path)
    st.write(
        f"<style>{css}</style>", unsafe_allow_html=True
    )
