import streamlit as st
import base64
from sthlm_puls.utils.constants import IMAGE_PATH

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
with open(IMAGE_PATH / "sthlmpuls_footer.png", "rb") as f:
    data = base64.b64encode(f.read()).decode()

st.markdown(f"""
    <div style="position: relative; width: 100%; margin-top: 2rem;">
        <img src="data:image/png;base64,{data}" style="width: 100%; display: block;">
    </div>
""", unsafe_allow_html=True)

