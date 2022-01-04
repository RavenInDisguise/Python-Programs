###############################################################################
#Elaborado por Mónica Alfaro P y Jennifer Alvarado B
#Inicio 29/07/2020 09:10 am
#Última modificación 29/07/2020 03:40 pm
#Versión 3.8.2
###############################################################################

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

def esBisiesto(anno):
    """
    Funcionalidad: Validar si un año es bisiesto.
    Entradas: El año.
    Salidas: True (sí es bis) o False (no es bis).
    """
    if(anno%4==0 and (anno%100!=0 or anno%400==0)):
       return True
    
###############################################################################
#Funciones recursivas:

#Reto 1:
def encontrarDigRec(num,dig,cont):
    """
    Funcionalidad: Contar la cantidad de veces que un dígito aparece en un número.
    Entradas: Número, dígito y contador.
    Salidas: La cantidad de veces que aparece el dígito indicado.
    """
    if num==0:
        return cont
    if num%10==dig:
        return encontrarDigRec(num//10,dig,cont+1)
    else:
        return encontrarDigRec(num//10,dig,cont)
###############################################################################
#Reto 2:
def sumarNumerosImparesIntervalo(num1,num2,suma):
    """
    Funcionalidad: Suma los números impares en un intervalo dado.
    Entrada: El primer número, el segundo y cero.
    Salida: La suma de los números impares en un intervalo dado.
    """
    if num1>num2:
        return suma
    elif esPar(num2):
        return sumarNumerosImparesIntervalo(num1,num2-1,suma)
    else:
        return sumarNumerosImparesIntervalo(num1,num2-1,suma+num2)
###############################################################################
#Reto 3:
def validarBinRec(num,var):
    """
    Funcionalidad: Validar que un número esa binario.
    Entradas: Número y variable.
    Salidas: True (es binario) o False (no es binario).
    """
    if num==0:
        return var
    elif num%10==1 or num%10==0:
        return validarBinRec(num//10,True)
    elif num%10!=1 or num%10!=0:
        return validarBinRec(0,False)
###############################################################################
#Reto 4:
def contarBisiestosInterv(anno1,anno2,suma):
    """
    Funcionalidad: Contar la cantidad de años bisiestos de un intervalo de años dado.
    Entrada: El primer año, el segundo y cero.
    Salida: La suma de los años bisiestos en un intervalo dado.
    """
    if anno1>anno2:
        return suma
    elif esBisiesto(anno2):
        return contarBisiestosInterv(anno1,anno2-1,suma+1)
    else:
        return contarBisiestosInterv(anno1,anno2-1,suma)
###############################################################################
#Reto 5:
def contarHumanosRec(num1,num2,cont):
    """
    Funcionalidad: Calcula el número de personas existentes en cada generación.
    Entrada: Número inicial de personas, número de generaciones a calcular y el contador..
    Salida: Cantidad de personas por generación.
    """
    if num2==0:
        print("Generación inicial:",num1//2,"personas")
        return 
    elif cont==num2:
        return num1
    else:
        resultado=(num1//2)*3
        print("En la generación",cont,":",resultado,"personas")
        return contarHumanosRec(resultado,num2,cont+1)
