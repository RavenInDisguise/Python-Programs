###############################################################################
#Elaborado por Mónica Alfaro P y Jennifer Alvarado B
#Inicio 29/07/2020 09:10 am
#Última modificación 29/07/2020 03:40 pm
#Versión 3.8.2
###############################################################################

print("\n-------------------------Recursividad por Cola---------------------------")
#Importación de librerías de funciones:
from funcionesRecCola import*
#Funciones de validaciones:

def validarValores(valor):
    """
    Funcionalidad: Valida si los valores son un número entero o no.
    Entrada: El valor.
    Salida: True/None.
    """
    if isinstance(valor,int):
        return True

def validarMayores(valor1,valor2):
    """
    Funcionalidad: Valida si el primer valor es menor que el segundo.
    Entrada: El int(valor1) y el int(valor2).
    Salida: True/None.
    """
    if (valor1<valor2):
        return True
    
def validarPositivo(valor1):
    """
    Funcionalidad: Valida si el primer valor es menor que el segundo.
    Entrada: El int(valor1) y el int(valor2).
    Salida: True/None.
    """
    if (valor1>=0):
        return True
    
def validarNum(numero):
    """
    Funcionalidad: Validar que el número sea entero y mayor o igual a cero.
    Entradas: Número.
    Salidas: True (correcto) o False (incorrecto).
    """
    if isinstance(numero,int)and numero>=0:
        return True
    else:
        return False
    
def validarNums(numero,digito):
    """
    Funcionalidad: Validar el número y el dígito. Entros y dígito entre 0 y 9.
    Entradas: El número y el dígito.
    Salidas: True (correctos) o False (incorrectos).
    """
    if isinstance(numero,int)and isinstance(digito,int):
        if numero>0 and 0<=digito<=9:
            return True
        else:
            return False
    else:
        return False
    
###############################################################################
    
def encontrarDigito():
    """
    Funcionalidad: Mostrar las entradas y sus salidas.
    Entradas: Lista con pruebas.
    Salidas: Resultado.
    """
    print("-------------------------------------------------------------------------")
    print("\nReto 1: Determinar la cantidad de veces de un dígito.\n")
    pruebas=[(25.2,2),(123451,1),(123233,3),(55565,5)]
    for pareja in pruebas:
        print(pareja)
        if validarNums(pareja[0],pareja[1]):
            print("En el número",pareja[0],"el dígito",pareja[1],"se repite "+str(encontrarDigRec(pareja[0],pareja[1],0))+" veces.\n")
        else:
            print("El número debe ser entero y el dígito debe estar entre 0 y 9.\n")
    return

#PP - Reto 1
encontrarDigito()

###############################################################################
    
def sumarImparesInterv():
    """
    Funcionalidad: Suma los números impares en un intervalo dado.
    Entrada: Ninguna.
    Salida: La suma de los números impares en un intervalo dado.
    """
    print("-----------------------------------------------------------------------")
    print("\nReto 2: Sume los números impares en un intervalo dado.")
    listaNumeros=[("Hola",25.3),(5,0),(-5,5),(0,7),(2,125)]
    for numero in listaNumeros:
        print("\nSu valor inicial (A): "+str(numero[0]))
        print("Su valor final (B): "+str(numero[1]))
        if(validarValores(numero[0]) and validarValores(numero[1])):
            if(validarMayores(numero[0],numero[1])):
                print("La suma de los valores impares es:",sumarNumerosImparesIntervalo(numero[0],numero[1],0))
            else:
                print("B debe ser mayor que A.")
        else:
            print("A y B deben ser números enteros.")

#PP - Reto 2 
sumarImparesInterv()

###############################################################################

def validarBin():
    """
    Funcionalidad: Mostrar las entradas y sus salidas.
    Entradas: Lista con pruebas.
    Salidas: Resultado.
    """
    print("\n-------------------------------------------------------------------------")
    print("\nReto 3: Validar si es binario.\n")
    pruebas=[1001019,5679,0,10101]
    for num in pruebas:
        if validarNum(num):
            print(num)
            print("¿El número",num,"es binario? "+str(validarBinRec(num,True))+"\n")
    return ""
#PP - Reto 3
validarBin()

###############################################################################
    
def cantidadBisiestoInterv():
    """
    Funcionalidad: Contar la cantidad de años bisiestos de un intervalo de años dado.
    Entrada: Ninguna.
    Salida: La suma de los años bisiestos en un intervalo dado.
    """
    print("-----------------------------------------------------------------------")
    print("\nReto 4: Cantidad de años bisiestos en un intervalo.")
    listaNumeros=[(1500,1836),(2000,2025)]
    for numero in listaNumeros:
        print("\nSu valor inicial: "+str(numero[0]))
        print("Su valor final: "+str(numero[1]))
        if(validarValores(numero[0]) and validarValores(numero[1])):
            if(validarMayores(numero[0],numero[1])):
                if(validarPositivo(numero[0]) and validarPositivo(numero[1])):
                    print("La cantidad de años bisiestos:",contarBisiestosInterv(numero[0],numero[1],0))
                else:
                    print("Ingrese sólo años positivos.")
            else:
                print("El año inicial debe ser mayor que el final.")
        else:
            print("Los años deben ser números enteros.")

#PP - Reto 4
       
cantidadBisiestoInterv()

###############################################################################

def contarGenHumana():
    """
    Funcionalidad: La cantidad de parejas por generación según un número dado.
    Entrada: Ninguna.
    Salida: La suma de los años bisiestos en un intervalo dado.
    """
    print("\n-----------------------------------------------------------------------")
    print("\nReto 5: Colonia humana.")
    generaciones=[-1,0,1,2,3,4]
    num=18
    for numero in generaciones:
        print("\nCantidad de personas inicial: ",num)
        print("Cantidad de generaciones: ",numero)
        if(validarValores(num) and validarValores(numero)):
            if(validarPositivo(num) and validarPositivo(numero)):
                contarHumanosRec(num,numero,0)
            else:
                print("Ingrese sólo números positivos.")
        else:
            print("Los números deben ser enteros.")

#PP - Reto 5
contarGenHumana()
