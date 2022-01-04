########################################################################
# Elaborado por: Mónica Alfaro P y Jennifer Alvarado B.
# Fecha de creación: 22/05/2020 02:35pm
# Fecha de última modificación: 24/05/2020 02:30pm
# Versión: 3.8.2
########################################################################

#Importación de librería:

from libreriaMonicaJennifer import *

print("~~~~~~~~~~~~~~~~~~~~~~~~Lab de Listas Iterativas~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~Mónica A. y Jennifer A.~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
########################################################################
#Reto 1:

def validar1(datos):
    """
    Funcionalidad: Validar que los valores sean enteros.
    Entradas: list(plistas).
    Salidas: True/False.
    """ 
    for i in datos:
        if (isinstance(i,int)):
            continue
        else:
            return False
    return True

def ingresarElemento1():
    """
    Funcionalidad: Entrada y salida de datos. Revisa que la lista no esté vacía.
    Entradas: Las listas.
    Salidas: Comentarios y listas pares e impares.
    """
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\nReto #1: Este reto divide una lista de números en dos listas, una con los números pares y otra con los impares, correspondientemente.\n")
    listas=[[ ],[1, 2, "c", 4],[1, 2, 3, 4, 5],[2, 4, 8, 10]]
    for i in listas:
        print(i)
        if not i:
            print("La lista de números no debe ser vacía\n")
        else:
            if validar1(i):
                print("Pares e impares: "+str(separarElementos(i))+"\n")
            else:
                print("Elementos no numéricos en la lista\n")  
ingresarElemento1()

########################################################################
#Reto 2:

def ingresarElemento2():
    """
    Funcionalidad: E/S de datos.
    Entradas: int(numero),list(listas).
    Salidas: Cuantas veces aparece un número en la lista.
    """   
    while True:
        try:
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("\nReto #2: Este reto determina cuántas veces aparece un número ingresado en la lista:")
            numero=int(input("Indique el número que desea averiguar cuántas veces aparece: "))
            listas=[[ ],[11, 45, 89, -6, 0, 78, 45, 156, 12],[0,0,0,-1,-1,0,'a'],[0,0,0,-1,-1,0,-1]]
            for i in listas:
                print("\nSu lista: ",i)
                if (validar1(i)):
                    print("El número ingresado: "+str(numero)+" aparece: "+str(buscarElemento(numero,i))+" veces.")   
                else:
                    print("Ingrese sólo números enteros.")

                continue
            return False
                
        except ValueError:
                print("El valor que ingresó es inválido. Ingrese un número.")
                continue
              

#Programa Principal
ingresarElemento2()

########################################################################

#Reto 3:

def ingresarElemento3():
    """
    Funcionalidad: Entrada y salida de datos. Revisa que la lista no esté vacía.
    Entradas: Las listas.
    Salidas: Listas de vocales.
    """
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\nReto #3: Este reto indica cuáles son las vocales de una lista, sin importar el tipo de elementos que tenga.\n")
    listas=[["x", "c", "a", "b", "i", "z", "e"],["b", "f", "g", "d", "x", "j", "p"],["u", "a", "i", "o", "e"],["p", "a", "q", "o", "d"]]
    for i in listas:
        print(i)
        if not i:
            print("La lista no debe ser vacía\n")
        else:
            print("Las vocales son: "+str(crearListaVocales(i))+"\n")  
ingresarElemento3()

########################################################################

#Reto 4:

def ingresarElemento4():
    """
    Funcionalidad: E/S de datos.
    Entradas: list(lista).
    Salidas: El número mayor str(salida[0], número menor str(salida[1]), diferencia entre estos: str(salida[2]).
    """   
    while True:
        try:
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("\nReto #4: Este reto genera una lista random, mostrando el número mayor, el menor y la diferencia entre estos:")
            lista=crearLista(5)
            salida=determinarMayor(lista)
            print("\nSe generó la lista: ",lista, "el número mayor es "+str(salida[0])+ ", el número menor es "+str(salida[1])+" y la diferencia entre ellos es de "+str(salida[2]))
            return False
                
        except ValueError:
                print("Valor inválido.")
                continue
              
ingresarElemento4()

########################################################################

#Reto 5:

def ingresarElemento5():
    """
    Funcionalidad: Entrada y salida de datos. Dependiendo de la lista manda los elementos.
    Entradas: Las listas.
    Salidas: Listas con elementos insertados.
    """
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\nReto #5: Este reto inserta un elemento definido en una lista después de otro elemento, también definido previamente.\n")
    listas=[["p", "q", "x", "n", "x",],["mate", "conta", "intro", "inglés", "deportiva"],["reto", "nebulosa", "divide", "vencerás", "examen"],[]]
    for i in listas:
        print(i)
        if i==listas[0]:
            elemento1="x"
            elemento2="hoy"
            print("Elemento 1: ",elemento1)
            print("Elemento 2: ",elemento2)
        elif i==listas[1]:
            elemento1="intro"
            elemento2="taller"
            print("Elemento 1: ",elemento1)
            print("Elemento 2: ",elemento2)
        elif i==listas[2]:
            elemento1="empollar"
            elemento2="huevo"
            print("Elemento 1: ",elemento1)
            print("Elemento 2: ",elemento2)
        else:
            elemento1="lunes"
            elemento2="martes"
            print("Elemento 1: ",elemento1)
            print("Elemento 2: ",elemento2)
        print("La nueva lista es: "+str(insertarElemento(i,elemento1,elemento2))+"\n")
  
ingresarElemento5()

########################################################################

#Reto 6:

def ingresarElemento6():
    """
    Funcionalidad: E/S de datos.
    Entradas: list(listas).
    Salidas: Lista libre de duplicados. 
    """   
    while True:
        try:
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("\nReto #6: Este reto permite eliminar duplicados de una lista:")
            listas=[[1,1,3,8,8,4,9,4,2],["a", "c", "m", "c", "a"]]
            for i in listas:
                print("\nSu lista: ",i)
                print("Su lista sin duplicados: "+str(eliminarElementosRepet(i)))
            return False
                
        except ValueError:
                print("Valor inválido.")
                continue
              

#Programa Principal
ingresarElemento6()

########################################################################

#Reto 7:

def validar7(nume):
    """
    Funcionalidad: Revisar que el número sea mayor a cero.
    Entradas: Número(nume).
    Salidas: True.
    """ 
    if nume>0:
        return True

def ingresarElemento7():
    """
    Funcionalidad: Entrada y salida de datos. Revisa que la lista no esté vacía.
    Entradas: Las listas.
    Salidas: Comentarios y listas parea e impares.
    """ 
    while True:
        try:
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("\nReto #7: Este reto crea una sucesión ULAM, si es par lo divide entre 2 y si es impar lo multiplica por 3 y le suma 1.\n")
            numero=int(input("Ingrese el número para iniciar la secuencia: "))
            if validar7(numero):
                print("La sucesión ULAM es: "+str(crearSecuencia(numero)))
                return False
            else:
                print("Debe ser un número mayor a 0")
        except ValueError:
            print("Debe ser un número entero.\n")
            continue
ingresarElemento7()

########################################################################

#Reto 8:

def ingresarElemento8():
    """
    Funcionalidad: E/S de datos.
    Entradas: list(listas).
    Salidas: True/False.
    """   
    while True:
        try:
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("\nReto #8: Este reto permite averiguar si se alternan pares e impares en una lista:")
            listas=[[2,5,8,7,10],[1,2,3,4,6],[1,2,3,4,5],[0,0,0,-1,-1,0,'a'],[]]
            for i in listas:
                print("\nSu lista: ",i)
                if not i:
                    print("La lista no puede estar vacía.")
                else:
                    if (validar1(i)):
                        print("¿Se alternan? "+str(alternarParesImpares(i)))
                    else:
                        print("Ingrese sólo números enteros.")
                    continue
                return False
                
        except ValueError:
                print("Valor inválido.")
                continue
              

#Programa Principal
ingresarElemento8()

########################################################################

#Reto 9:

def ingresarElemento9():
    """
    Funcionalidad: Entrada y salida de datos. Revisa que la lista no esté vacía.
    Entradas: Las listas.
    Salidas: Comentarios y listas pares e impares.
    """
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\nReto #9: Este reto indica si una lista es ascendente o no.\n")
    listas=[[2,4,5,6,7],[8,7,2,4,5]]
    for i in listas:
        print(i)
        if not i:
            print("La lista de números no debe ser vacía\n")
        else:
            if validar1(i):
                print("¿Es ascendente? "+str(listaAscendente(i))+"\n")
            else:
                print("Elementos no numéricos en la lista\n")
                
        
ingresarElemento9()

########################################################################

#Reto 10:

def ingresarElemento10():
    """
    Funcionalidad: E/S de datos.
    Entradas: int(numero), list(listas).
    Salidas: Lista con elementos duplicados según int(numero).
    """   
    while True:
        try:
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("\nReto #10: Este reto permite replicar los valores de una lista.")
            numero=int(input("Indique cuántas veces desea replicar los valores  de la lista: "))
            if(validar7(numero)):
                listas=[[1,3,3,7],[0,0,0,-1,-1,0,'a']]
                for i in listas:
                    print("\nSu lista: ",i)
                    print("Lista con los elementos replicados ",numero, " veces: "+str(replicarElementos(numero,i)))
                return False
            else:
                print("Ingrese sólo números enteros mayores a 0.")
                continue
                
        except ValueError:
                print("El valor que ingresó es inválido. Ingrese un número.")
                continue
              
#Programa Principal
ingresarElemento10()

########################################################################

#Reto 11:

def validar11(datos):
    """
    Funcionalidad: Validar que los elementos de las listas sean únicamente numéricos.
    Entradas: Las litas que no están vacías.
    Salidas: True(solo numéricas) o False(con letras).
    """
    for i in datos:
        for numeros in i:
            if isinstance(numeros,int):
                continue
            else:
                return False
    return True

def ingresarElemento11():
    """
    Funcionalidad: Entrada y salida de datos. Revisa que la lista no esté vacía.
    Entradas: Las listas.
    Salidas: Comentarios y listas pares e impares.
    """
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\nReto #11: Este reto muestra la diferencia entre dos conjuntos.\n")
    listas=[[[1,2,3,4,5,6],[9,8,7,6,5]],[[9,8,7,6,5],[1,2,3,4,5,6]]]
    for i in listas:
        if validar11(i):
            print(i)
            print("Los elementos diferentes son: "+str(diferenciarConjuntos(i[0],i[1]))+"\n")
        else:
            print("Deben ser listas válidas y numéricas.")

ingresarElemento11()

########################################################################

#Reto 12:

def ingresarElemento12():
    """
    Funcionalidad: E/S de datos.
    Entradas: list(lista1), list(lista2).
    Salidas: Lista unida con otra sin elementos duplicados entre ellas.
    """   
    while True:
        try:
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("\nReto #12: Este reto permite unir dos listas en una sola sin duplicados:")
            lista1=[1,3,7,9]
            lista2=[0,-1,10,3,'a',7]
            print("\nSu lista 1: ",lista1)
            print("Su lista 2: ",lista2)
            print("Lista nueva sin los elementos duplicados "+str(unirConjuntos(lista1,lista2)))
            return False
                
        except ValueError:
                print("Valor inválido.")
                continue
              
#Programa Principal
ingresarElemento12()

########################################################################

#Reto 13:

def ingresarElemento13():
    """
    Funcionalidad: Entrada y salida de datos. Revisa que la lista no esté vacía.
    Entradas: Las listas.
    Salidas: Comentarios y listas pares e impares.
    """
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\nReto #13: Este reto muestra la intercepción entre dos conjuntos.\n")
    listas=[[[1,2,3,4,5,6,7,8,9,10],[9,10,11,12,13,14,15,]],[[1,2,3,4,5,6,7,8,9,10],[]],[[1,2,3,4,5],[6,7,8,9,10]]]
    for i in listas:
        if validar11(i):
            print(i)
            print("Los elementos que coinciden son: "+str(interceptarConjuntos(i[0],i[1]))+"\n")
        else:
            print("Deben ser listas válidas y numéricas.")

ingresarElemento13()
########################################################################

#Reto 14:

def validarListas14(plista1,plista2):
    """
    Funcionalidad: Validar que las listas tengan la misma longitud.
    Entradas: list(plista1), list(plista2).
    Salidas: True/False.
    """ 
    if(len(plista1)==len(plista2)):
        return True

def validarLista14(plista):
    """
    Funcionalidad: Validar que los valores sean enteros.
    Entradas: list(plista).
    Salidas: True/False. 
    """ 
    for i in plista:
            if(isinstance(i,int)):
                continue
            else:
                return False
    return True

def ingresarElemento14():
    """
    Funcionalidad: E/S de datos.
    Entradas: list(lista1), list(lista2).
    Salidas: Multiplicación lineal de listas.
    """   
    while True:
        try:
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("\nReto #14: Este reto permite multiplicar dos listas:")
            lista1=[1,2,3]
            lista2=[4,5,9]
            if (validarListas14(lista1,lista2) and validarLista14(lista1) and validarLista14(lista2)):
                print("\nSu lista 1: ",lista1)
                print("Su lista 2: ",lista2)
                print("Lista multiplicada: "+str(multiplicarListas(lista1,lista2)))
                return False
            else:
                print("La lista debe tener sólo valores enteros y deben ser la misma cantidad de dígitos.")
                return True
                
        except ValueError:
                print("El valor que ingresó es inválido. Ingrese un número.")
                continue
              
#Programa Principal
ingresarElemento14()
