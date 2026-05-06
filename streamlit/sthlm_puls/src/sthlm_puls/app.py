import streamlit as st
import sys
import os
from sthlm_puls.utils.constants import IMAGE_PATH

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))


st.set_page_config(layout="wide")

# Header
st.image(IMAGE_PATH / "sthlmpuls.png", use_container_width=True)

pages = [
    st.Page("pages/home.py", title="Home"),
    st.Page("pages/events.py", title="Events"),
    st.Page("pages/raw_data.py", title="Events_raw"),
]
pg = st.navigation(pages)
pg.run()

# Footer
st.image(IMAGE_PATH / "sthlmpuls_footer.png", use_container_width=True)

