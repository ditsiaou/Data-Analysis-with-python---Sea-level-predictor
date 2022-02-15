import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import sys
import numpy as np

def draw_plot():
    # Read data from file
    df=pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots()
    y = df["CSIRO Adjusted Sea Level"]
    df=df.set_index(['Year'])
    plt.scatter(df.index,y)
    # Create first line of best fit
    res1=linregress(df.index,y)
    #(slope, intercept, rvalue, pvalue, stderr) = linregress(x,y)
    x1=pd.DataFrame(list(range(1880,2051)))
    y_pred1=res1[0]*x1 +res1[1]
    plt.plot(x1[0],y_pred1[0],'r')

    # Create second line of best fit
    df_index_2=pd.DataFrame(df.index).tail(14)
    y_2=pd.DataFrame(y).tail(14)
    res2=linregress(df_index_2['Year'],y_2["CSIRO Adjusted Sea Level"])
    x2=pd.DataFrame(list(range(2000,2051)))
    y_pred2=res2[0]*x2 +res2[1]
    plt.plot(x2[0],y_pred2[0],'g')

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()