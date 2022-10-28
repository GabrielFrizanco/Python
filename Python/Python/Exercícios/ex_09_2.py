# Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. 
# Pergunte a quantidade de KWH consumida e o tipo de instalação, sendo, 
# R para residências , I para Indústrias e C para Comércios. 
# Calcule o preço a pagar de acordo com a tabela a seguir;

# Tipo                  Faixa (kWh)    Preço (R$)
# Residencial           até 500         0,40  
#                       acima de 500    0,65

# Comercial             até 1000        0,55
#                       acima 1000      0,60

# Industrial            até 5000        0,55
#                       acima de 5000   0,60

kwh = (float(input("Informe a quantidade de KWH consumido: ")))
print("|===Local onde foi gasto os KWH===|\n1 - Residencial\n2 - Comercial\n3 - Industrial")
local = (int(input("Informe um dos números: ")))

if (local == 1):
    if(kwh >= 0 and kwh <= 500):
        custoAPagar = (kwh*0.40)
    elif(kwh > 500):
        custoAPagar = (kwh*0.65)

if (local == 2):
    if(kwh >= 1000 and kwh <= 1000):
        custoAPagar = (kwh*0.55)
    elif(kwh > 1000):
        custoAPagar = (kwh*0.55)

if(local == 3):
    if(kwh >= 5000 and kwh <= 5000):
        custoAPagar = (kwh*0.55)
    elif(kwh > 5000):
        custoAPagar = (kwh*0.60)