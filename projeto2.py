import pandas 
import numpy
import openpyxl
import plotly.express as px

tabela = pandas.read_csv("cancelamentos_sample.csv")

tabela = tabela.drop(columns="CustomerID")

grafico = px.histogram(tabela, x="idade")

grafico.show()