##E2
primerNumero= int(input("Ingrese el primer número:\n"))
segundoNumero= int(input("Ingrese el segundo número:\n"))
tercerNumero= int(input("Ingrese el tercer número:\n"))

if(primerNumero < segundoNumero and tercerNumero > primerNumero):
    print(f"{primerNumero} es el menor")
elif(segundoNumero<primerNumero and tercerNumero > segundoNumero):
    print(f"{segundoNumero} es el menor")
elif(primerNumero ==segundoNumero and primerNumero<tercerNumero):
    print(f'{primerNumero} y {segundoNumero} son menores')
elif(segundoNumero == tercerNumero and segundoNumero<primerNumero):
    print(f'{segundoNumero} y {tercerNumero} son menores')
elif(primerNumero == tercerNumero and segundoNumero> primerNumero):
    print(f'{primerNumero} y {tercerNumero} son menores')
elif(primerNumero == segundoNumero and primerNumero == tercerNumero):
    print("Los números son iguales")
else:
    print(f'{tercerNumero} es el menor')