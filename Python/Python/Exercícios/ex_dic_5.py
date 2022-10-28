# (5) Crie um dicionário para armazenar o nome, celular1, celular2 e email  de pelo menos 10 contatos de sua agenda.

dic_agenda = {}
print("Bem-Vindo(a)!")
qntd_pessoa = int(input("Informe a quantidade de pessoa que deseja adicionar na sua agenda: "))

i = 1
while i <= qntd_pessoa:
    nome = input("Informe o nome da pessoa: ")
    celular1 = input("Informe o número de celular/telefone da pessoa: ")
    opc = int(input("Deseja colocar outro número? (1 - Sim, 2 - Não)? "))
    
    if opc == 1:
        celular2 = input("Informe outro número de celular/telefone da pessoa: ")
    elif opc == 2:
        celular2 = "null"
  
    email = input("Informe o e-mail da pessoa: ")
    dic_agenda[i] = [nome, celular1, celular2, email]
    
    i += 1

print(dic_agenda)