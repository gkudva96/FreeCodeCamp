# Importing Libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Importing data
df = pd.read_csv('medical_examination.csv')

# Adding 'overweight' column
df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2)).map(lambda x : 1 if x > 25 else 0)

# Normalizing data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, making the value 0. If the value is more than 1, making the value 1.
df['cholesterol'] = df['cholesterol'].map(lambda x : 0 if x == 1 else 1)
df['gluc'] = df['gluc'].map(lambda x : 0 if x == 1 else 1)

# Drawing a Categorical Plot using Seaborn
def draw_cat_plot():

    # Creating a DataFrame for categorical plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars = ['cardio'], value_vars = ['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])

    # Grouping and reformatting the data to split it by 'cardio'. Showing the counts of each feature.
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name = "total")

    # Draw the catplot with 'sns.catplot()'
    fig = sns.catplot(x = 'variable', y = 'total', hue = 'value', col = 'cardio', kind = 'bar', data = df_cat).fig

    # Returning the figure
    return fig


# Plotting the Heat Map
def draw_heat_map():

    # Cleaning the data
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & \
    (df['height'] >= (df['height'].quantile(0.025))) & \
    (df['height'] <= (df['height'].quantile(0.975))) & \
    (df['weight'] >= (df['weight'].quantile(0.025))) & \
    (df['weight'] <= (df['weight'].quantile(0.975)))]

    # Calculating the correlation matrix
    corr = df_heat.corr()

    # Generating a mask for the upper triangle
    mask = np.triu(corr)

    # Initializing the figure
    fig, ax = plt.subplots(figsize = (9, 9))

    # Generating the heatmap
    sns.heatmap(corr, annot = True, fmt = '.1f', linewidths = 1, mask = mask, vmax = 0.3, \
        center = 0.09, square = True, cbar_kws = {'shrink' : 0.5})

    # Returning the figure
    return fig