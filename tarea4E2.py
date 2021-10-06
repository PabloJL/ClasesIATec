primerNumero= int(input("Ingrese el primer número:\n"))
segundoNumero= int(input("Ingrese el segundo número:\n"))
tercerNumero= int(input("Ingrese el tercer número:\n"))

if (primerNumero > segundoNumero and segundoNumero > tercerNumero):
    print(f'El primer número ({primerNumero}) es mayor que el segundo número ({segundoNumero}) y el tercer número({tercerNumero}))')

elif(segundoNumero> primerNumero and primerNumero> tercerNumero):
     print(f'El segundo número ({segundoNumero}) es mayor que el primer número ({primerNumero}) y el tercer número({tercerNumero}))')

elif(primerNumero == segundoNumero and primerNumero == tercerNumero):
    print('Los tres números son iguales')

else:
     print(f'El tercer número ({tercerNumero}) es mayor que el primer número ({primerNumero}) y el segundo número({segundoNumero}))')