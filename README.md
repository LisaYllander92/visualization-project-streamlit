# STHLMs Puls — Stockholm Events Visualization

A data engineering and visualization project that aggregates events, museums 
and cultural activities in Stockholm from multiple sources. Built as part of 
a collaborative school project together with UX25.

## Project Overview

The goal is to collect, clean and visualize data about what's happening in 
Stockholm — concerts, theatre, exhibitions, museums and more — presented 
through an interactive Power BI dashboard and data storytelling graphs.

## Power BI Presentation: STHLMs Puls
*Experience the result of five weeks of intensive development, where data meets design in a finished product.*

[![STHLMs PULS Demo](https://img.youtube.com/vi/7UbjM1A4YBI/0.jpg)](https://www.youtube.com/watch?v=7UbjM1A4YBI)

### Explore the Interactive Dashboard
Want to dive into the data yourself? You are more than welcome to explore the live version of the app via the link below.\
A small heads-up: We’ve really pushed the boundaries of what’s possible in Power BI for this project.\
Since this was our first time working with the platform, you might encounter a few minor bugs or performance quirks. We like to think of them as "charms of development"!

[Click here to explore the STHMLs Puls app](https://app.powerbi.com/Redirect?action=OpenApp&appId=28b6d6de-329e-4fe3-922f-bec9975c8e3c&ctid=735058e3-0e46-46ce-a1d5-c0b0a68980db&redirectedFromSignup=1&experience=power-bi)

## Data Sources

| Source | Type | Content |
|--------|------|---------|
| Ticketmaster Discovery API | REST API | Events, concerts, sport, theatre |
| VisitStockholm | Web scrape/API | Cultural events, exhibitions, guided tours |
| Fasching | Custom fetch | Jazz & club events |
| Berns | Custom fetch | Music & nightlife events |
| Google Places API | REST API | Museums, addresses, opening hours, ratings |
| Open-Meteo API | REST API | Weather forecast for Stockholm |

## Project Structure

```
visualization-project-streamlit/
├── api/                # API integrations and data fetching logic
├── data/               # Data storage
│   ├── output/         # Processed data files ready for visualization
│   └── raw/            # Original, unmodified source data
├── eda/                # Exploratory Data Analysis notebooks
│   ├── eda_lisa.ipynb  
│   ├── eda_rickard.ipynb
│   ├── eda_dennis.ipynb
│   └── eda_mossad.ipynb
├── streamlit/          # Source code for the Streamlit application
├── .env                # Environment variables (e.g., API keys)
├── .gitignore          # Files and folders to be ignored by Git
├── pyproject.toml      # Project metadata and Python dependencies
├── README.md           # Project documentation
└── uv.lock             # Deterministic lockfile for package versions
```


## Setup

### 1. Clone the repo
```bash
git clone https://github.com/rickardgarnau-byte/visualization-project-streamlit.git
cd visualization-project-streamlit
```

### 2. Install dependencies
```bash
uv sync
```

### 3. Add API keys
- Create a `.env` file in the project root:
- TICKETMASTER_KEY=your_key_here
- GOOGLE_PLACES_KEY=your_key_here

### 4. Fetch raw data

- uv run all api/fetch files

# Clean and merge
- uv run api/api_clean_visitstockholm.py
- uv run api/merge_events.py

## API Setup

| API | Where to get key |
|-----|-----------------|
| Ticketmaster | developer.ticketmaster.com |
| Visit Stockholm | https://api.visitstockholm.com/ |
| Google Places (New) | console.cloud.google.com → Enable "Places API (New)" |
| Open-Meteo | No key needed — free and open |

## Output Data

| File | Description |
|------|-------------|
| events_full_year.csv | All Stockholm events from Ticketmaster |
| visitstockholm_clean.csv | Cleaned VisitStockholm events |
| events_combined.csv | Merged events from all sources (~1200 events) |
| stockholm_museums.csv | Museums with address, opening hours, rating |
| museum_activity.csv | Museums with popularity index and free admission flag |

CSV files are excluded from Git via `.gitignore`.

## Deliverables

- [x] EDA per team member (pandas + duckdb)
- [x] Power BI dashboard with KPIs, filters, bar charts and pie charts
- [x] Published Power BI dashboard
- [x] Min. 2 data storytelling graphs in matplotlib
- [x] Streamlit dashboard

## Known Data Quality Issues

- VisitStockholm API uses "Jazz & Blues" as default genre for unclassified 
  music events. We handle this with a custom `assign_genre()` function that 
  reclassifies events based on event name.
- VisitStockholm events lack time data (only date available).

## Team

| Name | Role |
|------|------|
| Rickard | Startsida, Scenkonst, Nattliv, data pipeline |
| Lisa | Museum, semantic model, data pipeline |
| Dennis | Musik |
| Mossad | Övrigt |

> Streamlit dashboard developed by Lisa and Rickard.
- [**Explore the Streamlit Documentation & Source Code →**](./streamlit/sthlm_puls/src/sthlm_puls/README.md)

## Status

Complete — data collection, cleaning, EDA, Power BI and Streamlit dashboard done.
