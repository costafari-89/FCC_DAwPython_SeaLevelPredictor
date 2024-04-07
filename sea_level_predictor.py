import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv', header = 0, sep = ',', index_col = 0, parse_dates = True)
    
    # Create scatter plot
    fig, axes = plt.subplots(figsize = (12,6))
    plt.scatter(x=df.index.year, y = df['CSIRO Adjusted Sea Level'])
    plt.xlim(1850, 2075)
    
    
    # Create first line of best fit
    slope, intercept, r, p, se = linregress(x=df.index.year, y=df['CSIRO Adjusted Sea Level'])
    year_index = pd.date_range(start = '1880-01-01', end='2050-01-01', freq='1YS', inclusive ='both')
    plt.plot(year_index.year, slope*year_index.year +intercept, label = 'Best Fit All Data')


    # Create second line of best fit
    df_2000 = df.loc[df.index.year >= 2000]
    slope_2000, intercept_2000, r_2000, p_2000, se_2000 = linregress(x=df_2000.index.year, y=df_2000['CSIRO Adjusted Sea Level'])
    year_index_2000 = pd.date_range(start = '2000-01-01', end = '2050-01-01', freq='1YS', inclusive = 'both')
    plt.plot(year_index_2000.year, slope_2000*year_index_2000.year +intercept_2000, label = 'Best Fit Since 2000')


    # Add labels and title
    plt.legend()
    axes.set_title('Rise in Sea Level')
    axes.set_xlabel('Year')
    axes.set_ylabel('Sea Level (inches)')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
