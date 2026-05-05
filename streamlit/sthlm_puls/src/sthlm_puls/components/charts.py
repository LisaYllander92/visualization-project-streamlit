import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.font_manager import FontProperties
import numpy as np
import pandas as pd
from sthlm_puls.utils.constants import COLORS


def plot_events_weather(df_merged: pd.DataFrame) -> plt.Figure:

    bar_colors = [
        COLORS["pink"] if row["temp_max"] == df_merged["temp_max"].max()
        else COLORS["gray_light"]
        for _, row in df_merged.iterrows()
    ]

    fig, ax = plt.subplots(figsize=(8, 3))
    fig.patch.set_facecolor(COLORS["blue_light"])
    ax.set_facecolor(COLORS["blue_light"])

    x = np.arange(len(df_merged))
    ax.bar(x, df_merged["num_events"], color=bar_colors,
           width=0.6, edgecolor="none", zorder=2)

    emoji_font = FontProperties(family="Segoe UI Emoji")
    y_max = df_merged["num_events"].max()

    for i, row in df_merged.iterrows():
        ax.text(i, row["num_events"] + y_max * 0.06,
                row["icon"], ha="left", va="bottom",
                fontsize=14, fontproperties=emoji_font)
        ax.text(i, row["num_events"] + y_max * 0.16,
                f"{int(row['temp_max'])}°",
                ha="right", va="bottom", fontsize=8,
                color=COLORS["blue_dark"])

    legend_items = [
        mpatches.Patch(color=COLORS["pink"], label="Warmest day"),
        mpatches.Patch(color=COLORS["gray_light"], label="Other days"),
    ]

    ax.legend(handles=legend_items, fontsize=8, frameon=False,
              labelcolor=COLORS["blue_dark"], loc="upper left")

    ax.set_xticks(x)
    ax.set_xticklabels(df_merged["day_label"], fontsize=9, color=COLORS["blue_dark"])
    ax.set_ylabel("Number of events", fontsize=7, color=COLORS["blue_dark"])
    ax.yaxis.set_label_coords(-0.06, 0.5)
    ax.tick_params(axis="both", length=0, colors=COLORS["blue_dark"])
    ax.spines[["top", "right", "left"]].set_visible(False)
    ax.spines["bottom"].set_color(COLORS["blue_dark"])
    ax.set_ylim(0, y_max * 1.55)
    ax.yaxis.grid(True, color=COLORS["gray_1"], linewidth=0.5, linestyle='--')
    ax.set_axisbelow(True)
    ax.set_title(
        "This week's cultural events in Stockholm — pick the right day",
        loc="left", fontsize=12, fontweight="bold",
        color=COLORS["gray_3"], pad=20
    )
    ax.set_xlabel("Day", fontsize=7, color=COLORS["blue_dark"])
    ax.xaxis.set_label_coords(0.5, -0.1)

    fig.tight_layout()
    return fig



def plot_events_weekday(df: pd.DataFrame):
    # df = pd.read_csv('../streamlit/sthlm_puls/src/sthlm_puls/assets/data/events_combined.csv')

# Måndag överst i listan = måndag nederst i barh, söndag överst
    day_order  = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    day_labels = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    day_counts = df['day_of_week'].value_counts().reindex(day_order).fillna(0)
    total = day_counts.sum()
    pct = (day_counts / total * 100).round(1)

    fig, ax = plt.subplots(figsize=(8, 3))
    fig.patch.set_facecolor(COLORS["blue_light"])
    ax.set_facecolor(COLORS["blue_light"])

    ax.plot(day_labels, pct.values, color=COLORS["pink"], linewidth=2.5,
            marker='o', markersize=7, markerfacecolor='white',
            markeredgecolor=COLORS["pink"], markeredgewidth=2)
    ax.fill_between(day_labels, pct.values, alpha=0.1, color=COLORS["pink"])

    ax.spines[['top', 'right', 'left']].set_visible(False)
    ax.spines['bottom'].set_color(COLORS["gray_1"])
    ax.tick_params(colors=COLORS["blue_dark"], labelsize=10, length=0, pad=5)
    ax.set_xlabel('shares of events (%)', color=COLORS["blue_dark"], fontsize=7)
    ax.yaxis.grid(True, color=COLORS["gray_1"], linewidth=0.5, linestyle='--')
    ax.set_axisbelow(True)

    ax.set_title(
    'Stockholm is a weekend city – saturday dominates',
    loc='left',
    color=COLORS["gray_3"],
    fontsize=12,
    fontweight="bold",
    pad=20
    )

    fig.tight_layout()
    return fig