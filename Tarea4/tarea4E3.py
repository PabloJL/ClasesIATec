primerNumero= int(input("Ingrese el primer número:\n"))
segundoNumero= int(input("Ingrese el segundo número:\n"))

if(primerNumero > segundoNumero):
    print("Primer número menos el segundo número:\n",primerNumero-segundoNumero)
elif(primerNumero == segundoNumero):
    print('Los 2 números son iguales')
else:
    print("Segundo número menos el primer número:\n",segundoNumero-primerNumero)