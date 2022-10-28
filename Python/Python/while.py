# n = int(input("Tabuada? "))
# i = 1

# while i <= 10:
#     resultado = n * i
#     print(n,"*",i,"=",resultado)
#     i += 1



continua = "S"
while continua == "S" or continua == "s":
    m = int(input("Multiplo? "))
    i = 0
    while i <= 100:
        print(i)
        i += m
    continua = input("Continua S/N? ")
print("Fim!")
