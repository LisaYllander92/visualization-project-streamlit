import streamlit as st

from sthlm_puls.utils.constants import IMAGE_PATH, MARKDOWN_PATH
from sthlm_puls.utils.helpers import read_textfile
from sthlm_puls.components.charts import plot_events_weekday
from sthlm_puls.utils.helpers import read_textfile, get_events_df

def home():
    st.image(IMAGE_PATH / "sthlmpuls.png", width=1485)
    st.markdown(read_textfile(MARKDOWN_PATH / "intro_events.md"))
    home_footer()


def home_footer():
    st.image(IMAGE_PATH / "sthlmpuls_footer.png", width=1485)  # Justerad bredd


if __name__ == "__main__":
    home()