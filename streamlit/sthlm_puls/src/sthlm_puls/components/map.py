import pandas as pd
import folium
from streamlit_folium import st_folium

def events_map(df: pd.DataFrame, focus_venue: str = None):
    coords = df[["venue_lat", "venue_lon"]].dropna().drop_duplicates().values.tolist()

    if not coords:
        location = [59.33, 18.07]
        zoom = 13
    elif len(coords) == 1:
        location = coords[0]
        zoom = 15
    else:
        location = [59.33, 18.07]
        zoom = 13

    m = folium.Map(
        location=location,
        zoom_start=zoom,
        zoom_control=False,
        tiles="OpenStreetMap",
    )

    if len(coords) > 1:
        m.fit_bounds(coords)

    m = folium.Map(
        location=location,
        zoom_start=zoom,
        zoom_control=False,
        tiles="OpenStreetMap",
    )

    for _, row in df[["venue_lat", "venue_lon", "venue_name", "name", "url"]].drop_duplicates().iterrows():
        folium.CircleMarker(
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
