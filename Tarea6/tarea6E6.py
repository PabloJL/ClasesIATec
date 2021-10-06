seguir= True
while seguir == True:

    print("1:Suma.")
    print("2:Resta.")
    print ("3:Multiplicación.")
    print("4:División.")
    opcion = int(input("Elija una opción del 1 al 4: "))

    if(opcion == 1):
        print("Suma")
    elif(opcion==2):
        print("Resta")
    elif(opcion==3):
        print("Multiplicación")
    elif(opcion==4):
        print("División")
    else:
        print("Error")

    
    cortar = input("¿Desea salir?:").lower()
    if(cortar=="si"):
        seguir=False