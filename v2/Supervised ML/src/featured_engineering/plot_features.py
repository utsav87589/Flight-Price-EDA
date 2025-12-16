#---------------importing the libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pylab
import scipy.stats as stat


#------------writing the function to check the plot for the individual column
def plot_graphs(df, feature) : 

    #---------first plot, which is a hist plot
    plt.figure(figsize = (12, 4))
    plt.subplot(1, 3, 1)
    plt.title('Hist plot')
    df[feature].hist()
    plt.xlabel("")
    plt.ylabel("")

    #----------second one, which is a qq plot
    plt.subplot(1, 3, 2)
    plt.title('QQ plot')
    stat.probplot(df[feature], dist = 'norm', plot = pylab)
    plt.xlabel("")
    plt.ylabel("")
    
    #----------third plot, box plot
    plt.subplot(1, 3, 3)
    plt.title('Boxplot')
    sns.boxplot(df[feature])
    plt.xlabel("")
    plt.ylabel("")

    plt.show()

#-----------writing the function to plot the box plots for the features after scaling to verify the things
def plot_graphs_post_scaling(df, df_copy, feature) : 

    plt.figure(figsize = (8, 4))
    plt.subplot(1, 2, 1)
    plt.title('Boxplot : df')
    sns.boxplot(df[feature])
    plt.xlabel("")
    plt.ylabel("")

    plt.subplot(1, 2, 2)
    plt.title('Boxplot : df_copy')
    sns.boxplot(df_copy[feature])
    plt.xlabel("")
    plt.ylabel("")


    plt.show()