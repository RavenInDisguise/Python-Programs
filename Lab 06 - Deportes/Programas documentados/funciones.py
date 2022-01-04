########################################################################
# Elaborado por: Mónica Alfaro P y Jennifer Alvarado B.
# Fecha de creación: 24/06/2020 10:00
# Fecha de última modificación: 24/06/2020 15:50
# Versión: 3.8.2
########################################################################

#Importación de librerías:

import re
from archivos import *

########################################################################

def ingresarCodigo(codigoDeporte,nombreDeporte,explicacionDeporte,lugarDeporte,dicc):
    """
    Funcionalidad: Verificar si el código ya está registrado.
    Entrada: El código y sus datos, y el diccionario.
    Salida: True (ya se encuentra registrado) o False (no se encuentra y se puede registrar).
    """
    if codigoDeporte in dicc:
        print("Un deporte ya fue agregado con ese código.\n")
        return False
    else:
        dicc[codigoDeporte]=[nombreDeporte,explicacionDeporte,lugarDeporte]
        print("Deporte ingresado satisfactoriamente.\n")
        return True


def eliminarDeporte(codigoDeporte,dicc):
    """
    Funcionalidad: Verificar si el código ya está registrado.
    Entrada: El código y el diccionario.
    Salida: True (encontró el código y lo elimina) o False (el código no se puede eliminar porque no está registrado).
    """
    if codigoDeporte in dicc:
        del dicc[codigoDeporte]
        print("Deporte eliminado satisfactoriamente.\n")
        return True
    else:
        print("El deporte que desea eliminar, no existe registrado en la base de datos del TEC en Sede Central.\n")
        return False

def mostrarDeporte(dicc):
    """
    Funcionalidad: Mostrar todos los códigos de deportes y su información.
    Entrada: El diccionario.
    Salida: Los datos.
    """
    listas=list(dicc.items())
    for lista in listas:
        listas2=lista[1]
        print("\nCódigo: ", lista[0])
        print("Deporte: ",listas2[0])
        print("Explicación del deporte: ",listas2[1])
        print("Lugar donde se realiza: ",listas2[2])
    return

def mostrarPorCodigos(codigoDeporte,dicc):
    """
    Funcionalidad: Mostrar información sobre un código en específico.
    Entrada: El código y el diccionario.
    Salida: La información del deporte de ese código en específico.
    """
    if codigoDeporte in dicc:
        listas=dicc[codigoDeporte]
        print("\nDeporte: ",listas[0])
        print("Explicación del deporte: ",listas[1])
        print("Lugar donde se realiza: ",listas[2])
    else:
        print("Ese código no existe en el registro de deportes del TEC.")
    return

def mostrarPorLugares(lugarDeporte,dicc):
    """
    Funcionalidad: Mostrar información sobre códigos en específico dependiendo del lugar.
    Entrada: El lugar y el diccionario.
    Salida: Información sobre los deportes practicados en ese lugar.
    """
    listas=list(dicc.values())
    contador=0
    for lista in listas:
        if lugarDeporte in lista:
            print("\nDeporte: ",lista[0])
            print("Explicación del deporte: ",lista[1])
            print("Lugar donde se realiza: ",lista[2])
            contador=1
    if contador==0:
        print("No existen deportes registrados en el lugar: "+lugarDeporte+" que usted especifica.")
    return 
    
            
        
        
        
        
    
