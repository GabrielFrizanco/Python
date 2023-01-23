prim = 1
ult = 1
contador = 3
print(prim)
print(ult)
while contador <= 10:
    prox = prim + ult
    print(prox)
    prim = ult
    ult = prox
    contador += 1
