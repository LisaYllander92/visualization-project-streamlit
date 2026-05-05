# STHLMs PULS 🎭

A data-driven cultural guide for Stockholm — helping you discover events, plan around the weather, and explore the city's cultural scene.

## About

STHLMs PULS combines event data from multiple sources with real-time weather forecasts to help culturally curious Stockholmers find the best time to head out.

This streamlit dashboard is built as a extension of a group project that we did with UX.

## Features

- 📅 **This Week** — daily event counts combined with a 7-day weather forecast, highlighting the warmest day of the week
- 📊 **Events** — browse and filter cultural events by genre, venue and date
- 🗃️ **Raw Data** — explore the underlying dataset

## Data Sources

| Source | Type |
|---|---|
| Ticketmaster API | Concerts, sports & entertainment |
| VisitStockholm | Cultural events & exhibitions |
| Fasching | Jazz & club events |
| Berns | Club & live events |
| Open-Meteo API | Weather forecast (no API key required) |

## Project Structure
```
streamlit/
└── sthlm_puls/
└── src/
└── sthlm_puls/
├── components/
│   ├── charts.py       # Matplotlib visualizations
│   ├── kpis.py         # KPI components
│   └── weather.py      # Weather fetch & processing
├── pages/
│   ├── home.py         # Landing page
│   ├── events.py       # Events + weather chart
│   └── raw_data.py     # Raw data explorer
├── assets/
│   ├── data/           # CSV files
│   ├── image/          # Images
│   ├── markdown/       # Page intro texts
│   └── style/          # CSS
└── utils/
├── constants.py    # Paths and color palette
└── helpers.py      # Utility functions
```

## Getting Started

**Requirements:** Python 3.11+, [uv](https://github.com/astral-sh/uv)

**Install dependencies:**
```bash
uv sync
```

**Run the app:**
```bash
cd streamlit/sthlm_puls/src/sthlm_puls
uv run streamlit run app.py
```

## Color Palette

| Name | Hex |
|---|---|
| Pink | `#FF6666` |
| Purple 1 | `#777DA7` |
| Purple 2 | `#1F0322` |
| Blue Dark | `#2E4057` |
| Gray Light | `#D5D8DC` |

## Contributors

- Lisa Yllander
- Rickard Garnau