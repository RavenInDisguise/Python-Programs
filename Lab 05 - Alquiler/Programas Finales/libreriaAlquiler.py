########################################################################
# Elaborado por: Mónica Alfaro P y Jennifer Alvarado B.
# Fecha de creación: 22/06/2020 12:10
# Fecha de última modificación: 23/06/2020 11:25
# Versión: 3.8.2
########################################################################

#Importación de librerías:

import random
import pickle

########################################################################

#Declaracion de variable global:

nomArchivo="edificio"

########################################################################

#Archivos:

def graba(nomArchGrabar,matriz):
    """
    Funcionalidad: Graba los valores ingresados en memoria secundaria. 
    Entrada: Nombre del archivo (nomArchGrabar) y la matriz.
    Salida: Archivo grabado en memoria secundaria.
    """
    try:
        f=open(nomArchGrabar,"wb")
        print("\nInformación sobre el almacenamiento de los archivos:")
        print("1. El archivo será grabado en la memoria RAM: ", nomArchGrabar)
        pickle.dump(matriz,f)
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
    matriz=[]
    try:
        print("\nInformación sobre la lectura de los archivos:")
        f=open(nomArchLeer,"rb")
        print("1. El archivo está siendo leído: ", nomArchLeer)
        matriz = pickle.load(f)
        print("2. El archivo está siendo cerrado: ", nomArchLeer)
        f.close()
    except:
        print("Error al leer el archivo: ", nomArchLeer)
    return matriz

########################################################################

#Funciones del alquiler:

def generarMatrizVacia(numeroColumna,numeroFila):
    """
    Funcionalidad: Genera una matriz de acuerdo a los valores de fila y columna ingresados.
    Entrada: Número de columnas int(numeroColumna) y número de filas int(numeroFila).
    Salida: Una matriz de acuerdo a los valores de fila y columna ingresados.
    """
    matriz=[]
    piso=1
    while piso<=numeroFila:
        fila=[]
        columnas=1
        while columnas<=numeroColumna:
            fila.append(0)
            columnas+=1
        matriz.append(fila)
        piso+=1
    return matriz

def verificarLocal(locales,pisoIn,localIn):
    """
    Funcionalidad: Verifica que el piso y el local indicados sean válidos.
    Entradas: Los números de piso y local.
    Salidas: True (sí existen) o False (no existen).
    """
    mensaje=""
    if 1<=pisoIn<=len(locales):
        if 1<=localIn<=len(locales[pisoIn-1]):
            return True
        else:
            print("El local no existe en el piso.")
            return False
    else:
        print("El piso no existe en el edificio.")
        return False

def alquilerLocal(locales,pisoIn,localIn):
    """
    Funcionalidad: Alquila un local desocupado con un monto de ingreso random.
    Entradas: Matriz de locales, piso y número de local.
    Salidas: Matriz de locales con el local seleccionado modificado.
    """
    mensaje=""
    if verificarLocal(locales,pisoIn,localIn):
        if(locales[pisoIn-1][localIn-1]==0):
            monto=random.randint(150000,600000)
            locales[pisoIn-1][localIn-1]=monto
            mensaje="\nLocal exitosamente alquilado."
            graba(nomArchivo,locales)
        else:
            mensaje="Lo sentimos, el local ya está siendo alquilado."
    return mensaje

def pedirMonto():
    """
    Funcionalidad: Pide el monto nuevo.
    Entradas: El monto deseado.
    Salidas: El número del monto.
    """
    while True:
        try:
            montoNuevo=int(input("Ingrese el monto por el que desea cambiar el alquiler: "))
            if(montoNuevo>0):
                return montoNuevo
            else:
                print("Ingrese un monto con números enteros positivos mayores que 0.\n")
                continue
        except:
            print("Monto inválido, deben ser números enteros.\n")
            continue

def modificarRenta(locales,pisoIn,localIn):
    """
    Funcionalidad: Modifica una renta de un local en específico.
    Entradas: El número de piso y local.
    Salidas: Matriz con la renta del local modificada.
    """
    mensaje=""
    if verificarLocal(locales,pisoIn,localIn):
        if locales[pisoIn-1][localIn-1]!=0:
            montoNuevo=pedirMonto()
            locales[pisoIn-1][localIn-1]=montoNuevo
            mensaje="\nRenta exitosamente modificada."
            graba(nomArchivo,locales)
        else:
            mensaje="El local no está siendo alquilado."
    return mensaje

def menuDesalojo(locales,pisoIn,localIn):
    """
    Funcionalidad: Menú para saber si desea desalojar o no.
    Entradas: Número de piso (pisoIn), número de local (localIn),la matriz(locales) y el valor.
    Salidas: El local escogido desalojado.
    """
    flag=True
    while flag:
        valor=input("¿Desea desalojar el piso? Ingrese Si/No ")
        valor=valor.lower()
        if(valor=="sí" or valor=="si"):
            locales[pisoIn-1][localIn-1]=0
            mensaje="\nLocal exitosamente desalojado."
            graba(nomArchivo,locales)
            return mensaje
        elif(valor=="no"):
            mensaje="El local no fue desalojado."
            return mensaje
        else:
            print("Ingrese Si/No")
            continue
    flag=False
    return flag
        
    
def desalojarPiso(locales,pisoIn,localIn):
    """
    Funcionalidad: Desalojar un local.
    Entrada: Número de piso (pisoIn), número de local (localIn) y la matriz(locales).
    Salida: El local escogido desalojado.
    """
    mensaje=""
    if verificarLocal(locales,pisoIn,localIn):
        if(locales[pisoIn-1][localIn-1]!=0):
            mensaje=menuDesalojo(locales,pisoIn,localIn)
            return mensaje
        else:
            mensaje="No puede desalojar este local, ya que no está siendo alquilado."
            return mensaje
    else:
        return ""

def mostrarLocal(locales,pisoIn,localIn):
    """
    Funcionalidad: Mostrar la información de todos los locales de un local en específico y calcular el total de ingresos.
    Entradas: Los números de piso y local.
    Salidas: Información de piso, # de local e ingreso del local.
    """ 
    if verificarLocal(locales,pisoIn,localIn):
        return locales[pisoIn-1][localIn-1]
    else:
        return "ninguna. Valores del local ingresados no válidos."
                
def verificarPiso(locales,pisoIn):
    """
    Funcionalidad: Verifica que el piso indicado sea válido.
    Entradas: Los números de piso.
    Salidas: True (sí existen) o False (no existen).
    """
    if 1<=pisoIn<=len(locales):
        return True
    else:
        print("El piso no existe en el edificio.")
        return False

def mostrarPiso(locales,pisoIn):
    """
    Funcionalidad: Mostrar la información de todos los locales de un piso en específico y calcular el total de ingresos.
    Entradas: Los números de piso y local.
    Salidas: Información de piso, #de local y total de ingresos del piso.
    """
    if verificarPiso(locales,pisoIn):
        total=0
        posicion=1
        for local in locales[pisoIn-1]:
            print("\nPiso #",pisoIn)
            print("Local #",posicion)
            print("Monto de alquiler $: ",local)
            total+=local
            posicion+=1
        return total
    else:
        return "ninguno. Cantidad de pisos ingresados no válidos."

def verificarColumna(locales,columna):
    """
    Funcionalidad:
    Entradas: 
    Salidas: 
    """
    if 1<=columna<=len(locales):
        return True
    else:
        print("La columna no existe en el edificio.")
        return False

def mostrarColumna(matrizLocal,columna):
    """
    Funcionalidad: Mostrar las ganancias de los locales por columna.
    Entradas: La matriz (matrizLocal) y la int(columna).
    Salidas: Las ganancias de los locales por columna.
    """
    monto=0
    total=0
    if(verificarColumna(matrizLocal,columna)):
        for indice1,matriz in enumerate(matrizLocal):
            indice=indice1
            print("\nPiso #",indice+1)
            print("Local #",columna)    
            print("Monto de alquiler $: ", matriz[columna-1])
            monto=matriz[columna-1]
            total+=monto
        return total
    return "ninguno. Cantidad de columnas ingresadas no válidas."

def mostrarTotal(locales):
    """
    Funcionalidad: Mostrar información de todos los locales y calcular el total de ingresos del edificio.
    Entradas: Matriz con locales.
    Salidas: Información de cada local y el total de ingresos.
    """
    numPiso=1
    total=0
    for local in locales:
         numLocal=1
         for lugar in local:
            print("\nPiso #",numPiso)
            print("Local #",numLocal)
            print("Monto de alquiler $: ",lugar)
            total+=lugar
            numLocal+=1
         numPiso+=1
    return total

def reportarEdificio(locales):
    """
    Funcionalidad: Sacar las cantidades de alquilados y desocupados, y sus respectivos porcentajes.
    Entradas: La matriz con los locales y sus montos.
    Salidas: Cantidad de alquilados, desocupados y porcentajes de ambos.
    """
    ocupados=0
    desocupados=0
    total=0
    for local in locales:
         for lugar in local:
             if lugar!=0:
                 ocupados+=1
             else:
                 desocupados+=1
             total+=1
    porcenOcupados=int((ocupados*100)/total)
    porcenDesocupados=int((desocupados*100)/total)
    return ocupados,porcenOcupados,desocupados,porcenDesocupados
    
                
            
