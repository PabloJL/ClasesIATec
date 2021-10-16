# E3
import operator
import math
seguir= True

def areaTriangulo (b,h):
    print (f'El área del triángulo es de: {operator.truediv(operator.mul(b,h),2)}')

def areaCuadrado (l):
    print (f'El área del cuadrado es de: {operator.mul(l,l)}')

def areaRectangulo (b,h):
    print (f'El área del rectángulo es de: {operator.mul(b,h)}')

def areaCirculo (r):
    print (f'El área del círculo es de: {operator.mul(math.pi, math.pow(r,2))}')




while seguir == True:
    print("1:Triángulo.\n2:Cuadrado.\n3:Rectángulo.\n4:Circulo")
    opcion = int(input("Elija una opción del 1 al 4: "))
    
    if(opcion == 1):
        print("Triángulo")
        b= int(input("Base: "))
        h= int(input("Altura: "))
        areaTriangulo(b,h)
    elif(opcion==2):
        print("Cuadrado")
        l= int(input("Lado: "))
        areaCuadrado(l)
    elif(opcion==3):
        print("Rectángulo")
        b= int(input("Base: "))
        h= int(input("Altura: "))
        areaRectangulo(b,h)
    elif(opcion==4):
        print("Circulo")
        r= int(input("Radio: "))
        areaCirculo(r)
    else:
        print("Error")

    
    cortar = input("¿Desea salir?:").lower()
    if(cortar=="si"):
        seguir=False