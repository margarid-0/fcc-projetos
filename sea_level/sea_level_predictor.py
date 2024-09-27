import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
df = pd.read_csv('epa-sea-level.csv')

def draw_plot():
    fig, ax = plt.subplots()

    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = pd.Series([i for i in range(1880, 2051)])
    sea_levels_extended = intercept + slope * years_extended
    ax.plot(years_extended, sea_levels_extended, 'r', label='Linha de ajuste - todos os dados')

    recent_df = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(recent_df['Year'], recent_df['CSIRO Adjusted Sea Level'])
    years_recent = pd.Series([i for i in range(2000, 2051)])
    sea_levels_recent = intercept_recent + slope_recent * years_recent
    ax.plot(years_recent, sea_levels_recent, 'g', label='Linha de ajuste - desde 2000')

    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')

    ax.legend()

    plt.savefig('sea_level_plot.png')

    return ax