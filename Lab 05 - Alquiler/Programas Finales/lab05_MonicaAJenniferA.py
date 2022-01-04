########################################################################
# Elaborado por: Mónica Alfaro P y Jennifer Alvarado B.
# Fecha de creación: 22/06/2020 12:10
# Fecha de última modificación: 23/06/2020 11:25
# Versión: 3.8.2
########################################################################

#Importación de librerías:

from libreriaAlquiler import *
import random
import time
import pickle
import sys

########################################################################

#Declaracion de variable global:

nomArchivo="edificio"

########################################################################

def validarNumero(numero):
    """
    Funcionalidad: Validar si es un número positivo.
    Entrada: El número int(numero).
    Salida: True/None, depende del resultado del condicional.
    """
    if(numero>0):
        return True

def ingresarDatosAlquiler():
    """
    Funcionalidad: Ingresar los datos del tamaño del edificio.
    Entrada: Los pisos (numeroFila) y los locales (numeroColumna).
    Salida: Una matriz hecha con esos valores ingresados.
    """
    while True:
        try:
            numeroFila=int(input("\nIngrese la cantidad de pisos que posee el edificio: "))
            if(validarNumero(numeroFila)):
                while True:
                    numeroColumna=int(input("Ingrese la cantidad de locales que posee el edificio: "))
                    if(validarNumero(numeroColumna)):
                        matrizLocal=generarMatrizVacia(numeroColumna,numeroFila)
                        print("Este es el estado del local ingresado: \n",generarMatrizVacia(numeroColumna,numeroFila))
                        graba(nomArchivo,matrizLocal)
                        lista=lee(nomArchivo)
                        print("\nSu edificio almacenado en archivos: \n",lista)
                        menuPrincipal(matrizLocal)
                   
                    else:
                        print("Ingrese una cantidad de locales positivos mayores que cero.\n")
                        continue
               
            else:
                print("Ingrese una cantidad de pisos positivos mayores que cero.")
                continue
            return False
        
        except ValueError:
            print("Ingrese números enteros.")
            continue

########################################################################

def ingresaralquilerLocal(matrizLocal):
    """
    Funcionalidad: Ingresar un alquiler al edificio.
    Entrada: Número de piso (pisoIn) y número de local (localIn).
    Salida: Un local alquilado.
    """
    print("\nAlquiler de un local:")
    while True:
        try:
            
            pisoIn=int(input("\nIngrese el número de piso: "))
            if(validarNumero(pisoIn)):
                while True:
                    localIn=int(input("Ingrese el número de local: "))
                    if(validarNumero(localIn)):
                        print(alquilerLocal(matrizLocal,pisoIn,localIn))
                        menuPrincipal(matrizLocal)
                    else:
                        print("Ingrese una cantidad de locales positivos mayores que cero.\n")
                        continue
            else:
                print("Ingrese una cantidad de pisos positivos mayores que cero.")
                continue
            return False
        
        except ValueError:
            print("Ingrese números enteros.")
            continue

########################################################################

def ingresarMonto(matrizLocal):
    """
    Funcionalidad: Modifical el monto de alquiler.
    Entrada: Número de piso (pisoIn) y número de local (localIn).
    Salida: Un monto de alquiler modificado.
    """
    print("\nModificar monto de alquiler:")
    while True:
        try:
            pisoIn=int(input("\nIngrese el número de piso: "))
            if(validarNumero(pisoIn)):
                while True:
                    localIn=int(input("Ingrese el número de local: "))
                    if(validarNumero(localIn)):
                        print(modificarRenta(matrizLocal,pisoIn,localIn))
                        menuPrincipal(matrizLocal)
                    else:
                        print("Ingrese una cantidad de locales positivos mayores que cero.\n")
                        continue
            else:
                print("Ingrese una cantidad de pisos positivos mayores que cero.")
                continue
            return False
    
        except ValueError:
            print("Ingrese números enteros.")
            continue

########################################################################

def ingresarDesalojo(matrizLocal):
    """
    Funcionalidad: Desalojar un local.
    Entrada: Número de piso (pisoIn) y número de local (localIn).
    Salida: Un local desalojado.
    """
    print("\nDesalojar local:")
    while True:
        try:
            pisoIn=int(input("\nIngrese el número de piso: "))
            if(validarNumero(pisoIn)):
                while True:
                    localIn=int(input("Ingrese el número de local: "))
                    if(validarNumero(localIn)):
                        print(desalojarPiso(matrizLocal,pisoIn,localIn))
                        menuPrincipal(matrizLocal)
                    else:
                        print("Ingrese una cantidad de locales positivos mayores que cero.\n")
                        continue
            else:
                print("Ingrese una cantidad de pisos positivos mayores que cero.")
                continue
            return False
    
        except ValueError:
            print("Ingrese números enteros.")
            continue

########################################################################

def mostrarLocales(matrizLocal):
    """
    Funcionalidad: Mostrar un local.
    Entrada: Número de piso (pisoIn) y número de local (localIn).
    Salida: El local las ganancias del local.
    """
    print("\nGanancias de un local:")
    while True:
        try:
            pisoIn=int(input("\nIngrese el número de piso: "))
            if(validarNumero(pisoIn)):
                while True:
                    localIn=int(input("Ingrese el número de local: "))
                    if(validarNumero(localIn)):
                        print("Las ganancias de este local son: ",mostrarLocal(matrizLocal,pisoIn,localIn))
                        return False
                    else:
                        print("Ingrese una cantidad de locales positivos mayores que cero.\n")
                        continue
            else:
                print("Ingrese una cantidad de pisos positivos mayores que cero.")
                continue
            return False
        
        except ValueError:
            print("Ingrese números enteros.")
            continue
        
########################################################################

def mostrarPisos(matrizLocal):
    """
    Funcionalidad: Mostrar las ganancias de un piso.
    Entrada: Número de piso (pisoIn).
    Salida: Ganancias de un piso.
    """
    print("\nGanancias de un piso:")
    while True:
        try:
            pisoIn=int(input("\nIngrese el número de piso: "))
            if(validarNumero(pisoIn)):
                print("El monto total de ganancias del piso es:",mostrarPiso(matrizLocal,pisoIn))
                return False
            else:
                print("Ingrese una cantidad de pisos positivos mayores que cero.")
                continue

        except ValueError:
            print("Ingrese números enteros.")
            continue

########################################################################

def mostrarColumnas(matrizLocal):
    """
    Funcionalidad: Mostrar las ganancias de los locales por columna.
    Entrada: La columna int(columna).
    Salida: Las ganancias por columna.
    """
    print("\nGanancias de locales por columna:")
    while True:
        try:
            columna=int(input("\nIngrese el número de columna que desea observar los montos: "))
            if(validarNumero(columna)):
                print("\nEl monto total de ganancias de la columna es:",mostrarColumna(matrizLocal,columna))
                return False
            else:
                print("Ingrese una columna con un número positivo mayor que cero.")
        
        except ValueError:
            print("Ingrese números enteros.")
            continue

########################################################################    

def mostrarTotalidad(matrizLocal):
    """
    Funcionalidad: Mostrar totalidad de ganancias de todos los locales existentes.
    Entrada: La matriz (matrizLocal).
    Salida: Las ganancias totales de todos los locales existentes.
    """
    print("\nGanancias totales:")
    while True:
        try:
            print("\nEl monto total de ganancias es:",mostrarTotal(matrizLocal))
            return False
        
        except ValueError:
            print("Ingrese números enteros.")
            continue

########################################################################

def mostrarReporte(matrizLocal):
    """
    Funcionalidad: Mostrar un reporte de las ganancias totales de los locales.
    Entrada: La matriz (matrizLocal).
    Salida: Un reporte de las ganancias totales de los locales.
    """
    print("\nReporte de ganancias totales:")
    while True:
        try:
            salida=reportarEdificio(matrizLocal)
            print("\nTotal de locales alquilados: ",salida[0]," para un porcentaje de: ",salida[1],"%")
            print("Total de locales desocupados: ",salida[2]," para un porcentaje de: ",salida[3],"%") 
            return False
        
        except ValueError:
            print("Ingrese números enteros.")
            continue

######################################################################## 


def menuIngreso(matrizLocal):
    """
    Funcionalidad: Menú de ingresos.
    Entradas: La matriz (matrizLocal).
    Salidas: Los valores que retorne cada función llamada en el menú. 
    """
    menu=True
    while menu:
        print(
            """
⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘
⌘                                                                ⌘
⌘                     Reporte ingresos                           ⌘
⌘                                                                ⌘
⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘
⌘                                                                ⌘
⌘ 1.  Por local                                                  ⌘
⌘ 2.  Por piso                                                   ⌘
⌘ 3.  Por columna                                                ⌘
⌘ 4.  Por totalidad del edificio                                 ⌘ 
⌘ 5.  Salir                                                      ⌘ 
⌘                                                                ⌘
⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘
        """)
        menuOpcion=input("\nღIngrese una opción del menú principal: ")
        if (menuOpcion=="1"):
                mostrarLocales(matrizLocal)
                
        elif (menuOpcion=="2"):
                mostrarPisos(matrizLocal)
                
        elif (menuOpcion=="3"):
                mostrarColumnas(matrizLocal)
        
        elif (menuOpcion=="4"):
                mostrarTotalidad(matrizLocal)

        elif(menuOpcion=="5"):
                menuPrincipal(matrizLocal)
        else:
            print("Esa opción no existe, ingrese otra.\n")
            continue
    return

########################################################################    

def menuPrincipal(matrizLocal):
    """
    Funcionalidad: Mostrar el menú principal.
    Entradas: La matriz (matrizLocal).
    Salidas: Opción escogida del menú.
    """
    menu=True
    while menu:
        print(
            """
⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘
⌘                                                                ⌘
⌘                     Menú principal                             ⌘
⌘                                                                ⌘
⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘
⌘                                                                ⌘
⌘ 1.  Alquilar piso                                              ⌘
⌘ 2.  Modificar renta                                            ⌘
⌘ 3.  Desalojar                                                  ⌘
⌘ 4.  Indicar ingreso por alquiler.                              ⌘
⌘ 5.  Reporte total del edificio                                 ⌘
⌘ 6.  Salir del programa                                         ⌘
⌘                                                                ⌘
⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘
        """)

        menuOpcion=input("\nღIngrese una opción del menú principal: ")
        if (menuOpcion=="1"):
                ingresaralquilerLocal(matrizLocal)
                
        elif (menuOpcion=="2"):
                ingresarMonto(matrizLocal)
                
        elif (menuOpcion=="3"):
                ingresarDesalojo(matrizLocal)
        
        elif (menuOpcion=="4"):
                menuIngreso(matrizLocal)
                
        elif (menuOpcion=="5"):
                mostrarReporte(matrizLocal)
                
        elif (menuOpcion=="6"):
                graba(nomArchivo,matrizLocal)
                print("...")
                time.sleep(3)
                print("""
ღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღ
ღ                                                                             ღ
ღ                                ¡Adiós!                                      ღ
ღ                                                                             ღ
ღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღ
                      """)
                sys.exit()       
        else:
            print("Esa opción no existe, ingrese otra.\n")
    return



########################################################################

#Programa principal:
print("\n~Bienvenido al sistema de alquiler de locales~")
ingresarDatosAlquiler()





