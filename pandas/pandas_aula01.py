# importando biblioteca
import pandas as pd
import random
import numpy as np

dataset = pd.read_csv("credit_data.csv") # carregar os dados do arquivo credit_data
dataset.shape # exibir linhas e colunas do arquivo credit_data

dataset2 = pd.read_csv("census.csv") # carregar os dados do arquivo census
dataset2.shape # exibir linhas e colunas do arquivo census

dataset3 = pd.read_csv("autos.csv") # carregar os dados do arquivo autos
dataset3.shape # exibir linhas e colunas do arquivo autos

dataset.head() # mostra os indices e colunas

dataset.columns[0] # exibir colunas ou apenas uma coluna colocando um indice
#Quantidade de linhas e colunas do DataFrame
dataset.shape
#Descrição do Index
dataset.index
#Colunas presentes no DataFrame
dataset.columns
#Contagem de dados não-nulos
dataset.count()

dataset['teste'] = 0 # adicionando uma nova coluna
print(dataset.columns)

# dataset.isnull().sum() # somar todas as colunas

dataset['teste'].dropna() # dropando uma coluna adicionando o indice dela
print(dataset.columns)

# Resumo dos dados:
#Soma dos valores de um DataFrame
dataset.sum()
#Menor valor de um DataFrame
dataset.min()
#Maior valor
dataset.max()
#Index do menor valor
dataset.idmin()
#Index do maior valor
dataset.idmax()
#Resumo estatístico do DataFrame, com quartis, mediana, etc.
dataset.describe()
#Média dos valores
dataset.mean()
#Mediana dos valores
dataset.median()

df = pd.DataFrame({
    'Fname':['Harry','Sally','Paul','Abe','June','Mike','Tom'],
    'Age':[21,34,42,18,24,80,22],
    'Weight': [180, 130, 200, 140, 176, 142, 210],
    'Gender':['M','F','M','M','F','M','M'],
    'State':['Washington','Oregon','California','Washington','Nevada','Texas','Nevada'],
    'Children':[4,1,2,3,0,2,0],
    'Pets':[3,2,2,5,0,1,5]
})
print(df)