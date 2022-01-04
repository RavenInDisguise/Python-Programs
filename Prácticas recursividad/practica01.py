
#Validaciones

def validarValores(valor):
    """
    Funcionalidad: Valida si los valores son un número entero o no.
    Entrada: El valor.
    Salida: True/None.
    """
    if isinstance(valor,int):
        return True

def validarNum(num):
    """
    Funcionalidad: Valida si el número es positivo.
    Entrada: El número int(num).
    Salida: True/None.
    """
    if(0<=num):
        return True

def validarDigito(dig):
    if(0<dig<=9):
        return True

#Funciones generales

#Función desarrollada en un laboratorio anterior:
def esPar(num):
    """
    Funcionalidad: Encontrar si el número es par o no.
    Entrada: El número int(num).
    Salida: True/False.
    """
    if(num%2==0):
        return True
    else:
        return False

#Funciones recursivas

#Reto 2
    
def esParRecursivo(num):
    """
    Funcionalidad: Encuentra si la cifra posee un número par.
    Entrada: El número int(num).
    Salida: Si tiene o no un número par.
    """
    if num==0:
        return "La cifra numérica no posee ningún par."
    elif esPar(num):
        return "La cifra numérica, posee al menos un par."
    else:
        return esParRecursivo(num//10)

#Reto 4

def multiplicarImparesRec(num):
    """
    Funcionalidad: Multiplicar los números impares encontrados en un número.
    Entrada: El número int(num).
    Salida: La multiplicación de los números pares.
    """
    if num==1:
        return 1
    elif num==0:
        return 0
    elif esPar(num)==False:
        return num%10 * multiplicarImparesRec(num//10)
    else:
        return multiplicarImparesRec(num//10)

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

########################################################################

#Funciones principales
    
#Reto 2:

def descubrirPar():
    """
    Funcionalidad: Encuentra si la cifra posee un número par.
    Entrada: Ninguna.
    Salida: Si tiene o no un número par.
    """
    print("\nReto 2: Encontrar si existe al menos un número par en un número.")
    listaNumeros=["Hola",1357,1234]
    for numero in listaNumeros:
        print("\nSu valor: "+str(numero))
        if(validarValores(numero)):
            print(esParRecursivo(abs(numero)))
        else:
            print("El valor ingresado debe corresponder a un número únicamente.")
    

#Reto 4
        
def multiplicarImp():
    """
    Funcionalidad: Multiplicar los números impares encontrados en un número.
    Entrada: Ninguna.
    Salida: La multiplicación de los números pares.
    """
    print("\nReto 4: Multiplicar los números impares encontrados en un número.")
    listaNumeros=["1223a",12345,246]
    for numero in listaNumeros:
        print("\nSu valor: "+str(numero))
        if(validarValores(numero)):
            print("La multiplicación impar es:",multiplicarImparesRec(abs(numero)))
        else:
            print("El valor ingresado debe corresponder a un número únicamente.")
           
#Reto 6

def determinarRepeticiones():
    """
    Funcionalidad: Determinar cuántas veces aparece un dígito en un número.
    Entrada: El número int(num) y el dígito int(dig).
    Salida: La cantidad de veces que aparece.
    """
    print("\nReto 6: Determinar la cantidad de dígitos en una cifra:")
    listaNumeros=[(1234567123,2),(3451233453,3),(234565,9)]
    for numero in listaNumeros:
        print("\nSu valor: "+str(numero[0]))
        if(validarValores(numero[0])):
            if(validarNum(numero[0])):
                print("Su dígito: "+str(numero[1]))
                if(validarDigito(numero[1]) and validarValores(numero[1])):
                    print("Cantidad de veces que aparece el dígito "+str(numero[1])+" en "+str(numero)+":",determinarCantidad(numero[0],numero[1]))
                else:
                    print("Debe ingresar un dígito del 0 al 9.")
            else:
                print("El número debe ser positivo.")
        else:
            print("El valor ingresado debe corresponder a un número positivo únicamente.")
           

#Reto 8
        
def descubrirPrimo():
    """
    Funcionalidad: Descubrir si un número es primo.
    Entrada: Ninguna.
    Salida: True/False.
    """
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

#Reto 10
        
def elevarNumero():
    """
    Funcionalidad: Elevar un número a la potencia ingresada.
    Entrada: Ninguna.
    Salida: El número elevado a la potencia.
    """
    print("\nReto 8: Determinar si un número es primo.")
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



#Programa principal
        
#Reto 2
descubrirPar()

#Reto 3
multiplicarImp()

#Reto 6
determinarRepeticiones()

#Reto 8
descubrirPrimo()

#Reto 10
elevarNumero()



        

