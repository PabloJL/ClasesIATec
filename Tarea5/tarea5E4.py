##E4
cantidad = int(input("¿Cuántos números desea sumar?:\n"))
suma = 0
lista=[]

if(cantidad != 0):
    for i in range(cantidad):
        lista.append(int(input("Agregar número a la sumatoria:\n")))
    suma = sum(lista)
    print(f'La suma total es de: {suma}')
else:
    print("Error")    
