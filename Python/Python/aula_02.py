nome = input("Digite o seu nome: ")
anoNasc = int(input("Informe o seu ano de nascimento: "))
anoAtual = int(input("Informe o ano atual: "))
idade = (anoAtual - anoNasc)


if idade >= 18:
  print("+18")

else:
  print("-18")

print("Olá,", nome, "sua idade é:", idade)




nome = input("Informe o seu nome: ")
altura = float(input("Informe sua altura: "))
peso = int(input("Informe o seu peso: "))

imc = (peso/(altura * altura))

if imc < 18.5:
  print("ABAIXO DO PESO!")

elif imc > 18.5 and imc < 24.9:
  print("PESO NORMAL!")

elif imc > 25 and imc < 29.9:
  print("SOBREPESO I!")

elif imc > 30 and imc < 39.9:
  print("OBESIDADE II!")

else:
  print("OBESIDADE GRAVE III!")




precoProd = float(input("Digite o preço do produto: "))
opcao = int(input("Deseja incluir desconto? (1 - Sim/2 - Não): "))

while opcao != 1 and opcao != 2:
  opcao = int(input("Opção inválida! Digite novamente (1- Sim/2- Não): "))

if opcao == 1:
  desconto = int(input("Deseja incluir quanto de desconto?: "))
  descProd = (precoProd * desconto/100)
  print("Preço do produto (",desconto,"% de Desconto):",descProd)
else:
  print("Preço do produto sem desconto:",precoProd)




nome = input("Digite o seu nome: ")
anoNasc = int(input("Informe o seu ano de nascimento: "))
anoAtual = int(input("Informe o ano atual: "))

# idade da pessoa em anos
idade = anoAtual - anoNasc
idadeEmMeses = idade * 12
idadeEmDias = idade * 365
idadeEmHoras = idadeEmDias * 24
idadeEmMinutos = idadeEmHoras * 60
idadeEmSegundos = idadeEmHoras * 60
print("Idade Em Anos: ", idade)
print("Idade Em Meses: ", idadeEmMeses)
print("Idade Em Dias: ", idadeEmDias)
print("Idade Em Horas: ", idadeEmHoras)
print("Idade Em Minutos: ", idadeEmMinutos)
print("Idade Em Segundos: ", idadeEmSegundos)