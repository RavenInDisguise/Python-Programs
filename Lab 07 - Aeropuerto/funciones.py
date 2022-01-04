##########################################################################
#Elaborado por Mónica Alfaro Parrales y Jennifer Alvarado Brenes
#Inicio 04/07/2020 01:20 pm
#Última modificación 04/07/2020 22:50 pm
#Versión 3.8.2
##########################################################################
from clasesEquipaje import *

def menuEliminar(lista,maleta):
    """
    Funcionalidad: Menú para saber si desea desalojar o no.
    Entradas: Número de piso (pisoIn), número de local (localIn),la matriz(locales) y el valor.
    Salidas: El local escogido desalojado.
    """
    flag=True
    while flag:
        valor=input("¿Está seguro de eliminar esta maleta? Ingrese Si/No ")
        valor=valor.lower()
        if(valor=="sí" or valor=="si"):
            lista=lista.remove(maleta)
            mensaje="\nMaleta eliminada exitosamente."
            return mensaje
        elif(valor=="no"):
            mensaje="La maleta no fue eliminada."
            return mensaje
        else:
            print("Ingrese Si/No")
            continue
    flag=False
    return flag

def buscarCodigo(lista,codigo):
    """
    Funcionalidad: Busca el código en la lista de equipajes.
    Entradas: Lista y código a buscar.
    Salidas: False (sí se encuentra) o False (no se encuentra).
    """
    for maleta in lista:
        if maleta.obtenerCodigo()==codigo:
            return False
    return True

def eliminarMaletas(lista,codigo):
    """
    Funcionalidad: Busca el código en la lista de equipajes y elimina ese equipaje de la lista.
    Entradas: Lista y código a buscar.
    Salidas: Lista con ese equipaje borrado.
    """
    for maleta in lista:
        if maleta.obtenerCodigo()==codigo:
            print(menuEliminar(lista,maleta))
    return 
            

def consultarTotal(lista):
    """
    Funcionalidad: Mostrar la información de todos los equipajes.
    Entradas: Lista de equipajes.
    Salidas: La información.
    """
    for maleta in lista:
        tamano=maleta.obtenerTamano()
        fragilidad=maleta.obtenerFragilidad()
        if tamano==True:
            tamano="De mano"
        else:
            tamano="Grande"
        if fragilidad==True:
            fragilidad="Frágil"
        else:
            fragilidad="No frágil"
        print("\nCódigo: "+str(maleta.obtenerCodigo()))
        print("Peso: "+str(maleta.obtenerPeso())+" kg")
        print("Tamaño: ",tamano)
        print("Fragilidad: ",fragilidad)
        print("Descripción: "+str(maleta.obtenerDescripcion()))
        print("Estado: "+str(maleta.obtenerEstado()))
    return ""

def consultarCedula(lista,cedulaIngresada):
    """
    Funcionalidad: Mostrar la información de un equipaje especificado.
    Entradas: Lista y número de cédula.
    Salidas: La información del equipaje de esa persona.
    """
    contador=0
    for maleta in lista:
        codigo=maleta.obtenerCodigo()
        cedula=codigo[5:]
        if cedula==cedulaIngresada:
            contador=1
            tamano=maleta.obtenerTamano()
            fragilidad=maleta.obtenerFragilidad()
            if tamano==True:
                tamano="De mano"
            else:
                tamano="Grande"
            if fragilidad==True:
                fragilidad="Frágil"
            else:
                fragilidad="No frágil"
            print("\nCódigo: "+str(maleta.obtenerCodigo()))
            print("Peso: "+str(maleta.obtenerPeso())+" kg")
            print("Tamaño: ",tamano)
            print("Fragilidad: ",fragilidad)
            print("Descripción: "+str(maleta.obtenerDescripcion()))
            print("Estado: "+str(maleta.obtenerEstado()))
    if(contador==0):    
        mensaje="La maleta de esta persona no ha sido registrada aún."
        return mensaje
    return ""

def modificarPesos(lista,pesoMaleta,codigo):
    """
    Funcionalidad: Modifica el peso del equipaje especificado.
    Entradas: La lista, el peso y el código.
    Salidas: Lista con el peso modificado.
    """
    for maleta in lista:
        if maleta.obtenerCodigo()==codigo:
            maleta.asignarPeso(pesoMaleta)
            print("Peso modificado satisfactoriamente.")
    return

def modificarTamanos(lista,tamanoMaleta,codigo):
    """
    Funcionalidad: Modifica el tamaño del equipaje especificado.
    Entradas: La lista, el tamaño y el código.
    Salidas: Lista con el tamaño modificado.
    """
    for maleta in lista:
        if maleta.obtenerCodigo()==codigo:
            maleta.asignarTamano(tamanoMaleta)
            print("Tamaño modificado satisfactoriamente.")
    return

def modificarFragilidad(lista,fragilMaleta,codigo):
    """
    Funcionalidad: Modifica la fragilidad del equipaje especificado.
    Entradas: La lista, la fragilidad y el código.
    Salidas: Lista con la fragilidad modificada.
    """
    for maleta in lista:
        if maleta.obtenerCodigo()==codigo:
            maleta.asignarFragilidad(fragilMaleta)
            print("Fragilidad modificada satisfactoriamente.")
    return

def modificarEstados(lista,estadoMaleta,codigo):
    """
    Funcionalidad: Modifica el estado del equipaje especificado.
    Entradas: La lista, el estado y el código.
    Salidas: Lista con el estado modificado.
    """
    for maleta in lista:
        if maleta.obtenerCodigo()==codigo:
            maleta.asignarEstado(estadoMaleta)
            print("Estado modificado satisfactoriamente.")
    return

def modificarDescrip(lista,descripMaleta,codigo):
    """
    Funcionalidad: Modifica la descripción del equipaje especificado.
    Entradas: La lista, la descripción y el código.
    Salidas: Lista con la descripción modificada.
    """
    for maleta in lista:
        if maleta.obtenerCodigo()==codigo:
            maleta.asignarDescripcion(descripMaleta)
            print("Descripción modificada satisfactoriamente.")
    return 
    
    



    
        
