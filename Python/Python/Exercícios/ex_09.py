# Escreva um programa que pergunte a velocidade do carro de um usuário. 
# Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado, neste caso, 
# exiba o valor da multa, cobrando R$ 5,00 por Km acima de 80 Km/h.

veloCarro = int(input("Informe a velocidade do carro: "))

if veloCarro > 80:
    multaPagar = (veloCarro-80)*5.00
    print("Veículo ultrapassou os 80 km/h!\nMultado! Sua velocidade foi:",veloCarro,"km/h\nValor da multa: R$",multaPagar)
else:
    print("Velocidade do veículo não ultrapassou!\nSua velocidade: ",veloCarro,"km/h")
