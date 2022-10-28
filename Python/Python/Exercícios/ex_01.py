# (4) Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar. 
# Você deve poder escolher soma, subtração, multiplicação e divisão. Exiba o resultado da operação solicitada.

n1 = float(input("Informe um valor para o primeiro número: "))
n2 = float(input("Informe um valor para o segundo número: "))

infoOper = input("Informe a operação - (+, -, * e /): ")

if infoOper == "+":
  resultado = n1 + n2

elif infoOper == "-":
  resultado = n1 - n2

elif infoOper == "*":
  resultado = n1 * n2

elif infoOper == "/":
  resultado = (n1/n2)

print("Operção:",n1,infoOper,n2,"\nResultado:", resultado)