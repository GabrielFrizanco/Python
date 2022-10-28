# sistema de compras

# nome = input("Informe o seu nome: ")
lista_produtos = {}


qntd = int(input("Informe a quantidade de produto que deseja inserir: "))

i = 0

while i < qntd:
    cod_prod = int(input("Informe o código do produto: "))
    nome_prod = input("Informe o nome do produto: ")
    preco_prod = float(input("Informe o preço do produto: "))
    quantd_prod = int(input("Informe a quantidade do produto: "))
    valor_total = preco_prod * quantd_prod
        
    lista_produtos[cod_prod] = [nome_prod, preco_prod, quantd_prod, valor_total]

    i += 1

print("1 - Sim\n2 - Não")
opc = int(input("Deseja consultar algum produto? "))

if opc == 1:
    codigo = int(input("Informe o código do produto: "))
    if (codigo in lista_produtos):
        print("Produto está cadastrado!\n", lista_produtos[codigo])
    else:
        print("Produto não cadastrado!")





# for produtos in lista_produtos:
#     print(produtos)

# pegando as keys
# print(lista_produtos.keys())

# pegando os valores
# for produtos in lista_produtos:
#     listProd = lista_produtos[produtos]
#     print(listProd)

# tirar um valor (chave)
# lista_produtos.pop("Fone de Ouvido")

# verificar se existe conteúdo de chave e valor
# if "Fone de Ouvido" in lista_produtos:
#     print("Existe!")
# else:
#     print("Não existe!")

# if 30.00 in lista_produtos.values():
#     print("Existe!")
# else:
#     print("Não existe!")
# print(lista_produtos)