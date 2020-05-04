def factorial_no_recursivo(numero):
    fact = 1
    #Se genera una lista que va de la n a l, el -1 indica que cada iteración se resta. 1 al indice
    for i in range(numero,1,-1):
        fact *=i #Esto es equivalente a fact = fact *i
    return fact
factorial_no_recursivo(5)#Invocamos a la funcion
