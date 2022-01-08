import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
import random
import statistics
import csv

df = pd.read_csv('medium_data.csv')
data = df['reading_time'].tolist()
fig = ff.create_distplot([data], ['reading_time'], show_hist = False)
fig.show()

population_mean = statistics.mean(data)
print("Mean = ", population_mean)
population_standarddeviation = statistics.stdev(data)
print("Standard deviation = ", population_standarddeviation)

dataset = []
for i in range(0,1000):
  random_index = random.randint(0,len(data))
  value = data[random_index]
  dataset.append(value)

mean_list = []

for i in range(0,1000):
  set_of_means = random_set_of_mean(100)
  mean_list.append(set_of_means)

mean = statistics.mean(mean_list)
standarddeviation = statistics.stdev(mean_list)
print("mean of population = ", mean)
print("standard deviation of population = ", standarddeviation)
