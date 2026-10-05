import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


# 1. Import the data
df = pd.read_csv('cardio_train.csv')

# 2. Add 'overweight' column
df['overweight'] = (
    df['weight'] / ((df['height'] / 100) ** 2) > 25
).astype(int)

# 3. Normalize cholesterol and gluc (0 = good, 1 = bad)
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)


def draw_cat_plot():
    # 5. Melt into long format
    df_cat = pd.melt(
        df,
        id_vars=['cardio'],
        value_vars=['cholesterol', 'gluc', 'smoke', 'alco',
                    'active', 'overweight']
    )

    # 6. Group and count
    df_cat = (
        df_cat.groupby(['cardio', 'variable', 'value'])
               .size()
               .reset_index(name='total')
    )

    # 7. Draw categorical plot
    fig = sns.catplot(
        x='variable',
        y='total',
        hue='value',
        col='cardio',
        data=df_cat,
        kind='bar'
    ).fig

    # 8. Save
    fig.savefig('catplot.png')
    return fig


def draw_heat_map():
    # 11. Clean data
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # 12. Correlation matrix
    corr = df_heat.corr()

    # 13. Upper-triangle mask
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14. Set up figure
    fig, ax = plt.subplots(figsize=(12, 10))

    # 15. Heatmap
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt='.1f',
        center=0,
        square=True,
        linewidths=0.5,
        cbar_kws={'shrink': 0.5},
        ax=ax
    )

    # 16. Save
    fig.savefig('heatmap.png')
    return fig