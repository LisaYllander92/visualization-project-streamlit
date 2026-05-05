import streamlit as st

from sthlm_puls.utils.constants import IMAGE_PATH, MARKDOWN_PATH
from sthlm_puls.utils.helpers import read_textfile
from sthlm_puls.components.charts import plot_events_weekday
from sthlm_puls.components.filters import read_textfile, get_events_df

def home():
    st.markdown("# HOME")
    st.image(IMAGE_PATH / "sthlmpuls.png")
    st.markdown(read_textfile(MARKDOWN_PATH / "intro_events.md"))
    df = get_events_df()
    fig = plot_events_weekday(df)
    st.pyplot(fig)



if __name__ == "__main__":
    home()