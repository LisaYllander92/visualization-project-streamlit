import streamlit as st
from sthlm_puls.utils.helpers import get_events_df

def raw_data():
    st.title("RAW DATA")
    st.markdown("Explore the raw dataset")
    st.dataframe(get_events_df())

if __name__ == "__main__":
    raw_data()