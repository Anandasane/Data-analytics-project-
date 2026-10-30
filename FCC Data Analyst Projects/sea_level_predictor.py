import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.scatter(
        df['Year'],
        df['CSIRO Adjusted Sea Level'],
        color='steelblue',
        s=15,
        label='Original Data'
    )

    # First line of best fit — full dataset (1880 → 2050)
    res_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_all = np.arange(df['Year'].min(), 2051)
    ax.plot(
        years_all,
        res_all.intercept + res_all.slope * years_all,
        color='red',
        label='Best Fit (1880 → 2050)'
    )

    # Second line of best fit — from 2000 onwards
    df_recent = df[df['Year'] >= 2000]
    res_recent = linregress(
        df_recent['Year'],
        df_recent['CSIRO Adjusted Sea Level']
    )
    years_recent = np.arange(2000, 2051)
    ax.plot(
        years_recent,
        res_recent.intercept + res_recent.slope * years_recent,
        color='green',
        label='Best Fit (2000 → 2050)'
    )

    # Labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    ax.legend()

    # Save and return
    fig.savefig('sea_level_plot.png')
    return fig