# dicionário

# dic_vazio = {}
# dic_vazio2 = dict()

# dic_estados = {"SP": "São Paulo", 
#                "PR": "Paraná", 
#                "MG": "Minas Gerais"}

# print(dic_vazio,"\n",dic_vazio2,"\n",dic_estados)

# dic_produtos = {1: "Caneta",
#                 200: "Pen Drive",
#                 30: "Caderno",
#                 4: "Mouse",
#                 12: "Teclado"}
# print(dic_produtos)

# print(dic_produtos[4])


# dic_notas_alunos = {
#       "Carlos": [6.0, 4.0, 8.0],
#       "Marcio": [8.0, 9.0, 6.0], 
#       "Antonio": [5.5, 7.0, 9.0]}
# print(dic_notas_alunos)

# dic_notas_alunos2 = {
#       "Carlos": {"nota1" : 6.0, "nota2" : 4.0, "nota3" : 8.0 },
#       "Marcio": {"nota1" : 8.0, "nota2" : 9.0, "nota3" : 6.0 }, 
#       "Antonio": {"nota1" : 5.5, "nota2" : 7.0, "nota3" : 9.0 }}
# print( dic_notas_alunos2["Carlos"])

dic_notas = {}
qntdPessoa = int(input("Quantas pessoas deseja adicionar: "))
i = 0

while i < qntdPessoa:
    nome = input("Informe o nome: ")
    n1 = float(input("Informe a nota 1: "))
    n2 = float(input("Informe a nota 2: "))
    n3 = float(input("Informe a nota 3: "))
    n4 = float(input("Informe a nota 4: "))

    media = (n1+n2+n3+n4)/4

    dic_notas[nome] = {"Nota 1": n1, "Nota 2:": n2, "Nota 3": n3, "Nota 4": n4, "Média": media}
    i = i + 1
print(dic_notas)
print("Lista de pessoas: ", dic_notas.keys())



