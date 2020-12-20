# Importing Libraries
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Defining a dictionary to map month number to month name
months = {'01' : 'January', '02' : 'February', '03' : 'March', '04' : 'April', \
'05' : 'May', '06' : 'June', '07' : 'July', '08' : 'August', '09' : 'September', \
'10' : 'October', '11' : 'November', '12' : 'December'}

# Importing data
# Setting the 'date' column as the index
# Parsing the 'date' values as datetime objects
df = pd.read_csv('fcc-forum-pageviews.csv', index_col = 'date', parse_dates = True)

# Cleaning data
# Removing rows where number of views are in the top 2.5%
# Removing rows where number of views are in the bottom 2.5%
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]

# Function definition for drawing a line plot
def draw_line_plot():
  # Creating a copy of the dataframe
  df_line_plot = df.copy()
  # Plotting a line plot between the dates and page views
  fig1, ax = plt.subplots()
  ax.plot(df_line_plot.index, df_line_plot['value'], 'r')
  # Setting the title, xlabel, and ylabel for the plot
  ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
  ax.set_xlabel('Date')
  ax.set_ylabel('Page Views')
  # Setting the height and width of the figure
  fig1.set_figheight(6)
  fig1.set_figwidth(20)
  # Saving image and returning figure
  fig1.savefig('line_plot.png')
  return fig1

# Function definition for drawing a bar plot
def draw_bar_plot():
    # Creating a copy of the dataframe
    df_bar = df.copy()
    # Resetting the index
    df_bar = df_bar.reset_index()
    # Converting from datetime to string
    df_bar = df_bar.astype({"date" : str})
    # Modifying the dataframe for the bar plot
    df_bar['Years'] = df_bar['date'].apply(lambda x : x.split('-')[0])
    df_bar['Months'] = df_bar['date'].apply(lambda x : months[x.split('-')[1]])
    df_bar = pd.melt(df_bar, id_vars = ['Years', 'Months'], value_vars = ['value'], value_name = 'view_count')
    df_bar = df_bar.groupby(['Years', 'Months'], as_index = False).mean().rename(columns = {"view_count" : "Average Page Views"})
    # Drawing bar plot
    fig2 = sns.catplot(x = 'Years', y = 'Average Page Views', hue = 'Months', kind = 'bar', data = df_bar).fig
    # Saving image and returning figure
    fig2.savefig('bar_plot.png')
    return fig2

# Function definition for drawing the box plots
def draw_box_plot():
    # Creating a copy of the dataframe
    df_box = df.copy()
    # Resetting the index
    df_box = df_box.reset_index()
    # Converting from datetime to string
    df_box = df_box.astype({"date" : str})
    # Modifying the dataframe for the box plots
    df_box['Year'] = df_box['date'].apply(lambda x : int(x.split('-')[0]))
    df_box['Month'] = df_box['date'].apply(lambda x : months[x.split('-')[1]][0:3])
    df_box['Month_Num'] = df_box['date'].apply(lambda x : int(x.split('-')[1]))
    df_box = df_box.sort_values("Month_Num")
    # Drawing box plots
    fig3, ax = plt.subplots(1, 2)
    sns.boxplot(x = 'Year', y = 'value', ax = ax[0], data = df_box)
    ax[0].title.set_text('Year-wise Box Plot (Trend)')
    ax[0].set_ylabel('Page Views')
    sns.boxplot(x = 'Month', y = 'value', ax = ax[1], data = df_box)
    ax[1].title.set_text('Month-wise Box Plot (Seasonality)')
    ax[1].set_ylabel('Page Views')
    fig3.set_figheight(10)
    fig3.set_figwidth(30)
    # Saving image and returning figure
    fig3.savefig('box_plot.png')
    return fig3