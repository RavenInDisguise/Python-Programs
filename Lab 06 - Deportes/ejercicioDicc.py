########################################################################
# Elaborado por: Mónica Alfaro P y Jennifer Alvarado B.
# Fecha de creación: 24/06/2020 10:00
# Fecha de última modificación: XX/XX/2020 XX:XX
# Versión: 3.8.2
########################################################################

#Importación de librerías:

from funciones import *
from archivos import *
import re
import time
import pickle
import sys

########################################################################

#Variable global:

dicc={"TEC56":["Fútbol","Es un deporte que utiliza un esférico y se juega con 11 jugadores","Cancha de fútbol"],
      "TEC44":["Basketball","Es un deporte que utiliza una bola color naranja y se trata de encestarla","Cancha de basketball"],
      "TEC96":["Tennis","Es un deporte que utiliza una raqueta y una bola pequeña blanca","Gimnasio"]}

########################################################################

def validarCodigo(codigoDeporte):
    """
    Funcionalidad: 
    Entrada: 
    Salida:
    """
    if(re.match(r"^(TEC)[0-9][0-9]$",codigoDeporte)):
        return True
    
def validarCodigoIgual(codigoDeporte):
    """
    Funcionalidad: 
    Entrada: 
    Salida:
    """
    
def validarNombre(nombreDeporte):
    """
    Funcionalidad: 
    Entrada: 
    Salida:
    """
    if(4<len(nombreDeporte)):
        return True

def validarExplicacion(nombreExplicacion):
    """
    Funcionalidad: 
    Entrada: 
    Salida:
    """
    if(4<len(nombreExplicacion)<=49):
        return True
    
def ingresarDeportes(dicc):
    """
    Funcionalidad: 
    Entrada: 
    Salida:
    """
    try:
        print("\nIngreso de datos del deporte: ")
        while True:
            codigoDeporte=input("Ingrese un código de deporte con el formato TEC##: ")
            codigoDeporte=codigoDeporte.strip()
            if(validarCodigo(codigoDeporte)):
                while True:
                    nombreDeporte=input("Ingrese un nombre del deporte: ")
                    if(validarNombre(nombreDeporte)):
                        while True:
                            explicacionDeporte=input("Ingrese la explicación de su deporte: ")
                            if(validarExplicacion(explicacionDeporte)):
                                while True:
                                    lugarDeporte=input("Ingrese el lugar donde se desarrolla: ")
                                    lugarDeporte=lugarDeporte.capitalize().strip()
                                    if(validarExplicacion(lugarDeporte)):
                                        if(ingresarCodigo(codigoDeporte,nombreDeporte,explicacionDeporte,lugarDeporte,dicc)):
                                            graba(nomArchivo,dicc)
                                        return False
                                    else:
                                        print("Lugar ingresado menor que 5 caracteres o mayor que 50.\n")
                                        continue
                            else:
                                print("Explicación ingresada menor que 5 caracteres o mayor que 50.\n")
                                continue
                    else:
                        print("Nombre ingresado menor que 5 caracteres.\n")
                        continue 
            else:
                print("Ingrese un código válido según el formato.\n")
                continue
    
    except ValueError:
        print("El valor ingresado es incorrecto.")

########################################################################

def eliminarDeportes(dicc):
    """
    Funcionalidad: 
    Entrada: 
    Salida:
    """
    print("\nEliminación de datos de deportes: ")
    try:
        while True:
            codigoDeporte=input("Ingrese un código de deporte con el formato TEC##: ")
            if(validarCodigo(codigoDeporte)):
                if(eliminarDeporte(codigoDeporte,dicc)):
                    graba(nomArchivo,dicc)
                    return False    
            else:
                print("Ingrese un código válido según el formato.\n")
                continue
    except:
        print("El valor ingresado es incorrecto.")
        
########################################################################

def mostrarDeportes(dicc):
    """
    Funcionalidad: 
    Entrada: 
    Salida:
    """
    print("\nMostrar todos los datos de los deportes: ")
    try:
        mostrarDeporte(dicc)
        
    except:
        print("El valor es incorrecto.")

        
########################################################################

def mostrarPorCodigo(dicc):
    """
    Funcionalidad: 
    Entrada: 
    Salida:
    """
    print("\nMostrar datos de un deporte por código: ")
    try:
        while True:
            codigoDeporte=input("Ingrese un código de deporte con el formato TEC##: ")
            if(validarCodigo(codigoDeporte)):
                mostrarPorCodigos(codigoDeporte,dicc)
                return False
            else:
                print("Ingrese un código válido según el formato.\n")
                continue
            
    except ValueError:
        print("El valor ingresado es incorrecto.")

########################################################################

def mostrarPorLugar(dicc):
    """
    Funcionalidad: 
    Entrada: 
    Salida:
    """
    print("\nMostrar datos de los deportes por lugar: ")
    try:
        while True:
            lugarDeporte=input("Ingrese el lugar donde se desarrollan los deportes: ")
            lugarDeporte=lugarDeporte.capitalize().strip()
            if(validarExplicacion(lugarDeporte)):
                mostrarPorLugares(lugarDeporte,dicc)
                return False
            else:
                print("Lugar ingresado menor que 5 caracteres o mayor que 50.\n")
                continue
            
    except ValueError:
        print("El valor ingresado es incorrecto.")

########################################################################    

def menuBuscarDeportes(dicc):
    """
    Funcionalidad: Menú de ingresos.
    Entradas: .
    Salidas: Los valores que retorne cada función llamada en el menú. 
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
⌘ 1.  Información completa de todos los deportes                 ⌘
⌘ 2.  Información por código deportes                            ⌘
⌘ 3.  Información por lugar                                      ⌘
⌘ 4.  Salir del programa                                         ⌘
⌘                                                                ⌘
⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘
        """)
        menuOpcion=input("\nღIngrese una opción del menú principal: ")
        if (menuOpcion=="1"):
                mostrarDeportes(dicc)
                
        elif (menuOpcion=="2"):
                mostrarPorCodigo(dicc)
                
        elif (menuOpcion=="3"):
                mostrarPorLugar(dicc)
        
        elif (menuOpcion=="4"):
                menuPrincipal(dicc)
                
        else:
            print("Esa opción no existe, ingrese otra.\n")
            continue
    return
  
def menuPrincipal(dicc):
    """
    Funcionalidad: Mostrar el menú principal.
    Entradas: .
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
⌘ 1.  Registrar un deporte                                       ⌘
⌘ 2.  Eliminar un deporte                                        ⌘
⌘ 3.  Buscar                                                     ⌘
⌘ 4.  Salir del programa                                         ⌘
⌘                                                                ⌘
⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘
        """)

        menuOpcion=input("\nღIngrese una opción del menú principal: ")
        if (menuOpcion=="1"):
               ingresarDeportes(dicc)
                
        elif (menuOpcion=="2"):
                eliminarDeportes(dicc)
                
        elif (menuOpcion=="3"):
                 menuBuscarDeportes(dicc)
                
        elif (menuOpcion=="4"):
                graba(nomArchivo,dicc)
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
print("\n~Bienvenido al sistema de deportes~")
graba(nomArchivo,dicc)
dicc=lee(nomArchivo)
print("\nSu lista de deportes almacenada en archivos: \n",dicc)
menuPrincipal(dicc)

