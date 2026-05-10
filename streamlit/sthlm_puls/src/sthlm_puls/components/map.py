import pandas as pd
import folium
from streamlit_folium import st_folium

# import pydeck as pdk
# from sthlm_puls.utils.constants import MAPBOX_TOKEN, COLORS
# pdk.settings.mapbox_key = MAPBOX_TOKEN

def events_map(df: pd.DataFrame):
    m = folium.Map(
        location=[59.33, 18.07],
        zoom_start=12,
        tiles="OpenStreetMap",
    )

    for _, row in df[["venue_lat", "venue_lon", "venue_name", "name", "url"]].drop_duplicates().iterrows():
        folium.Marker(
            location=[row["venue_lat"], row["venue_lon"]],
            radius=5,
            color="#FF6666",
            fill=True,
            fill_color="#FF6666",
            fill_opacity=0.8,
            tooltip=f"{row['name']} - click for more info",
            popup=folium.Popup(
                f"""
                        <div style="font-family: sans-serif; min-width: 180px;">
                            <b>{row['name']}</b><br>
                            📍 {row['venue_name']}<br><br>
                            <a href="{row['url']}" target="_blank"
                               style="color: #FF6666; font-weight: bold;">
                                Read more and buy tickets →
                            </a>
                        </div>
                        """,
                max_width=250,
                sticky=True
            )
        ).add_to(m)

    return m




# def events_map(df: pd.DataFrame, mapbox_token: str):
#     link_color = COLORS["pink"]  # interpolera färgen innan HTML-strängen
#
#     layer = pdk.Layer(
#         "ScatterplotLayer",
#         data=df[["venue_lat", "venue_lon", "venue_name", "name", "url"]].drop_duplicates(),
#         get_position=["venue_lon", "venue_lat"],
#         get_radius=100,
#         get_fill_color=[255, 102, 102],
#         pickable=True
#     )
#
#     view = pdk.ViewState(
#         latitude=59.33,
#         longitude=18.07,
#         zoom=12
#     )
#
#     return pdk.Deck(
#         layers=[layer],
#         initial_view_state=view,
#         tooltip={
#             "html": f"""
#                 <b>{{name}}</b><br>
#                 📍 {{venue_name}}<br>
#                 <a href="{{url}}" target="_blank"
#                    style="color: {link_color};">
#                    Buy tickets →
#                 </a>
#             """,
#             "style": {
#                 "backgroundColor": "#1F0322",
#                 "color": "white",
#                 "padding": "10px",
#                 "borderRadius": "6px",
#                 "fontSize": "13px"
#             }
#         },
#         map_style="mapbox://styles/mapbox/navigation-night-v1",
#         api_keys={"mapbox": mapbox_token}
#     )