'''
Лаба номер 8
'''
import pandas as pd
import plotly.express as px
df = pd.read_csv('udemy_courses.csv')
task1 = df.groupby('subject')['price'].mean()
task2 = df.groupby('price')['num_subscribers'].mean()
fig1 = px.bar(task1)
fig1.show()
fig2 = px.line(task2)
fig2.show()
