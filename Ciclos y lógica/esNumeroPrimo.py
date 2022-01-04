########################################################################
# Elaborado por: Mónica Alfaro P
# Fecha de creación: 12/03/2020 10:10pm
# Fecha de última modificación: 12/03/2020 11:40pm
# Versión: 3.8.1
########################################################################

#Funciones
def esNumeroPrimo(num):
    """
    Ejemplo de definición de una función:
    Funcionalidad: Saber si el número ingresado es primo o no.
    Entrada: int(numero)
    Salida: Si es primo o no.
    """
    contador=1
    numeroPrimo=0
    while(contador<=num):
        if(num%contador==0):
            numeroPrimo+=1
        else:
            ""
        contador+=1
    if(numeroPrimo==2):
        print("Es primo.")
    else:
        print("No es primo.")
    return 
        
#Programa principal
numero=int(input("Inserte un número entero: "))
esNumeroPrimo(numero)
