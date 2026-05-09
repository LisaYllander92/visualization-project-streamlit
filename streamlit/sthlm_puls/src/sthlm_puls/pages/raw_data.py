import streamlit as st
from sthlm_puls.utils.helpers import get_raw_events_df

def raw_data():
    st.title("RAW DATA")
    st.markdown("Explore the underlying dataset behind the visualizations. "
    "Data is sourced from Ticketmaster, VisitStockholm, Fasching, and Berns — "
    "cleaned, merged, and updated regularly.")
    st.dataframe(get_raw_events_df())

if __name__ == "__main__":
    raw_data()