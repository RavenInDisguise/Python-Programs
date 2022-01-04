########################################################################
# Elaborado por: Mónica Alfaro P y Jennifer Alvarado B.
# Fecha de creación: 24/06/2020 10:00
# Fecha de última modificación: 24/06/2020 15:50
# Versión: 3.8.2
########################################################################

#Importacion de librerías:
import pickle

########################################################################

#Declaracion de variable global:

nomArchivo="deportes"

########################################################################

#Archivos:

def graba(nomArchGrabar,dicc):
    """
    Funcionalidad: Graba los valores ingresados en memoria secundaria. 
    Entrada: Nombre del archivo (nomArchGrabar) y el diccionario.
    Salida: Archivo grabado en memoria secundaria.
    """
    try:
        f=open(nomArchGrabar,"wb")
        print("\nInformación sobre el almacenamiento de los archivos:")
        print("1. El archivo será grabado en la memoria RAM: ", nomArchGrabar)
        pickle.dump(dicc,f)
        print("2. El archivo será cerrado: ", nomArchGrabar)
        f.close()
    except:
        print("Error al grabar el archivo: ", nomArchGrabar)
        

def lee (nomArchLeer):
    """
    Funcionalidad: Lee los valores almacenados en memoria secundaria.
    Entrada: El nombre del archivo: nomArchLeer.
    Salida: La matriz que estaba guardada en memoria secundaria.
    """
    dicc={}
    try:
        print("\nInformación sobre la lectura de los archivos:")
        f=open(nomArchLeer,"rb")
        print("1. El archivo está siendo leído: ", nomArchLeer)
        dicc = pickle.load(f)
        print("2. El archivo está siendo cerrado: ", nomArchLeer)
        f.close()
    except xxx:
        print("Error al leer el archivo: ", nomArchLeer)
    return dicc

########################################################################
