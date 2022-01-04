########################################################################
# Elaborado por: Mónica Alfaro P
# Fecha de creación: 12/03/2020 9:40pm
# Fecha de última modificación: 12/03/2020 10:05pm
# Versión: 3.8.1
########################################################################

#Ejemplo de definición de una función:
#Funcionalidad: Elevar un número.
#Entrada: int(numero),int(numeroPot).
#Salida: Número int(numero) elevado a la int(numeroPot).

def elevarNumero(num, numPot):
    contador=0
    potencia=1
    if(isinstance(num,int)):
        if(numPot==0):
            print("El número",num, "elevado a la 0 es 1.")
        else:
            while(contador<numPot):
                potencia=potencia*num
                contador+=1
            print("El número",num,"elevado a la",numPot, "es", potencia)
            return
    else:
        print("El valor debe ser únicamente entero.")
        
#Programa principal
numero=int(input("Inserte un número entero: "))
numeroPot=int(input("Inserte un número entero al que desea elevar: "))
elevarNumero(numero, numeroPot)
