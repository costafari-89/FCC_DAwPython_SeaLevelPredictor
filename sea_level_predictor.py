import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv', header = 0, sep = ',', index_col = 0, parse_dates = True)
    
    # Create scatter plot
    fig, axes = plt.subplots(figsize = (12,6))
    plt.scatter(x=df.index.year, y = df['CSIRO Adjusted Sea Level'])
    
    # Create first line of best fit


    # Create second line of best fit


    # Add labels and title
    axes.set_title('Rise in Sea Level')
    axes.set_xlabel('Year')
    axes.set_ylabel('Sea Level (inches)')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
