#E3
import random 

numero = random.randint(0,100)
salir= True

while salir == True:
    numero = random.randint(0,100)
    if(numero%2==1):
        print(f'{numero} es impar')
    else:
        print(f'{numero} es par')

    cortar = input("Desea salir?:").lower()
    if(cortar=="si"):
        salir=False

