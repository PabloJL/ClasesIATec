# E4
import operator
seguir= True

def opertations(a,b,operation):
    if(operation == 1):
        print(f'La suma de {a} + {b} es {operator.add(a,b)}')
    elif(operation == 2):
        print(f'La resta de {a} - {b} es {operator.sub(a,b)}')
    elif(operation == 3):
        print(f'La multiplicación de {a} * {b} es {operator.mul(a,b)}')
    elif(operation == 4):
        print(f'La división de {a} / {b} es de {operator.truediv(a,b)}')


while seguir == True:
    print("1:Suma.\n2:Resta.\n3:Multiplicación.\n4:División")
    opcion = int(input("Elija una opción del 1 al 4: "))
    
    if(opcion == 1):
        print("Suma")
        a= int(input("Valor 1: "))
        b= int(input("Valor 2: "))
        opertations(a,b,opcion)
    elif(opcion==2):
        print("Resta")
        a= int(input("Valor 1: "))
        b= int(input("Valor 2: "))
        opertations(a,b,opcion)
    elif(opcion==3):
        print("Multiplicación")
        a= int(input("Valor 1: "))
        b= int(input("Valor 2: "))
        opertations(a,b,opcion)
    elif(opcion==4):
        print("División")
        a= int(input("Valor 1: "))
        b= int(input("Valor 2: "))
        opertations(a,b,opcion)
    else:
        print("Error")

    
    cortar = input("¿Desea salir?:").lower()
    if(cortar=="si"):
        seguir=False