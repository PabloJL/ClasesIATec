#E4
import random 
listNumeros = []

seguir= True
suma=0

while seguir == True:
    numero = random.randint(0,100)
    listNumeros.append(numero)
    print(numero)
    
    cortar = input("¿Desea seguir sumando números?:").lower()
    if(cortar=="no"):
        seguir=False
        suma = sum(listNumeros)
        print(f'La suma total es de: {suma}')

