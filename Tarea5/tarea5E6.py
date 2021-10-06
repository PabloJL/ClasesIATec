lista = list(range(1,11))
suma = 0

for i in lista:
    numero= int(input("Agregar número:\n"))
    lista[i] = numero

    if(numero>0):
        suma += numero

# for s in lista:
#     if(lista[s] >0):
#         suma += lista[s]

print(f'La suma es de: {suma}')