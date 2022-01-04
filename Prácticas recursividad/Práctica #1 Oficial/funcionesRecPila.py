##############################################################################
#Elaborado por Mónica Alfaro Parrales y Jennifer Alvarado Brenes
#Inicio: 24/07/2020 10:35 am
#Última modificación: 24/07/2020 06:00 pm
#Versión 3.8.2
##############################################################################

#Función desarrollada en un laboratorio anterior:

def esPar(numero):
    """
    Funcionalidad: Validar si un número es par.
    Entradas: El número.
    Salidas: True (sí es par) o False (no es par).
    """
    if numero%2==0:
        return True
    else:
        return False

#Reto 1

def encontrarCeroRec(num):
    """
    Funcionalidad: Retorna True al encontrar un cero en un número.
    Entradas: El número.
    Salidas: True o False.
    """
    if num==0:
        return False
    elif (num%10)==0:
        return True
    else:
        return encontrarCeroRec(num//10)
#Reto 2

def esParRecursivo(num):
    """
    Funcionalidad: Encuentra si la cifra posee un número par.
    Entrada: El número int(num).
    Salida: Si tiene o no un número par.
    """
    if num==0:
        return "La cifra numérica no posee ningún par."
    elif esPar(num%10):
        return "La cifra numérica, posee al menos un par."
    else:
        return esParRecursivo(num//10)
    
#Reto 3

def sumarNumerosRec(num):
    """
    Funcionalidad: Suma todos los dígitos de un número. 123
    Entradas: El número.
    Salidas: El resultado de la suma.
    """
    if num==0:
        return 0
    else:
        return num%10 + sumarNumerosRec(num//10)
    
#Reto 4

def multiplicarImparesRec(num):
    """
    Funcionalidad: Multiplicar los números impares encontrados en un número.
    Entrada: El número int(num).
    Salida: La multiplicación de los números impares.
    """
    if num==1:
        return 1
    elif num==0:
        return 0
    elif esPar(num)==False:
        return num%10 * multiplicarImparesRec(num//10)
    else:
        return multiplicarImparesRec(num//10)
    
#Reto 5

def encontrarMayorRec(num):
    """
    Funcionalidad: Encontrar el dígito mayor de un número.
    Entradas: El número. 
    Salidas: El dígito mayor.
    """
    if num==0:
        return 0
    else:
        if num%10>encontrarMayorRec(num//10): 
            return num%10
        else:
            return encontrarMayorRec(num//10)
        
#Reto 6

def determinarCantidad(num,dig):
    """
    Funcionalidad: Determinar cuántas veces aparece un dígito en un número.
    Entrada: El número int(num) y el dígito int(dig).
    Salida: La cantidad de veces que aparece.
    """
    if num==0:
        return 0
    elif num%10==dig:
        return 1 + determinarCantidad(num//10,dig)
    else:
        return 0 + determinarCantidad(num//10,dig)
    
#Reto 7

def formarParesRec(num):
    """
    Funcionalidad: Formar un número con los dígitos pares de otro.
    Entradas: El número.
    Salidas: El número nuevo. 
    """
    if num==0:
        return 0
    else:
        if esPar(num%10):
            return (10*formarParesRec(num//10))+num%10
        else:
            return formarParesRec(num//10)
        
#Reto 8

def esNumeroPrimo(num,valor=2):
    """
    Funcionalidad: Descubrir si un número es primo.
    Entrada: El número int(num) y valor que es 2.
    Salida: True/False.
    """
    if num%valor==0 and valor!=2:
        return False

    elif valor>num/2:
        return True
    else:
        return esNumeroPrimo(num, valor+1)
    
#Reto 9

def sumarMultiplosRec(num,dig):
    """
    Funcionalidad: Sumar los dígitos del primer números que sean múltiplos del segundo.
    Entradas: Ambos números.
    Salidas: El resultado de las operaciones.
    """
    if num==0:
        return 0
    else:
        resultado=(num%10)%dig
        if resultado==0:
            return num%10 + sumarMultiplosRec(num//10,dig)
        else:
            return sumarMultiplosRec(num//10,dig)
        
#Reto 10

def elevarPotencia(num,pot):
    """
    Funcionalidad: Elevar un número a la potencia ingresada.
    Entrada: El número int(num) y la potencia int(pot).
    Salida: El número elevado a la potencia.
    """
    if pot==0:
        return 1
    else:
        return num * elevarPotencia(num,pot-1)
