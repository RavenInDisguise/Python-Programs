########################################################################
# Elaborado por: Mónica Alfaro P y Jennifer Alvarado B.
# Fecha de creación: 13/06/2020 5:45
# Fecha de última modificación: 14/06/2020 00:44
# Versión: 3.8.2
########################################################################

import names
import random

def nombreRandom():
    """
    Funcionalidad: Generar nombre y apellidos.
    Entrada: Ninguna.
    Salida: Nombres y apellidos str(nombre). 
    """
    nombre1=[names.get_first_name()]
    nombre2=[names.get_last_name()]
    nombre3=[names.get_last_name()]
    nombre=[]
    nombre=nombre1+nombre2+nombre3
    return nombre

def audio():
    """
    Funcionalidad: Generar estado del audio aleatoria.
    Entrada: Ninguna.
    Salida: El estado del audio
    """
    audio=random.choice(["True", "False"])
    return audio

def presencia():
    """
    Funcionalidad: Generar presencia aleatoria.
    Entrada: Ninguna.
    Salida: Presencia int(1,2,3). 
    """
    presencia=random.choice([1,2,3])
    return presencia

def reaccion():
    """
    Funcionalidad: Generar reacción aleatoria. 
    Entrada: Ninguna.
    Salida: La reacción.
    """
    reaccion=random.choice(["sn", "ap","lv"])
    return reaccion

def crearMatrizPersona():
    """
    Funcionalidad: Crear una lista con los datos aleatorios por persona.
    Entrada: Ninguna.
    Salida: Lista con datos aleatorios por persona (matriz).
    """
    matriz=[]
    matriz.append([nombreRandom(),audio(),presencia(),reaccion()])
    return matriz

def crearMatrizFila(ppersonas):
    """
    Funcionalidad: Crear una lista con filas de los datos aleatorios por persona.
    Entrada: Cantidad de personas int(ppersonas).
    Salida: Lista con filas de los datos aleatorios por persona (matriz1).
    """
    filas=5
    matriz1=[]   
    i=1
    if(ppersonas<5):
       filas=ppersonas 
    while i <= filas:
            matriz1+=crearMatrizPersona()
            i+=1
    return matriz1


def crearMatriz(ppersonas,count,matrizActual):
    """
    Funcionalidad: Crear la matriz completa con los usuarios y las filas.
    Entrada: Cantidad de personas, contador int(count), matriz actual (cada 25 usuarios).
    Salida: Matriz completa y contador (matrizActual+matriz, count). 
    """
    if(count>=4):
        return matrizActual
    else:
        filas=ppersonas/5
        matriz=[]
        i=1
        if(filas%1!=0):
            filas+=1
        while i <= filas and ppersonas > 0 :
            salida=crearMatrizFila(ppersonas)
            print("\nColumna: ",i,salida)
            matriz+=salida
            i+=1
            ppersonas-=5
            if(len(matriz)==25):
                return crearMatriz(ppersonas,count+1,matrizActual+matriz)
        return matrizActual+matriz, count

def reactivarAudio(matrizTotal,nombre,apellido1):
    """
    Funcionalidad: Encontrar usuario por nombre.
    Entrada: La matriz total, el nombre y el apellido.
    Salida: Datos del usuario específico (i) y la matriz total (matrizTotal), o mensaje en caso de no encontrar participante.
    """
    contador=0
    for i in matrizTotal:
        nombrePer=i[0]
        if nombrePer[0]==nombre and nombrePer[1]==apellido1:
            contador=1
            return i,matrizTotal
    if(contador==0):
        mensaje="Participante no encontrado."
        return mensaje
            
def reactivarAudio2(salida,matrizTotal):
    """
    Funcionalidad: Cambiar estado del audio.
    Entrada: Los datos del usuario y la matriz completa (salida, matrizTotal).
    Salida: Mensaje, la pantalla, columna y fila en que se encuentra del usuario (datos[0],datos[1],datos[2]).
    """
    if salida[1] == "True":
        mensaje="No se puede activar el audio porque ya está activo."
    else:
        valor=str("True")
        salida[1]="True"
        datos=encontrarPosicion(salida,matrizTotal)
        print("Pantalla: ",datos[0])
        print("Columna: ",datos[1])
        print("Fila: ",datos[2])
        mensaje="Su audio está siendo activado."
    return mensaje

def validarNombre(nombre):
    """
    Funcionalidad: Validar si el nombre tiene tres palabras.
    Entrada: Nombre str(nombre).
    Salida: Largo de nombre.split. 
    """
    nombre=nombre.split(' ')
    return len(nombre)

def renombrar(matrizTotal,nombre,apellido1,apellido2):
    """
    Funcionalidad: Si el nombre ingresado está en la lista de usuarios, permite cambiarlo por otro.
    Entrada: La matriz general, el nombre a buscar y el nombre para reemplazar.
    Salida: La persona con el nuevo nombre y la matriz con esa persona registrada.
    """
    for i in matrizTotal:
        nombrePer=i[0]
        if nombrePer[0]==nombre and nombrePer[1]==apellido1 and nombrePer[2]==apellido2:
            nombreNuevo=input("Ingrese el nuevo nombre completo: ")
            if(validarNombre(nombreNuevo)==3):
                nombreNuevo=nombreNuevo.title()
                nombreNuevo=nombreNuevo.split(" ")
                nombrePer[0]=nombreNuevo[0]
                nombrePer[1]=nombreNuevo[1]
                nombrePer[2]=nombreNuevo[2]
                print("Nombre cambiado satisfactoriamente.")
                return i,matrizTotal
            else:
                print("El nombre ingresado no es válido.")
                continue
        else:
            continue
    print("Este usuario no se encuentra en la llamada.")
       
def mostrarTotalidad(matrizTotal):
    """
    Funcionalidad: Mostrar todos los usuarios de la llamada.
    Entrada: La matriz total (matrizTotal).
    Salida: La pantalla, columna y fila en que se encuentra del usuario (datos[0],datos[1],datos[2]), nombre, apellido,
    apellido 2, estado del audio y la presencia.
    """
    for i in matrizTotal:
        datos=encontrarPosicion(i,matrizTotal)
        print("\nPantalla: ",datos[0])
        print("Columna: ",datos[1])
        print("Fila: ",datos[2])
        nombre=str(i[0]).split()
        nombre1=nombre[0].strip("[]").strip("''").strip("''").strip(",").strip("''")
        apellido1=nombre[1].strip("[]").strip(",").strip("''").strip("''")
        apellido2=nombre[2].strip("[]").strip("''").strip(",").strip("''").strip("''")
        print("Nombre: ", str(nombre1)+" "+str(apellido1)+" "+str(apellido2))
        if(i[1]=="True"):
            valor="Activado."
        else:
            valor="Inactivo."
        print("Audio: ", valor)
        if(i[2]==1):
            valor2="Foto visible."
        elif(i[2]==2):
            valor2="Foto no visible."
        else:
            valor2="Video activo."
        print("Presencia de cámara: ", valor2)

def ingresarVideo(matrizTotal):
    """
    Funcionalidad: Mostrar todos los usuarios de la llamada con el vídeo activado.
    Entrada: La matriz total (matrizTotal).
    Salida: La pantalla, columna y fila en que se encuentra del usuario (datos[0],datos[1],datos[2]), nombre, apellido,
    apellido 2.
    """
    contador=0
    for lista in matrizTotal:
        video=lista[2]
        if(video==3):
            datos=encontrarPosicion(lista,matrizTotal)
            print("\nPantalla: ",datos[0])
            print("Columna: ",datos[1])
            print("Fila: ",datos[2])
            contador+=1
            nombre=str(lista[0]).split()
            nombre1=nombre[0].strip("[]").strip("''").strip("''").strip(",").strip("''")
            apellido1=nombre[1].strip("[]").strip(",").strip("''").strip("''")
            apellido2=nombre[2].strip("[]").strip("''").strip(",").strip("''").strip("''")
            print("Nombre: ", str(nombre1)+" "+str(apellido1)+" "+str(apellido2))
    if(contador==0):
        print("\nNadie tiene el vídeo activado.")
    else:
        print("\nLa cantidad de personas con vídeo activado: ",contador)
        
def encontrarColumnaFila(posicion):
    """
    Funcionalidad: Saca el número de columna y fila basado en la posición de la matriz general.
    Entrada: La posición.
    Salida: Número de columna y fila.
    """
    if 20<=posicion<=24:
        fila=posicion-19
        columna=5
    elif 15<=posicion<=19:
        fila=posicion-14
        columna=4
    elif 10<=posicion<=14:
        fila=posicion-9
        columna=3
    elif 5<=posicion<=9:
        fila=posicion-4
        columna=2
    else:
        fila=posicion+1
        columna=1
    return columna,fila

def encontrarPosicion(persona,matrizTotal):
    """
    Funcionalidad: Encuentra la pantalla, columna, fila y muestra el nombre de una persona.
    Entrada: La persona y la matriz general.
    Salida: Número de pantalla, columna, fila y nombre.
    """
    nombre=persona[0]
    nombreNuevo=nombre[0]+" "+nombre[1]+" "+nombre[2]
    posicion=matrizTotal.index(persona)
    if 0<=posicion<=24:
        posicion=posicion
        pantalla=1
    elif 25<=posicion<=49:
        posicion=posicion-25
        pantalla=2
    elif 50<=posicion<=74:
        posicion=posicion-50
        pantalla=3
    else:
        fila=posicion-75
        pantalla=4
    salida=encontrarColumnaFila(posicion)
                     #columna  #fila
    return pantalla,salida[0],salida[1],nombreNuevo

def buscarParticipante(nombre,matriz):
    """
    Funcionalidad: Busca una similitud entre una cadena y el nombre y apellidos.
    Entrada: La cadena y la persona actual de la matriz.
    Salida: True (hay similitud) o False (no la hay).
    """
    nombreP=matriz[0]
    for palabra in nombreP:
        if nombre in palabra or nombre.capitalize() in palabra:
            return True
    
            
      
