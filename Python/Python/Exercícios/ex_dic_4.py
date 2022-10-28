# (4) Crie um dicionário vazio e o complete com uma chave para cada dia da semana, 
# tendo como seu valor uma lista com as aulas que você tem nesse dia.

dic_calendario = {}
qntd_dias = int(input("Informe a quantidade de dias que deseja: "))
i = 1

while i <= qntd_dias:
    print("Dia",i,"da semana!")
    validar_aula = int(input("Opções abaixo\n1 - Sim\n2 - Não\nVocê tem aula nesse dia? "))
    
    while validar_aula == 1:
        aula = input("Informe o nome da aula: ")
        opcMaisAula = int(input("Tem mais aula? (1- Sim, 2 - Não): "))
        dic_calendario[i] = [aula]

        if validar_aula == 2:
            dic_calendario[i] = ["Não Tem aula!"]
            print("\nFim do dia",i,"\n")
        else:
            print("Valor inválido!")
            opc = int(input("\nOpções abaixo\n1 - Sim\n2 - Não\nVocê tem mais aula dia",i,": "))
    i += 1
i += 1
print(dic_calendario)

