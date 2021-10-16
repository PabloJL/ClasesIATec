##E5
cantidad = int(input("¿Cuántos unidades desea promediar?:\n"))
suma = 0
unidades=[]

if(cantidad != 0):
    for i in range(cantidad):
        unidades.append(int(input("Agregar calificación:\n")))
    suma = sum(unidades)
    promedio = suma/cantidad
    print(f'Su promedio es de: {promedio}')
else:
    print("Error")    
