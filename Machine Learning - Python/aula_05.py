# tupla
tupla_vazia = ()
tupla_vazia2 = tuple()
tupla1 = (3, 6, 9, 12, 15, 18, 21, 24, 27, 30)
tupla2 = (3, 6, 9, 12, 15, 18, 21, 24, 27, 30, "tupla", (1, 2, 3))
tupla3 = (3, 6, 9, 12, 15, 18, 21, 24, 27, 30, "tupla", [1, 2, 3])
print(tupla_vazia,"\n")
print(tupla_vazia2,"\n")
print(tupla1,"\n")
print(tupla2,"\n")
print(tupla3)
type(tupla2)
len(tupla2)

notas = (8.0, 6.0, 8.0, 9.0, 6.5, 7.5)
print(len(notas)) # ler
print(max(notas)) # valor máximo
print(min(notas)) # valor minimo
print(sum(notas)) #soma de todos os valores
notas.count(8.0) # quantos 8.0 tem

lista = list(notas)
print(lista)
lista.append(11.0)
print(lista)
print(notas)

notas = tuple(lista)
print(notas)
len(notas)

tupla3 = (3, 6, 9, 12, 15, 18, 21, "renato", 27, 30, "tupla", [10, 20, 30])
print(tupla3[7][0])
print(tupla3[7][0:2])
#tupla3 = [11][2] = 100
print()

# dicionário
dic_vazio = {}
dic_vazio2 = dict()
print(dic_vazio2)
dic_estados = {"SP": "São Paulo", "PR" : "Paraná", "MG" : "Minas Gerais"}
print(dic_estados)

dic_produtos = {
    1 : "Caneta",
    200 : "Pen Drive",
    30 : "Caderno",
    4 : "Mouse",
    12 : "Teclado"
 }
print(dic_produtos)


dic_notas_alunos = {
      "Carlos"  : [6.0, 4.0, 8.0],
      "Marcio"  : [8.0, 9.0, 6.0], 
      "Antonio" : [5.5, 7.0, 9.0]
}
print(dic_notas_alunos)

dic_notas_alunos2 = {
      "Carlos"    : {"nota1" : 6.0, "nota2" : 4.0, "nota3" : 8.0 },
      "Marcio"   : {"nota1" : 8.0, "nota2" : 9.0, "nota3" : 6.0 }, 
      "Antonio" : {"nota1" : 5.5, "nota2" : 7.0, "nota3" : 9.0 }
}
print(dic_notas_alunos2["Carlos"])