import streamlit as st

pages = [
    st.Page("pages/home.py", title="Home"),
    st.Page("pages/events.py", title="Events"),
    st.Page("pages/raw_data.py", title="Events_raw"),
]
st.set_page_config(layout="wide")
pg = st.navigation(pages)

pg.run()