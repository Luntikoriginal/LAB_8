'''
Лаба номер 8
'''
import pandas as pd
import plotly.express as px
d = pd.read_csv('udemy_courses.csv')
task1 = d.groupby('subject')['price'].mean()
task2 = d.groupby('price')['num_subscribers'].mean()
fig1 = px.bar(task1)
fig1.show()
fig2 = px.line(task2)
fig2.show()
