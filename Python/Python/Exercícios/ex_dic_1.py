# (1) Crie um dicionário para armazenar o número e o nome dos meses do ano.

dic_num = {}

num_mes = int(input("Informe a quantidade de mês que deseja adicionar: "))
while num_mes > 12 or num_mes <= 0:
    num_mes = int(input("Não posso adicionar essa quantidade de mês\nTente novamente: "))

i = 1
while i <= num_mes:
    nome_mes = input("Informe o Mês que deseja: ")
    dic_num[i] = nome_mes
    print("\nAdicionado!\n","Número do Mês:",i,"\nMês:",nome_mes,"\n")
    i += 1

print(dic_num)