##########################################################################
#Elaborado por: Mónica Alfaro Parrales y Jennifer Alvarado Brenes
#Inicio: 23/07/2020 16:22 pm
#Última modificación: 23/07/2020 16:22 pm
#Versión 3.8.2
##########################################################################

#Importación de librerías:

from clasesBebida import *
from funciones import *
import re
import time
import sys
import pickle

##########################################################################

def graba(nomArchGrabar,lista):
    """
    Funcionalidad: Guardar los datos de las bebidas en memoria secundaria.
    Entradas: El nombre del archivo y la lista de datos.
    Salidas: ---
    """
    try:
        f=open(nomArchGrabar,"wb")
        print("Voy a grabar el archivo: ", nomArchGrabar)
        pickle.dump(lista,f)
        print("Voy a cerrar el archivo: ", nomArchGrabar)
        f.close()
    except:
        print("Error al grabar el archivo: ", nomArchGrabar)

def lee(nomArchLeer):
    """
    Funcionalidad: Leer los datos de las bebidas en memoria secundaria.
    Entradas: El nombre del archivo.
    Salidas: ---
    """
    lista=[]
    try:
        f=open(nomArchLeer,"rb")
        print("Voy a leer el archivo: ", nomArchLeer)
        lista = pickle.load(f)
        print("Voy a cerrar el archivo: ", nomArchLeer)
        f.close()
    except:
        print("El archivo no existe aún, será creado como: ", nomArchLeer)
    return lista
