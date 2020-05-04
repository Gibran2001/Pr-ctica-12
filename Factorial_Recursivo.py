def factorial_recursivo(numero):
    if numero < 2: #El caso base es cuando numero <2 y la función regresa I
        return 1
    return numero * factorial_recursivo(numero-1) #La función se llama a si misma
factorial_recursivo(5)#Invocamos
