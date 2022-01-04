#Elaborado por: Mónica Alfaro P y Jennifer Alvarado B.
#Fecha de creación: 15/03/20 12:58 p.m
#Última modificación: 24/05/2020 02:30pm
#Versión: 3.8.2

########################################################################

#Importación de librerías:
import random

#Funciones de la tarea 01:

########################################################################

#Funcion reto 1:

def formarNumInverso(num):
    """
    Funcionalidad: Invertir número.
    Entradas: El número int(num).
    Salidas: Número invertido int(inverso)
    """
    inverso=0
    while (num>0):
        residuo=num%10
        inverso=(inverso*10)+residuo
        num=num//10
    return inverso
    
        
########################################################################

#Funciones reto 2:

def esPar(pnumero):
    """
    Funcionalidad: Averiguar si un número es par o no.
    Entradas: El número int(pnumero).
    Salidas: Verdadero o falso, de acuerdo a si cumple con el condicional o no.
    """
    if(pnumero%2==0):
        return True
    
def obtenerPares (pnum):
    """
    Funcionalidad: Mostrar los números pares que aparezcan en orden.
    Entradas: El número int(pnum).
    Salidas: Números pares encontrados en orden int(inverso).
    """
    inverso=0
    while(pnum>0):
        residuo=pnum%10
        if (esPar(residuo)):
            inverso=(inverso*10)+residuo #Se sacan los números pares, pero al revés.
        pnum=pnum//10
    return formarNumInverso(inverso)#Se invierten los números pares para que se muestren en orden.
                                    #Reutilizando la función formarNumInverso().


########################################################################

#Función reto 3:

def obtenerFactorial(num):
    """
    Funcionalidad: Obtener factorial de un número ingresado.
    Entradas: El número (num).
    Salidas: El factorial del número ingresado int(resultado).
    """
    i=1
    resultado=1
    while (i<=num):
        resultado=resultado*i
        i=i+1
    return resultado


########################################################################

#Funcion reto 4:

def obtenerCantidades(pnum):
    """
    Funcionalidad: Obtener cantidad de pares e impares.
    Entradas: El número (pnum).
    Salidas: contadorPar (int), contadorImpar (int). Cantidad de pares e impares de un número.
    """
    contadorPar=0
    contadorImpar=0
    while (pnum!=0):
        div=pnum%10
        if (esPar(pnum)): #Reutilizo la función esPar() porque es la misma validación.
            contadorPar+=1
        else:
            contadorImpar+=1
        pnum=pnum//10
    return contadorPar, contadorImpar


########################################################################

#Funcion reto 5:

def obtenerSumatoria(numero):
    """
    Funcionalidad: Obtener la sumatoria i**2.
    Entradas: El número ingresado int(numero).
    Salidas: Resultado de la sumatoria int(sumatoria).
    """
    i=1
    sumatoria=0
    while (i<=numero):
        sumatoria=(i**2)+sumatoria
        i+=1
    return sumatoria


########################################################################

#Funcion reto 6:

def convertirABinario (pnum):
    """
    Funcionalidad: Convertir un número decimal a binario.
    Entradas: El número int(pnum).
    Salidas: El número binario str(binario). 
    """
    binario=" "
    while(pnum//2!=0):
        if(pnum%2==0):
            binario="0"+binario
        else:
            binario="1"+binario
        pnum=pnum//2
    return str(pnum)+binario
        


########################################################################

#Funcion reto 7:

#Se reutiliza la función formarNumInverso() del reto #1.


########################################################################

#Funciones de la tarea 02:

########################################################################

#Función reto 1:

def diferenciarValores(num):
    """
    Funcionalidad: Mostrar el dígito mayor y el menor de un número.
    Entradas: El número int(num).
    Salidas: El dígito mayor y el menor de un número int(numMay,numMen). 
    """
    numMay=0
    numMen=num
    while num>0:
        if num%10>numMay:
            numMay=num%10
        if num%10<numMen:
            numMen=num%10
        num=num//10
    return numMay,numMen


########################################################################

#Función reto 2:

def convertirDecimal(pnum):
    """
    Funcionalidad: Convertir a decimal un número binario.
    Entradas: El número int(pnum).
    Salidas: Número decimal int(decimal). 
    """
    decimal=0
    while True:
        i=1
        while pnum>0:
            decimal=(pnum%10*i)+decimal
            i=i*2
            pnum=pnum//10
        return decimal

########################################################################

#Función reto 3:

def convertirOctal(num):
    """
    Funcionalidad: Convertir a octal un número.
    Entradas: El número int(pnum).
    Salidas: Número convertido a octal.
    """
    residuo=0
    while True:
        while (num//8)>0:
            residuo=(residuo*10)+(num%8)
            num=num//8
        if num//8==0:
            residuo=(residuo*10)+(num%8)
        return formarNumInverso(residuo) #Reutilizamos la función formarNumInverso() para invertir el número. 
    
########################################################################

#Función reto 4:

def revisarCapicua(num):
    """
    Funcionalidad: Revisa si el número es capicúa.
    Entradas: El número int(pnum) y el número inverso.
    Salidas: True (si son iguales) o False (si no son iguales).
    """
    salida=formarNumInverso(num)
    if(num==salida):
        return True

########################################################################

#Función reto 5:

def revisarDiferencia(numero1, numero2):
    """
    Funcionalidad: Contar si los números son iguales.
    Entradas: El número 1 cortado int(numero1)y int(numero2).
    Salidas: El contador int(contador2).
    """
    contador2=0
    while (numero2>0):
        div2=numero2%10
        if  (div2!=numero1):
            contador2=contador2
        else:
            contador2+= 1
        numero2=numero2//10
    return contador2

def compararNum(num1, num2):
    """
    Funcionalidad: Generar un número con los dígitos distintos.
    Entradas: Los números ingresados int(num1, num2).
    Salidas: Los números distintos en caso de existir int(diferencia), o False.
    """
    diferencia=" "
    contador=0
    while (num1>0):
        numero=num1%10
        if revisarDiferencia(numero, num2)==0:
            diferencia=str(numero)+diferencia
            contador+=1
        num1=num1//10
    if(contador==0):
        return False
    return diferencia
            
########################################################################

#Funciones reto 6:

def esBisiesto(anno):
    """
    Funcionalidad: Revisar si es bisiesto.
    Entradas: Un año.
    Salidas: True (si es bisiesti) o False (si no es bisiesto).
    """ 
    if(anno%4==0):
        return True
    
def encontrarBisiestos(anno1,anno2):
    """
    Funcionalidad: Revisar si es bisiesto.
    Entradas: Un año.
    Salidas: True (si es bisiesti) o False (si no es bisiesto).
    """ 
    bisiesto=" "
    while(anno2>=anno1):
        if(esBisiesto(anno2)):
            annoBis=anno2
            bisiesto=str(annoBis)+"\n"+bisiesto
        anno2=anno2-1
    return bisiesto

########################################################################

#Funciones del Lab de listas iterativas (strings)

########################################################################

#Función reto 1:

def separarElementos (lista):
    """
    Funcionalidad: Separar una listas en pares e impares.
    Entradas: La lista.
    Salidas: Lista nueva con dos listas (pares e impares). 
    """ 
    listaPar=[]
    listaImpar=[]
    for i in lista:
        if esPar(i):
            listaPar.extend([i])
        else:
            listaImpar.extend([i])
    lista=[listaPar,listaImpar]
    return lista
########################################################################

#Función reto 2:

def buscarElemento(pnumero,plista):
    """
    Funcionalidad: Busca un elemento y cuenta cuántas veces aparece.
    Entradas: int(pnumero), list(plista).
    Salidas: Contador de cuántas veces se repite un número int(contador).
    """  
    contador=0
    for i in plista:
        if(i==pnumero):
            contador+=1
        i+=1
    return contador

########################################################################

#Función reto 3:

def crearListaVocales(lista):
    """
    Funcionalidad: Crear una lista que contenga las vocales de la lista original.
    Entradas: La lista.
    Salidas: Lista nueva solamente con las vocales
    """ 
    listaVocales=[]
    for i in lista:
        if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
            listaVocales.extend([i])
        else:
            continue
    return listaVocales

########################################################################

#Función reto 4:

def crearLista(pnumero):
    """
    Funcionalidad: Crear una lista random.
    Entradas: int(pnumero).
    Salidas: Lista random del tamaño pnumero: list(lista).
    """  
    lista=[random.randint(0,99) for _ in range(pnumero)]
    return lista

def determinarMayor (plista):
    """
    Funcionalidad: Determinar número mayor, menor y diferencia entre estos de una lista.
    Entradas: list(plista).
    Salidas: Número mayor int(numMayor), número menor int(numMenor), diferencia.
    """  
    numMayor=0
    numMenor=99
    for i in plista:
        if(i>=numMayor):
            numMayor=i
        elif(i<=numMenor):
            numMenor=i
    return numMayor,numMenor, numMayor-numMenor

########################################################################

#Función reto 5:

def crearSecuencia (lista):
    """
    Funcionalidad: Crear una sucesión ULAM a partir de un número.
    Entradas: Número.
    Salidas: Lista de la secuencia.
    """ 
    secuencia=[]
    secuencia.extend([lista])
    while secuencia[-1]!=1:
        if esPar(secuencia[-1]):
            resultado=(secuencia[-1])/2
        else:
            resultado=((secuencia[-1])*3)+1
        resultado=int(resultado)
        secuencia.extend([resultado])
    return secuencia

########################################################################

#Función reto 6:

def eliminarElementosRepet(plista):
    """
    Funcionalidad: Eliminar elementos repetidos de una lista y mostrarlo en otra lista.
    Entradas: list(plista).
    Salidas: Lista sin elementos repetidos list(lista2).
    """
    lista2=[]
    for i in plista:
        if i not in lista2:
            lista2.append(i)
    return lista2

########################################################################

#Función reto 7:

def insertarElemento(lista,elemento1,elemento2):
    """
    Funcionalidad: Insertar el elemento 2 después del elemento 1.
    y si está bien, elimina el último.
    Entradas: Lista y elementos.
    Salidas: Nueva lista con elementos insertados.
    """
    nuevaLista=[]
    for i in lista:
        if i==elemento1:
            nuevaLista.extend([i,elemento2])
        else:
            nuevaLista.extend([i])
    return nuevaLista

########################################################################

#Función reto 8:

def alternarParesImpares(plista):
    """
    Funcionalidad: Averiguar si se alternan los números pares e impares.
    Entradas: list (plista).
    Salidas: Valor=True/False.
    """
    valor=""
    i=0
    listaNueva1=plista[1::2]
    listaNueva2=plista[0::2]
    for i in plista:
        if(plista[0]%2==0):
            for i in listaNueva1:
                if(i%2!=0):
                    for i  in listaNueva2:
                        if(i%2==0):
                            valor=True
                        else:
                            valor=False
                
        elif(plista[0]%2!=0):
            for i in listaNueva1:
                if(i%2==0):
                    for i  in listaNueva2:
                        if(i%2!=0):
                            valor=True
                        else:
                            valor=False
    return valor
########################################################################

#Función reto 9:

def listaAscendente(lista):
    """
    Funcionalidad: Verificar si una lista es ascendente. Compara los dos últimos dígitos
    y si está bien, elimina el último.
    Entradas: Lista.
    Salidas: True (es ascendente) o False (no es ascendente).
    """
    for i in lista:
        if lista[-1]>lista[-2]:
            lista.pop(-1)
        else:
            return False
    return True

########################################################################

#Función reto 10:

def replicarElementos(pnumero, plista):
    """
    Funcionalidad: Replica los elementos de una lista una cantidad n de veces y mostrarlo en otra lista.
    Entradas: int(pnumero), list(plista).
    Salidas: Lista replicada n veces, list(nuevaLista).
    """
    num=0
    nuevaLista=[]
    for i in plista:
        while (num!=pnumero):
            nuevaLista.append(i)
            num+=1
        num=0      
    return nuevaLista

########################################################################

#Función reto 11:

def diferenciarConjuntos(conjunto1,conjunto2):
    """
    Funcionalidad: Saca los elementos diferentes entre dos conjuntos.
    Entradas: lista1(conjunto1),lista2(cojunto2).
    Salidas: list(nuevaLista).
    """
    listaNueva=[]
    repetir=False
    for i in range(len(conjunto1)):
        for i1 in range(len(conjunto2)):
            if conjunto1[i]==conjunto2[i1]:
                repetir=True
            else:
                continue
        if repetir==False:
            listaNueva=listaNueva+[conjunto1[i]]
        repetir=False
    return listaNueva
            

########################################################################

#Función reto 12:

def unirConjuntos(plista1,plista2):
    """
    Funcionalidad: Unir dos listas sin duplicados entre ellas y mostrarlo en otra lista.
    Entradas: list(plista1),list(plista2).
    Salidas: list(nuevaLista).
    """
    nuevaLista=[]
    for i in plista1:
        if(plista2.count(i)==0):
            nuevaLista.append(i)
    for i in plista2:
        if(plista1.count(i)==0):
            nuevaLista.append(i)
    return nuevaLista
########################################################################

#Función reto 13:

def interceptarConjuntos(conjunto1,conjunto2):
    """
    Funcionalidad: Saca la intercepción entre dos conjuntos.
    Entradas: lista1(conjunto1),lista2(conjunto2).
    Salidas: lista(nuevaLista).
    """
    listaNueva=[]
    for i in range(len(conjunto1)):
        for i1 in range(len(conjunto2)):
            if conjunto1[i]==conjunto2[i1]:
                listaNueva=listaNueva+[conjunto1[i]]
            else:
                continue
    return listaNueva

########################################################################

#Función reto 14:

def multiplicarListas(plista1,plista2):
    """
    Funcionalidad: Multiplicar linealmente dos listas y mostrarlo en otra lista.
    Entradas: list(plista1),list(plista2).
    Salidas: list(nuevaLista).
    """ 
    nuevaLista=[]
    e=0
    for i in plista1:
            resultado=int(i*plista2[e])
            nuevaLista.append(resultado)
            e+=1
    return nuevaLista  
