#E5
seguir= True
while seguir == True:

    print("1:De pesos a dólares")
    print("2:De dólares a pesos")
    print ("3:De pesos a euros.")
    print("4:De euros a pesos.")
    opcion = int(input("Elija una opción del 1 al 4: "))

    if(opcion == 1):
        print("De pesos a dólares")
    elif(opcion==2):
        print("De dólares a pesos")
    elif(opcion==3):
        print("De pesos a euros")
    elif(opcion==4):
        print("De euros a pesos")
    else:
        print("Error")

    
    cortar = input("¿Desea salir?:").lower()
    if(cortar=="si"):
        seguir=False
       