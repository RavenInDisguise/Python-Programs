########################################################################
# Elaborado por: Mónica Alfaro P
# Fecha de creación: 11/03/2020 4:20pm
# Fecha de última modificación: 11/03/2020 5:10pm
# Versión: 3.8.1
########################################################################

#Ejemplo de definición de una función:
#Funcionalidad: Definir si hay un cero en el número entero ingresado.
#Entrada: int(num)
#Salida: ¿Posee o no posee al menos un cero?

def encontrarAlmenosUnCero (num):
    if(isinstance(num,int)):
        if(num%10==0):
            print("Posee al menos un cero.")
            while (num!=0):
                num=num//10
            return
        else:
            print("No posee ningún cero.")
    else:
        print("Número no entero.")

#Programa principal
numero=int(input("Inserte un número entero: "))
encontrarAlmenosUnCero(numero)


