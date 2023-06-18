import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
import csv
import statistics
import random

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()

def random_set_of_mean(counter):    
    data_set = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data))
        value = data[random_index]
        data_set.append(value)
    Mean = statistics.mean(data_set)
    return Mean

def setup():
    meanList = []
    for i in range(0,100):
        mean_set = random_set_of_mean(30)
        meanList.append(mean_set)
    show_fig(meanList)

def show_fig(meanList):
    df = meanList
    fig = ff.create_distplot([df],["Reading time"],show_hist=False)
    fig.show()

setup()