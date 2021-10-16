# E1
seguir= True

def exchange(currency, convertTo):
    if (convertTo == 1):
        total = currency / 20.34
        print(f'${currency} pesos son ${total} dolares')
    elif (convertTo == 2):
        total = currency * 20.34
        print(f'${currency} dolares son ${total} pesos')
    elif (convertTo == 3):
        total = currency / 23.59
        print(f'${currency} pesos son €{total} euros')
    elif (convertTo == 4):
        total = currency * 23.59
        print(f'€{currency} euros son ${total} pesos')
    
    

while seguir == True:
    print("1:De pesos a dólares\n2:De dólares a pesos.\n3:De pesos a euros.\n4:De euros a pesos.")
    opcion = int(input("Elija una opción del 1 al 4: "))

    if(opcion == 1):
        print("Pesos a dólares")
        value= int(input("Cantidad en pesos:"))
        exchange(value, opcion)
    elif(opcion==2):
        print("Dólares a pesos")
        value= int(input("Cantidad en dólares:"))
        exchange(value, opcion)
    elif(opcion==3):
        print("Pesos a euros")
        value = int(input("Cantidad en pesos:"))
        exchange(value, opcion)
    elif(opcion==4):
        print("Euros a pesos")
        value = int(input("Cantidad en euros:"))
        exchange(value, opcion)
    else:
        print("Error")

    
    cortar = input("¿Desea salir?:").lower()
    if(cortar=="si"):
        seguir=False
       