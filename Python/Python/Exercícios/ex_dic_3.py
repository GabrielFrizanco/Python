# (3) Faça um dicionário para armazenar o nome e celular de sua agenda de contatos.

dic_agenda = {}

qntd_pessoa = int(input("Informe quantas pessoas deseja adicionar na agenda: "))

i = 1
while i <= qntd_pessoa:
    nome = input("Informe o nome da pessoa: ")
    num_pessoa = input("Informe o número da pessoa: ")
    dic_agenda[nome] = num_pessoa

    i+= 1

print(dic_agenda)