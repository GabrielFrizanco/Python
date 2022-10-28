# média de nota com while
nome = input("Digite o nome: ")
n1 = float (input("Digite a Nota 1: "))
n2 = float (input("Digite a Nota 2: "))

while (n1 > 10 or n2 > 10):
  n1 = float (input("Nota errada! Digite novamente a nota 1: "))
  n2 = float (input("Nota errada! Digite novamente a nota 2: "))

media = (n1 + n2)/2

print(nome,"Sua média final:", media)

if media >= 7:
  print("Aprovado!")
else:
  print("Exame!")