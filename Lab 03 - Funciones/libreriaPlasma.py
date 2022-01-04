########################################################################
# Elaborado por: Mónica Alfaro P.
# Fecha de creación: 03/06/2020 14:20
# Fecha de última modificación: 03/06/2020 23:10
# Versión: 3.8.2
########################################################################

#Importación de librerías:

import re

########################################################################

#Definición de las funciones:

########################################################################

#Función menú principal:

def seguirOno(seguir):
    """
    Funcionalidad: Saber si el usuario quiere continuar
    Entradas: Si/No.
    Salidas: True/False.
    """
    if seguir=="si"or seguir=="Si"or seguir=="SI":
        return seguir.upper()
    elif seguir=="no"or seguir=="No"or seguir=="NO":
        return seguir.lower()
    else:
        return ''

########################################################################


#Funciones proceso #1:

def validarCedula(cedula):
    """
    Funcionalidad: Revisa que la cédula tenga 9 números y no empiece en 0.
    Entrada: La cédula int(cedula).
    Salida: True/False. 
    """
    cedula=str(cedula)
    if re.match(r"[1-9]{1}[0-9]{8}$",cedula):
            return True
    else:
            return False
            
def buscarCedulas(cedula,recuperadosDonantes):
    """
    Funcionalidad: Buscar si las cédulas son iguales.
    Entrada: La cédula y la lista original de recuperados: int(cedula), list[recuperadosDonantes]
    Salida: True/False.
    """
    cedula=str(cedula)
    for i in  recuperadosDonantes:
        if i == cedula:
            return False
        else:
            continue
    return True

def listarCedulas(cedula,recuperadosDonantes):
    """
    Funcionalidad: Agrega las cédulas que no se encuentren en la lista.
    Entrada: La cédulas y la lista de cédulas.
    Salida: Lista con la cédula agregada o False, si no se agrega por no cumplir con las validaciones.
    """
    if validarCedula(cedula):
        if buscarCedulas(cedula,recuperadosDonantes):
            return recuperadosDonantes.append(cedula),True
        else:
            print("La cédula ya se encuentra registrada.\n")
            return "",False
    else:
        print("Debe ingresar una cédula con números enteros, sin espacios ni guiones.\n")
        return "",False


########################################################################
    
#Funciones proceso #2:
 
def generarProvincia(pindice):
    """
    Funcionalidad: Retorna la provincia a la que pertenece la cédula.
    Entrada: El índice (primer número de una cédula).
    Salida: El nombre de la provincia.
    """
    provinciaL=""
    indice=0
    indice=(int(pindice)-1)
    provinciaL=provincia[indice]
    return provinciaL
    
def generarTomo(pcedula):
    """
    Funcionalidad: Retorna el número de tomo de una cédula.
    Entrada: Cédula.
    Salida: Número de tomo.
    """
    pcedula=str(pcedula)
    icedula=pcedula[1:5]
    return icedula
        
def generarAsiento(pcedula):
    """
    Funcionalidad: Retorna el número de asiento de una cédula.
    Entrada: Cédula.
    Salida: Número de asiento.
    """
    pcedula=str(pcedula)
    icedula=pcedula[5:]
    return icedula

########################################################################

#Funciones proceso #3:

def listarDonadores(pnumero,recuperadosDonantes):
    """
    Funcionalidad: Muestra los datos para la provincia solicitada.
    Entrada: Número de cédula de provincia y lista de cédulas.
    Salida: Cantidad de cédulas y lista de cédulas.
    """
    nuevaLista=[]
    icedula=""
    listaCedulas="No hay cédulas."
    for i in recuperadosDonantes:
        cedula=i
        icedula=str(cedula[0])
        if icedula == str(pnumero):
            nuevaLista.append(i)
            listaCedulas="\n".join(nuevaLista)
    contador=len(nuevaLista)
    return contador, listaCedulas

########################################################################

#Funciones proceso #4:

def imprimirTotal(provinciaL,j,nuevaLista):
    """
    Funcionalidad: Imprime los datos (provincia,cantidad de cédulas y lista de cédulas) para la provincia solicitada.
    Entrada: La provincia, cantidad de cédulas y lista de cédulas.
    Salida: Datos impresos.
    """
    j=int(j)
    listaCedulas="\n".join(nuevaLista)
    if(len(nuevaLista)==0):
        listaCedulas="Aún no reporta donadores."
    if(j==7):
        print("\nLos donadores "+str(provinciaL)+" son "+str(len(nuevaLista))+", las cédulas son: \n"
              +str(listaCedulas))
    elif(j==8):
        print("\nLos donadores "+str(provinciaL)+" son "+str(len(nuevaLista))+", las cédulas son: \n"
              +str(listaCedulas))
    else:
        print("\nLos donadores de la provincia de "+str(provinciaL)+" son "+str(len(nuevaLista))+", las cédulas son: \n"
              +str(listaCedulas))
    return 
        
def contarProvincias(pcedula,provincia):
    """
    Funcionalidad: Saca las cédulas, la cantidad de cédulas y la provincia de la ocasión solicitada.
    Entrada: La lista de cédulas y la lista de provincias.
    Salida: Provincia, cantidad de cédulas y lista de cédulas.
    """
    for j,k in enumerate(provincia):
        nuevaLista=[]
        for i in pcedula:
            cedula=i
            indiceProvincia=int(j)
            indiceProvincia2=indiceProvincia+1
            if(str(cedula[0])==str(indiceProvincia2)):
                nuevaLista.append(cedula)
                nuevaLista.sort
            provinciaL=k
        imprimirTotal(provinciaL,j,nuevaLista)
    return

########################################################################

#Funciones proceso #5:

#Reutilización de la función listarDonadores(x,y):

########################################################################

#Lista de provincias:
    
provincia=["San José", "Alajuela", "Cartago",
           "Heredia", "Guanacaste", "Puntarenas", "Limón",
           "Nacionalizados/Extranjeros", "Casos especiales"]

########################################################################



