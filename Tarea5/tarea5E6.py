##E6
lista = list(range(1,11))
suma = 0

for i in lista:
    numero= int(input("Agregar número:\n"))
    lista[i] = numero

    if(numero>0):
        suma += numero

print(f'La suma es de: {suma}')