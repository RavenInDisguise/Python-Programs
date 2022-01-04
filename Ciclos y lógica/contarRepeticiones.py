########################################################################
# Elaborado por: Mónica Alfaro P
# Fecha de creación: 12/03/2020 8:00pm
# Fecha de última modificación: 12/03/2020 9:00pm
# Versión: 3.8.1
########################################################################

#Ejemplo de definición de una función:
#Funcionalidad: Contar la cantidad de números repetidos de acuerdo al número ingresado por el usuario y el número que desea averiguar.
#Entrada: int(numero),int(numeroRepe)
#Salida: ¿Cuántas veces se repite? int(contador)

def contarRepeticiones(num,numRepe):
    contador=0
    if(isinstance(num,int)):
        while(num!=0):
            numVal=num%10
            if(numVal==numRepe):
                contador+=1
            else: ""
            num=num//10
        print("El número se repite esta cantidad de veces: ",contador)
        return
    else:
        print("No es un número entero")
        
#Programa principal
numero=int(input("Inserte un número entero: "))
numeroRepe=int(input("Inserte el número entero que desea saber si se repite: "))
contarRepeticiones(numero, numeroRepe)
