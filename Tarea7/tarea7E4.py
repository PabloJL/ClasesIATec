# E4
def pesoToDolar (value):
    return value / 20.34

value = float(input("¿Cuántos pesos desea convertir?: "))
llamada = pesoToDolar(value)
euros = llamada * 0.86

print (f'Valor en pesos: ${value}\nValor en dolares: ${llamada}\nValor en Euros: €{euros}')

