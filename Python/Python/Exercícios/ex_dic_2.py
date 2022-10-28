# (2) Crie um dicionário para armazenar o número e o nome do dia da semana.

dic_semana = {}

num_semana = int(input("Informe a quantidade de dia para a semana: "))

while num_semana > 7 or num_semana <= 0:
    num_semana = int(input("Número da semana errado!\nDigite novamente: "))

i = 1
while i <= num_semana:
    nome_semana = input("Informe o nome da semana: ")
    dic_semana[i] = nome_semana
    i += 1

print(dic_semana)