##############################################################################
#Elaborado por Mónica Alfaro Parrales y Jennifer Alvarado Brenes
#Inicio: 24/07/2020 10:35 am
#Última modificación: 24/07/2020 06:00 pm
#Versión 3.8.2
##############################################################################

#Práctica de Recursividad por Pila

from funcionesRecPila import*
##############################################################################

print("-------------------Práctica - Recursividad de Pila---------------------")

#Validaciones:

def validarNumero1(numero):
    """
    Funcionalidad: Validar que un dato sea un número entero.
    Entradas: El número.
    Salidas: Mensaje indicado.
    """
    if isinstance(numero,int):
        if numero>0:
            salida=encontrarCeroRec(numero)
            mensaje="¿"+str(numero)+" contiene ceros? "+str(salida)
            return mensaje
        else:
            return "Debe indicar un número entero mayor a cero."
    else:
        return "Debe indicar un número entero."
    
def validarValores(valor):
    """
    Funcionalidad: Valida si los valores son un número entero o no.
    Entrada: El valor.
    Salida: True/None.
    """
    if isinstance(valor,int):
        return True

def validarDigito(dig):
    if(0<dig<=9):
        return True
    
def validarNum(num):
    """
    Funcionalidad: Valida si el número es positivo.
    Entrada: El número int(num).
    Salida: True/None.
    """
    if(0<=num):
        return True

def validarNumero7(numero):
    """
    Funcionalidad: Validar que un número sea entero. Si es negativo, lo vuelve positivo,
    Entradas: El número.
    Salidas: Mensaje indicado.
    """
    if isinstance(numero,int):
        numeroNuevo=formarParesRec(abs(numero))
        mensaje="El número que se forma con los dígitos pares de "+str(numero)+" es: "+str(numeroNuevo)
        return mensaje
    else:
        return "Debe indicar un número entero."
    
#Reto 1 – Encontrar al menos un cero en un número.

def encontrarCero():
    """
    Funcionalidad: Muestra los datos de prueba y sus respuestas.
    Entradas: No hay.
    Salidas: Las respuestas del reto.
    """
    prueba1=[125.2,-10,0,125,81254010]
    print("-----------------------------------------------------------------------")
    print("\nReto 1: Encontrar al menos un cero en un número.\n")
    for numero in prueba1:
        print(numero)
        print(str(validarNumero1(numero))+"\n")

#PP - Reto 1
encontrarCero()

##############################################################################
        
#Reto 2 – Indique si en una cifra dada, hay al menos un par.

def descubrirPar():
    """
    Funcionalidad: Encuentra si la cifra posee un número par.
    Entrada: Ninguna.
    Salida: Si tiene o no un número par.
    """
    print("-----------------------------------------------------------------------")
    print("\nReto 2: Indique si en una cifra dada, hay al menos un par.")
    listaNumeros=["Hola",1357,1234]
    for numero in listaNumeros:
        print("\nSu valor: "+str(numero))
        if(validarValores(numero)):
            print(esParRecursivo(abs(numero)))
        else:
            print("El valor ingresado debe corresponder a un número únicamente.")
#PP - Reto 2
descubrirPar()

##############################################################################
        
#Reto 3 – Indique la suma de los dígitos de una cifra.
        
def sumarNumeros():
    """
    Funcionalidad: Muestra los datos de prueba y sus respuestas.
    Entradas: No hay.
    Salidas: Las respuestas del reto.
    """
    print("\n-----------------------------------------------------------------------")
    print("\nReto 3: Indique la suma de los dígitos de una cifra.\n")
    numero=12345
    print(numero)
    resultado=sumarNumerosRec(numero)
    print("La suma de los dígitos de",numero,"es: ",resultado,"\n")

#PP - Reto 3
sumarNumeros()

##############################################################################
        
#Reto 4 – Indique la multiplicación de los sólo los dígitos impares.

def multiplicarImp():
    """
    Funcionalidad: Multiplicar los números impares encontrados en un número.
    Entrada: Ninguna.
    Salida: La multiplicación de los números pares.
    """
    print("-----------------------------------------------------------------------")
    print("\nReto 4: Multiplicar los números impares encontrados en un número.")
    listaNumeros=["1223a",12345,246]
    for numero in listaNumeros:
        print("\nSu valor: "+str(numero))
        if(validarValores(numero)):
            print("La multiplicación impar es:",multiplicarImparesRec(abs(numero)))
        else:
            print("El valor ingresado debe corresponder a un número únicamente.")
#PP - Reto4
multiplicarImp()

##############################################################################
        
#Reto 5 – Encontrar el número más grande la de cifra numérica.

def encontrarMayor():
    """
    Funcionalidad: Muestra los datos de prueba y sus respuestas.
    Entradas: No hay.
    Salidas: Las respuestas del reto.
    """
    print("\n-----------------------------------------------------------------------")
    print("\nReto 5: Encontrar el número más grande la de cifra numérica.\n")
    prueba5=["123a",4571,333]
    for escenario in prueba5:
        print(escenario)
        if validarValores(escenario):
            salida=encontrarMayorRec(escenario)
            print("El número mayor de",escenario," es: ",salida,"\n")
        else:
            print("Debe ser un número entero.\n")
#PP - Reto 5
encontrarMayor()
    
##############################################################################

#Reto 6 – Determinar la cantidad de dígitos en una cifra: Ingresa la cifra numérica y un dígito a buscar.

def determinarRepeticiones():
    """
    Funcionalidad: Determinar cuántas veces aparece un dígito en un número.
    Entrada: El número int(num) y el dígito int(dig).
    Salida: La cantidad de veces que aparece.
    """
    print("-----------------------------------------------------------------------")
    print("\nReto 6: Determinar la cantidad de dígitos en una cifra:")
    listaNumeros=[(1234567123,2),(3451233453,3),(234565,9)]
    for numero in listaNumeros:
        print("\nSu valor: "+str(numero[0]))
        if(validarValores(numero[0])):
            if(validarNum(numero[0])):
                print("Su dígito: "+str(numero[1]))
                if(validarDigito(numero[1]) and validarValores(numero[1])):
                    print("Cantidad de veces que aparece el dígito "+str(numero[1])+" en "+str(numero[0])+":",determinarCantidad(numero[0],numero[1]))
                else:
                    print("Debe ingresar un dígito del 0 al 9.")
            else:
                print("El número debe ser positivo.")
        else:
            print("El valor ingresado debe corresponder a un número positivo únicamente.")
#PP - Reto 6
determinarRepeticiones()

##############################################################################

#Reto 7 – Formar un número con los dígitos pares de otro número.

def formarPares():
    """
    Funcionalidad: Muestra los datos de prueba y sus respuestas.
    Entradas: No hay.
    Salidas: Las respuestas del reto.
    """
    print("\n-----------------------------------------------------------------------")
    print("\nReto 7: Formar un número con los dígitos pares de otro número.\n")
    prueba7=["Hola!",255.3,-2556,2552180,125,135]
    for escenario in prueba7:
        print(escenario)
        print(str(validarNumero7(escenario))+"\n")

#PP - Reto7
formarPares()

##############################################################################

#Reto 8 –Número primo.

def descubrirPrimo():
    """
    Funcionalidad: Descubrir si un número es primo.
    Entrada: Ninguna.
    Salida: True/False.
    """
    print("-----------------------------------------------------------------------")
    print("\nReto 8: Determinar si un número es primo.")
    listaNumeros=["sd",-25,401,7,5,9]
    for numero in listaNumeros:
        print("\nSu valor: "+str(numero))
        if(validarValores(numero)):
            if(validarNum(numero)):
                print(esNumeroPrimo(abs(numero)))
                
            else:
                print("Debe ser un número positivo.")
                
        else:
            print("El valor ingresado debe corresponder a un número únicamente.")
#PP - Reto 8
descubrirPrimo()

##############################################################################

#Reto 9 - Sumar dígitos múltiplos.

def sumarMultiplos():
    """
    Funcionalidad: Muestra los datos de prueba y sus respuestas.
    Entradas: No hay.
    Salidas: Las respuestas del reto.
    """
    print("\n-----------------------------------------------------------------------")
    print("\nReto 9: Sumar dígitos múltiplos.\n")
    prueba9=[(6,3),(1002,7),(666,3),(1234,2)]
    for numero in prueba9:
        print(numero)
        if(validarValores(numero[0])):
            if(validarNum(numero[0])):
                if(validarDigito(numero[1]) and validarValores(numero[1])):
                    resultado=sumarMultiplosRec(numero[0],numero[1])
                    print("La suma que los dígitos en",numero[0],"que son múltiplos de",numero[1],"es: ",resultado,"\n")
                else:
                    print("Debe ingresar un dígito del 0 al 9.")
            else:
                print("El número debe ser positivo.")
        else:
            print("El valor ingresado debe corresponder a un número positivo únicamente.")

#PP - Reto 9
sumarMultiplos()

##############################################################################

#Reto 10 - Elevar un número a una potencia dada.

def elevarNumero():
    """
    Funcionalidad: Elevar un número a la potencia ingresada.
    Entrada: Ninguna.
    Salida: El número elevado a la potencia.
    """
    print("-----------------------------------------------------------------------")
    print("\nReto 10: Elevar un número a una potencia dada.")
    listaNumeros=[(5,0),(2,4),(0,0),(5,3),(1,0)]
    for numero in listaNumeros:
        print("\nSu valor: "+str(numero))
        if(validarValores(numero[0])):
            if(validarNum(numero[0])):
                print("La potencia elevada es: ",elevarPotencia(abs(numero[0]),abs(numero[1])))
                
            else:
                print("Debe ser un número positivo.")
                
        else:
            print("El valor ingresado debe corresponder a un número únicamente.")
            
#PP - Reto 10
elevarNumero()
print("\n-----------------------------------------------------------------------")
