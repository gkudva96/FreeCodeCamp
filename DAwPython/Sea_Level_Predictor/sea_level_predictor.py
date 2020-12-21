# Importing Libraries
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

# Function definition to draw the necessary plots
def draw_plot():

    # Reading data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Creating scatter plot
    plt.figure()
    plt.scatter(df['Year'], df.iloc[:, 1], s = 2)

    # Creating first line of best fit
    extended_years = np.arange(1880, 2050, 1)
    slope1, intercept1, _, _, _ = linregress(df['Year'], df.iloc[:, 1])
    plt.plot(extended_years, slope1 * extended_years + intercept1, 'r', label = 'Best Fit 1')

    # Creating second line of best fit
    slope2, intercept2, _, _, _ = linregress(df.iloc[120 : , 0], df.iloc[120 : , 1])
    plt.plot(extended_years[120:], slope2 * extended_years[120:] + intercept2, 'g', label = 'Best Fit 2')

    # Adding labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.legend()
    
    # Saving plot and returning data for testing
    plt.savefig('sea_level_plot.png')
    return plt.gca()