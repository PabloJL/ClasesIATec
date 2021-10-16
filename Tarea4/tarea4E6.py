##E6
primerNumero= int(input("Ingrese el primer número:\n"))
segundoNumero= int(input("Ingrese el segundo número:\n"))

if(primerNumero>=0 and segundoNumero>=0):
    print(f'El primer número ({primerNumero}) y el segundo ({segundoNumero}) son de signo positivo, por lo tanto, son de signos iguales')
elif(primerNumero<0 and segundoNumero>=0):
    print(f'El primer número ({primerNumero}) es negativo y el segundo ({segundoNumero}) es positivo, por lo tanto, tienen signos diferentes')
elif(primerNumero>=0 and segundoNumero<0):
    print(f'El primer número ({primerNumero}) es positivo y el segundo ({segundoNumero}) es negativo, por lo tanto, tienen signos diferentes')
else:
    print(f'El primer número ({primerNumero}) y el segundo ({segundoNumero}) son de signo negativo, por lo tanto, son de signos iguales')