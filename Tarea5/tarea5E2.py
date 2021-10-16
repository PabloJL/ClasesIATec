#E2
numero= int(input("Ingrese un número del 1 al 10:\n"))


if(numero>0 and numero<=10):
    for i in range(1,11):
        print (i*numero)
else: 
    print("Error")

