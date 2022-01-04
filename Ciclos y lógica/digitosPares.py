########################################################################
# Elaborado por: Mónica Alfaro P
# Fecha de creación: 11/03/2020 3:10pm
# Fecha de última modificación: 11/03/2020 4:00pm
# Versión: 3.8.1
########################################################################

#Ejemplo de definición de una función:
#Funcionalidad: Mostrar los pares del entero ingresado.
#Entrada: Entero int(num)
#Salida: Números pares del entero.

def mostrarPares (num):
    if(isinstance(num,int)):
        print("Los números pares del entero ingresado son: ")
        while (num!=0):
                if(num%2==0):
                    print(num%10)
                else:
                    ""
                num=num//10
        return 
    else:
        print("Número no entero.")

#Programa principal
numero=int(input("Inserte un número entero: "))
mostrarPares(numero)


