# FAÇA O CALCULADO DA MÉDIA DOS ALUNOS E MOSTRE A SITUAÇÃO DELES, 
# SENDO ASSIM SÓ ACEITANDO APROVADO(A) E REPROVADO(A)
# P.S: EXERCÍCIO DE FIXAÇÃO DA BIBLIOTECA PANDAS

import pandas as pd
from IPython.display import display

df = pd.read_excel("Escola.xlsx")

#display(df)

# fazendo a média
df["Média"] = (df["N1"] + df["N2"])/2

# se média for >=5 aprovado(a), senão reprovado(a)
df.loc[df["Média"]>= 5, "Situação"] = "Aprovado(a)"
df.loc[df["Média"]< 5, "Situação"] = "Reprovado(a)"

# colocando os dados em outro arquivo
df.to_excel("Escola_Atualizado.xlsx", index=False)
