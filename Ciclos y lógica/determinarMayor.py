########################################################################
# Elaborado por: Mónica Alfaro P
# Fecha de creación: 12/03/2020 9:15pm
# Fecha de última modificación: 12/03/2020 9:30pm
# Versión: 3.8.1
########################################################################

#Ejemplo de definición de una función:
#Funcionalidad: Determinar el número mayor de una serie de números ingresados.
#Entrada: int(numero)
#Salida: Número mayor int(numMayor)

def determinarMayor(num):
    numMayor=0
    if(isinstance(num,int)):
        while(num!=0):
            num2=num%10
            if(numMayor<num2):
                numMayor=num2
            else: ""
            num=num//10
        print("El número mayor es: ", numMayor)
        return
    elif num==None:
        print("Debe ingresar un valor numérico.")
    else:
        print("El valor debe ser únicamente entero.")
        
#Programa principal
numero=int(input("Inserte un número entero: "))
determinarMayor(numero)
