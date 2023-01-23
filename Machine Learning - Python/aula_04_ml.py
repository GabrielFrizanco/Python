# lista
lista = ["Arroz", "Feijão", "Carne", "Macarrão", "Salada"]
v = lista
print(v)

v[0] = 100

print(v)

lista2 = [10, 20, 30, 40, 50]
v2 = lista2[:] # copia
v2[0] = 700
print(lista2)
print(v2)

lista3 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

print(lista3[2:-2])

lista4 = [12, 9, 5]
len(lista4) # ler

lista5 = [1,2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista5)

del lista5[2]
lista5[2] = "null"
print(lista5)

produto1 = ["Maçã", 10, 2.00]
produto2 = ["Pera", 5, 1.75]
produto3 = ["Laranja", 12, 0.50]
compras = [produto1, produto2, produto3]
print(compras)

# adicionar outra lista
notas1 = [10, 9, 5, 9, 6.5, 7]
notas2 = [3, 2.5, 1]
notas1.extend(notas2)
print(notas1)

listaConv = ["João",
             "Fábio",
             "Bernardo", 
             "Higor", 
             "Amanda", 
             "Fabiana"]

len(listaConv)