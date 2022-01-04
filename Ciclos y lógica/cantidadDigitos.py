########################################################################
# Elaborado por: Mónica Alfaro P
# Fecha de creación: 11/03/2020 1:10pm
# Fecha de última modificación: 11/03/2020 1:30pm
# Versión: 3.8.1
########################################################################

#Ejemplo de definición de una función:
#Funcionalidad: Contar la cantidad de dígitos de un entero ingresado.
#Entrada: Entero int(num)
#Salida: Cantidad de dígitos (contador)

def cantidadDigitos (num):
    contador=0
    if(isinstance(num,int)):
        while (num!=0):
            num=num//10
            contador+=1
        print("Tiene un total de: ",contador, " dígitos.")
        return 
    else:
        print("Número no entero.")

#Programa principal
numero=int(input("Inserte un número entero: "))
cantidadDigitos(numero)


