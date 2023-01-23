lista = [1, 2, 3, 4, 5]
print(lista)
x = 0
soma = 0
while x < 5:
  soma += lista[x]
  print("{",soma,"}")
  x += 1

# ler uma lista
teste = int(input("informe um número: "))
lista = []

i = 1
while i <= teste :
  infoTrans = input("Insira um transporte: ")
  lista.append(infoTrans)
  i = i + 1
lista