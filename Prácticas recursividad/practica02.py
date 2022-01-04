
#Validaciones:

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

def esBisiesto(anno):
    """
    Funcionalidad: Validar si un año es bisiesto.
    Entradas: El año.
    Salidas: True (sí es bis) o False (no es bis).
    """
    if(anno%4==0 and (anno%100!=0 or anno%400==0)):
       return True

##############################################################################
    
#Funciones recursivas:

#Reto 2
    
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

#Reto 4
    
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

##############################################################################
   
#Reto 2

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

##############################################################################
    
#Reto 4

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

##############################################################################
    
#Reto 5

def contarGenHumana():
    """
    Funcionalidad: La cantidad de parejas por generación según un número dado.
    Entrada: Ninguna.
    Salida: La suma de los años bisiestos en un intervalo dado.
    """
    print("-----------------------------------------------------------------------")
    print("\nReto 5: Cantidad de años bisiestos en un intervalo.")
    listaNumeros=[(9,2)]
    for numero in listaNumeros:
        print("\nSu valor inicial: "+str(numero[0]))
        print("Su valor final: "+str(numero[1]))
        if(validarValores(numero[0]) and validarValores(numero[1])):
            if(validarPositivo(numero[0]) and validarPositivo(numero[1])):
                contarHumanos(numero[0],numero[1],0)
            else:
                print("Ingrese sólo números positivos.")
        else:
            print("Los números deben ser enteros.")

#PP - Reto 5
       
contarGenHumana()
