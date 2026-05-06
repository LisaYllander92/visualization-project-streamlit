import streamlit as st
import pandas as pd
from datetime import datetime
import duckdb

from sthlm_puls.utils.constants import DATA_PATH
from sthlm_puls.components.weather import fetch_weather_forecast
from sthlm_puls.components.charts import plot_events_weather
from sthlm_puls.components.filters import venue_filter, genre_filter, date_filter
from sthlm_puls.components.kpis import total_events_kpi, unique_venues_kpi, total_events_this_month_kpi


def events_layout():
    st.title("📅 This Week in Stockholm")
    st.markdown("Find the best day to experience Stockholm's cultural scene.")

    # Load data
    weather = fetch_weather_forecast(days=7)
    events = pd.read_csv(DATA_PATH / "events_combined.csv")
    events["date"] = pd.to_datetime(events["date"])

    # Count events per day
    events_per_day = (
        events[events["date"].dt.date.between(
            weather["date"].dt.date.min(),
            weather["date"].dt.date.max()
        )]
        .groupby(events["date"].dt.date)
        .size()
        .reset_index(name="num_events")
    )
    events_per_day["date"] = pd.to_datetime(events_per_day["date"])

    # Merge
    df_merged = weather.merge(events_per_day, on="date", how="left")
    df_merged["num_events"] = df_merged["num_events"].fillna(0).astype(int)

    # Plot
    fig = plot_events_weather(df_merged)
    st.pyplot(fig)

    st.markdown("## *Explore to find what your next event will be*")


    # Filters
    col1,col2, col3 = st.columns(3)
    with col1:
        date_range = date_filter(events)
    with col2:
        venue = venue_filter(events)
    with col3:
        genre = genre_filter(events)


    # Filter table
    filtered = events.copy()

    if venue != "All":
        filtered = filtered[filtered["venue_name"] == venue]

    if genre != "All":
        filtered = filtered[filtered["genre"] == genre]

    if len(date_range) == 2:
        filtered = filtered[
            (filtered["date"].dt.date >= date_range[0]) &
            (filtered["date"].dt.date <= date_range[1])
            ]

    st.dataframe(filtered[["name", "venue_name", "date", "genre"]]
                 .assign(date=filtered["date"].dt.strftime("%y-%m-%d"))
                 .rename(columns={
                    "name": "Event",
                    "venue_name": "Venue",
                    "date": "Date",
                    "genre": "Genre"})
                    .reset_index(drop=True))

    col1, col2, col3 = st.columns(3)

    with col1:
        count = total_events_kpi(filtered, genre)
        st.metric(label=f"Total events ({genre})", value=count)
    with col2:
        count = unique_venues_kpi(filtered, venue)
        st.metric(label=f"Unique venues ({venue})", value=count)

    with col3:
        month_name = datetime.today().strftime("%B")
        st.metric(label=f"Total events in {month_name}", value=total_events_this_month_kpi(events))


if __name__ == "__main__":
    events_layout()