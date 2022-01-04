########################################################################
# Elaborado por: Mónica Alfaro P y Jennifer Alvarado B.
# Fecha de creación: 24/06/2020 10:00
# Fecha de última modificación: 24/06/2020 15:50
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
      "TEC96":["Tennis","Es un deporte que utiliza una raqueta y una bola pequeña verde","Gimnasio"]}

########################################################################

def validarCodigo(codigoDeporte):
    """
    Funcionalidad: Valida el formato del código ingresado (TEC + dos números).
    Entrada: El código.
    Salida: True (es correcto) o False (no cumple con el formato).
    """
    if(re.match(r"^(TEC)[0-9][0-9]$",codigoDeporte)):
        return True
    
def validarNombre(nombreDeporte):
    """
    Funcionalidad: Valida el largo del nombre del deporte ingresado.
    Entrada: El deporte.
    Salida: True (es correcto) o False (no cumple con el formato).
    """
    if(4<len(nombreDeporte)):
        return True

def validarExplicacion(nombreExplicacion):
    """
    Funcionalidad: Valida el largo de la explicación ingresada.
    Entrada: La explicación.
    Salida: True (es correcto) o False (no cumple con el formato).
    """
    if(4<len(nombreExplicacion)<=49):
        return True
    
def ingresarDeportes(dicc):
    """
    Funcionalidad: Valida que todos los datos que se ingresen al agregar un código cumplan con las especificaciones y graba.
    Entrada: Los datos (código, deporte, explicación y lugar).
    Salida: False (si se grabó bien).
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
    Funcionalidad: Verifica que el código se encuentre en el diccionario y luego lo elimina (graba el cambio en el archivo).
    Entrada: El diccionario y el código.
    Salida: False (cuando lo elimina).
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
    Funcionalidad: Muestra la información del deporte especificado.
    Entrada: El diccionario y el nombre del deporte. 
    Salida: Información del deporte.
    """
    print("\nMostrar todos los datos de los deportes: ")
    try:
        mostrarDeporte(dicc)
        
    except:
        print("El valor es incorrecto.")

        
########################################################################

def mostrarPorCodigo(dicc):
    """
    Funcionalidad: Muestra la información del deporte de un código especificado.
    Entrada: El diccionario y el código. 
    Salida: Información del deporte con ese código.
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
    Funcionalidad: Muestra la información de los deportes de un lugar especificado.
    Entrada: El diccionario y el nombre del lugar. 
    Salida: La información.
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

