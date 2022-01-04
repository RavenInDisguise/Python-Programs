########################################################################
# Elaborado por: Mónica Alfaro P
# Fecha de creación: 13/03/2020 12:45pm
# Fecha de última modificación: 13/03/2020 XX:XXpm
# Versión: 3.8.1
########################################################################


#Funciones

#Ejemplo de definición de una función:
#Funcionalidad: Contar la cantidad de dígitos de un entero ingresado.
#Entrada: Entero int(num)
#Salida: Cantidad de dígitos (contador).
def mostrarDigitos(num):
    contador=0
    if(isinstance(num,int)):
        print("Los números del entero ingresado son: ")
        while (num!=0):
            print(num%10)
            num=num//10
            contador+=1
        print("Tiene un total de: ",contador, " dígitos.\n")
        return 
    else:
        print("Número no entero.")

#Ejemplo de definición de una función:
#Funcionalidad: Mostrar los pares del entero ingresado.
#Entrada: Entero int(num)
#Salida: Números pares del entero.
def mostrarPares (num):
    if(isinstance(num,int)):
        print("Los números pares del entero ingresado son: ")
        while (num!=0):
                if(num%2==0):
                    print(num%10,"\n")
                else:
                    ""
                num=num//10
        return 
    else:
        print("Número no entero.")

#Ejemplo de definición de una función:
#Funcionalidad: Definir si hay un cero en el número entero ingresado.
#Entrada: int(num)
#Salida: ¿Posee o no posee al menos un cero?
def encontrarAlmenosUnCero (num):
    if(isinstance(num,int)):
        if(num%10==0):
            print("Posee al menos un cero.\n")
            while (num!=0):
                num=num//10
            return
        else:
            print("No posee ningún cero.\n")
    else:
        print("Número no entero.")

#Ejemplo de definición de una función:
#Funcionalidad: Multiplicar los números impares ingresados.
#Entrada: int(numero)
#Salida: Multiplicación de los impares de int(numero). 
def multiplicarImpares (num):
    mult=1
    if(isinstance(num,int)):
        while(num!=0):
            numVal=num%10
            if(numVal%2!=0):
                mult=mult*numVal
            else: ""
            num=num//10
        print("El número se repite esta cantidad de veces: ",mult)
        return
    else:
        print("No es un número entero")

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

#Ejemplo de definición de una función:
#Funcionalidad: Saber si el número ingresado es primo o no.
#Entrada: int(num)
#Salida: Si es primo o no. 
def esNumeroPrimo(num):
    contador=1
    numeroPrimo=0
    while(contador<=num):
        if(num%contador==0):
            numeroPrimo+=1
        else:
            ""
        contador+=1
    if(numeroPrimo==2):
        print("Es primo.")
    else:
        print("No es primo.")
    return

#Programa principal
        
#Switch case
def menu():     
      print("\n 1)Mostrar los elementos de una cifra."
      "\n 2)Mostrar los valores pares de una cifra."
      "\n 3)Encontrar al menos un cero en una cifra."
      "\n 4)Multiplicar los números impares en una cifra."
      "\n 5)Contar los números repetidos en una cifra."
      "\n 6)Determinar el número mayor de una cifra."
      "\n 7)Elevar una cifra a una potencia."
      "\n 8)Decifrar si una cifra es prima o no."
      "\n 9)Sumar los múltiplos de un intervalo de dos cifras ingresadas."
      "\n 10)Decifrar si una cifra es binaria o no.")

print("¡Hola!")
menu()
opcion=int(input("Escoja una opción: "))

if(opcion==1):
        numero=int(input("Inserte un número entero: "))
        mostrarDigitos(numero)
elif(opcion==2):
        numero=int(input("Inserte un número entero: "))
        mostrarPares(numero)
elif(opcion==3):
        numero=int(input("Inserte un número entero: "))
        encontrarAlmenosUnCero(numero)
elif(opcion==4):
        numero=int(input("Inserte un número entero: "))
        multiplicarImpares(numero)
elif(opcion==5):
        numero=int(input("Inserte un número entero: "))
        numeroRepe=int(input("Inserte el número entero que desea saber si se repite: "))
        contarRepeticiones(numero, numeroRepe)
elif(opcion==6):
        numero=int(input("Inserte un número entero: "))
        determinarMayor(numero)
elif(opcion==7):
        numero=int(input("Inserte un número entero: "))
        numeroPot=int(input("Inserte un número entero al que desea elevar: "))
        elevarNumero(numero, numeroPot)
elif(opcion==8):
        numero=int(input("Inserte un número entero: "))
        esNumeroPrimo(numero)
#elif(opcion==9)
#elif(opcion==10)

    
    

    
    
    
