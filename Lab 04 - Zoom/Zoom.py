########################################################################
# Elaborado por: Mónica Alfaro P y Jennifer Alvarado B.
# Fecha de creación: 13/06/2020 5:45
# Fecha de última modificación: 14/06/2020 10:50
# Versión: 3.8.2
########################################################################

########################################################################
#Importación de librerías:

import re
import math
import sys
import time
from Funciones import *

########################################################################

#Definición de funciones:

def ingresarParticipantes():
    """
    Funcionalidad: Ingresar la cantidad de participantes y generar la matriz.
    Entrada: Cantidad de personas de la matriz int(ppersonas).
    Salida: La matriz generada según la cantidad de personas.
    """
    while True:
        try:
            personas=int(input("\nIngrese la cantidad de personas que están en llamada: "))
            if(personas < 101 and personas > 0):
                salida=crearMatriz(personas,0,[])
                print("\nPantallas: ", math.ceil(personas/25))
                pant=personas//25
                num=personas-(pant*25)
                print("Filas: ", pant+(math.ceil(num/5)))
                print("\nParticipantes totales:\n",salida[0])
                menuPrincipal(salida[0])
                return False
            else:
                print("No se permiten más de cien participantes, ni menos de uno.")
                continue
            
        except ValueError:
            print("Ingrese un número entero.")
            continue
        
def ingresarAudioNombre(matrizTotal):
    """
    Funcionalidad: Cambiar el estado del audio. 
    Entrada: El nombre, el primer apellido str(nombre, apellido) y Matriz total.
    Salida: El estado del audio si es que el participante pertenece a la llamada.
    """
    while True:
        try:
            print("\nCambiar estado del audio:")
            nombre=input("Ingrese su nombre: ")
            apellido=input("Ingrese su primer apellido: ")
            nombre=nombre.capitalize().strip()
            apellido=apellido.capitalize().strip()
            salida=reactivarAudio(matrizTotal,nombre,apellido)
            if(salida!="Participante no encontrado."):
                print(reactivarAudio2(salida[0],matrizTotal))
            else:
                print(reactivarAudio(matrizTotal,nombre,apellido))
            return False
        
        except ValueError:
            print("Ingrese un valor válido.")
            continue

def ingresarNombreNuevo(matrizTotal):
    """
    Funcionalidad: Cambiar el nombre de un usuario. 
    Entrada: El nombre, el primer apellido, el segundo apellido str(nombre, apellido1, apellido2) y Matriz total.
    Salida: El nombre cambiado de ser posible, sino un mensaje de porqué no se pudo cambiar.
    """
    while True:
        try:
            print("\nCambiar el nombre de un usuario:")
            nombre=input("Ingrese su nombre: ")
            apellido1=input("Ingrese su primer apellido: ")
            apellido2=input("Ingrese su segundo apellido: ")
            nombre=nombre.capitalize().strip()
            apellido1=apellido1.capitalize().strip()
            apellido2=apellido2.capitalize().strip()
            nuevoUsuario=renombrar(matrizTotal,nombre,apellido1,apellido2)
            if(nuevoUsuario!=None):
                salida=encontrarPosicion(nuevoUsuario[0],nuevoUsuario[1])
                print("\nNúmero de pantalla: ",salida[0])
                print("Número de fila: ",salida[2])
                print("Número de columna: ",salida[1])
                print("Nombre: ",salida[3])
                
            return False
        
        except ValueError:
            print("Ingrese un número entero.")
            continue
        
def ingresarTotalidad(matrizTotal):
    """
    Funcionalidad: Mostrar la totalidad de participantes de la llamada.
    Entrada: Matriz total.
    Salida: Matriz total.
    """
    while True:
        try:
            print("\nMostrar totalidad de usuarios:")
            mostrarTotalidad(matrizTotal)
            return False

        except:
            print("Valor no válido.")
            continue
        
def ingresarParticipantesVideo(matrizTotal):
    """
    Funcionalidad: Mostrar los participantes que tienen el vídeo activado.
    Entrada: Matriz total.
    Salida: Matriz total.
    """
    while True:
        try:
            print("\nMostrar totalidad de usuarios con el vídeo activado:")
            ingresarVideo(matrizTotal)
            return False
        except:
            print("Valor no válido.")
            continue

def validarNombre(nombre):
    """
    Funcionalidad: Validar si el nombre tiene tres palabras.
    Entrada: Nombre str(nombre).
    Salida: Largo de nombre.split. 
    """
    nombre=nombre.split(' ')
    return len(nombre)
        
def ingresarBuscarNombre(matrizTotal):
    """
    Funcionalidad: Buscar un nombre según lo ingresado por el usuario.
    Entrada: Matriz total, nombre str(nombre).
    Salida: Número de pantalla, número de fila, número de columna, nombre str(salida[0],salida[1],salida[2],salida[3]).
    """
    while True:
        try:
            print("\nBuscar participantes para enviar mensaje:")
            print("Ingrese únicamente un nombre, apellido o letra:")
            nombre=input("Enviar a: ")
            nombre=nombre.capitalize().strip()
            contador=0
            if(validarNombre(nombre)==1):
                for i in matrizTotal:
                    if buscarParticipante(nombre,i):
                        contador=1
                        salida=encontrarPosicion(i,matrizTotal)
                        print("\nNúmero de pantalla: ",salida[0])
                        print("Número de fila: ",salida[2])
                        print("Número de columna: ",salida[1])
                        print("Nombre: ",salida[3])
                if(contador==0):
                    print("Participante no encontrado.")
                    continue
                return False
            else:
                 print("Ingrese únicamente un nombre, apellido o letra.")
                 continue
                
        
        except ValueError:
            print("Ingrese un valor válido.")
            
def menuPrincipal(matrizTotal):
    """
    Funcionalidad: Mostrar el menú principal.
    Entradas: Matriz Total.
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
⌘ 1.  Reactivar mi audio.                                        ⌘
⌘ 2.  Renombrar.                                                 ⌘
⌘ 3.  Mostrar totalidad de participantes.                        ⌘
⌘ 4.  Mostrar participantes con vídeo.                           ⌘
⌘ 5.  Buscar un participante en el chat.                         ⌘
⌘ 6.  Salir de zoom.                                             ⌘
⌘                                                                ⌘
⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘
        """)

        menuOpcion=input("\nღIngrese una opción del menú principal: ")
        if (menuOpcion=="1"):
                ingresarAudioNombre(matrizTotal)
                
        elif (menuOpcion=="2"):
                ingresarNombreNuevo(matrizTotal)
                
        elif (menuOpcion=="3"):
                ingresarTotalidad(matrizTotal)
        
        elif (menuOpcion=="4"):
                ingresarParticipantesVideo(matrizTotal)
                
        elif (menuOpcion=="5"):
                ingresarBuscarNombre(matrizTotal)
                
        elif (menuOpcion=="6"):
                print("(5)")
                time.sleep(5)
                print("(4)")
                time.sleep(5)
                print("(3)")
                time.sleep(5)
                print("(2)")
                time.sleep(5)
                print("(1)")
                time.sleep(5)
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

#Programa Principal:

print("""
ღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღ
ღ                                                                             ღ
ღ                         ¡Bienvenido a Zoom!                                 ღ
ღ                                                                             ღ
ღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღ
                      """)

ingresarParticipantes()

