import pandas as pd
import pydeck as pdk
from sthlm_puls.utils.constants import MAPBOX_TOKEN

pdk.settings.mapbox_key = MAPBOX_TOKEN

def events_map(df: pd.DataFrame, mapbox_token: str):
    layer = pdk.Layer(
        "ScatterplotLayer",
        data=df[["venue_lat", "venue_lon", "venue_name"]].drop_duplicates(),
        get_position=["venue_lon", "venue_lat"],
        get_radius=100,
        get_fill_color=[255, 102, 102],
        pickable=True
    )

    view = pdk.ViewState(
        latitude=59.33,
        longitude=18.07,
        zoom=12
    )

    return pdk.Deck(
        layers=[layer],
        initial_view_state=view,
        tooltip={"text": "{venue_name}"},
        map_style="mapbox://styles/mapbox/navigation-night-v1",
        api_keys={"mapbox": mapbox_token})

