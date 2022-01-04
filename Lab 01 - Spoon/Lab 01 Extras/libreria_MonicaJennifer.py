########################################################################
# Elaborado por: Mónica Alfaro P y Jennifer Alvarado B.
# Fecha de creación: 15/05/2020 10:10am
# Fecha de última modificación: XX/XX/2020 XX:XX
# Versión: 3.8.2
########################################################################

#Función 1:

def obtenerOpcionRepos(pcodigo):
    """
    Funcionalidad: Averiguar las opciones de la repostería.
    Entradas: El código str(codigo).
    Salidas: La opción de la repostería str(opcionRepos).
    """
    if((pcodigo[2])=="D"):
        opcionRepos="dulce" 
    else:
        opcionRepos="salado"
    
    return opcionRepos

def obtenerRepos(pcodigo):
    """
    Funcionalidad: Averiguar el tipo de repostería.
    Entradas: El código str(codigo).
    Salidas: El tipo de repostería (reposteria[x])
    """
    reposteria=["un: nidito","un: palito de queso","una: orejita","un: biscuit","un: crocante", "una: enchilada","una: empanada"]
    codigo=int(pcodigo[3])
    return reposteria[codigo-1]

def saborRepos(pcodigo):
    """
    Funcionalidad: Averiguar el sabor de la repostería.
    Entradas: El código str(codigo).
    Salidas: El sabor de la repostería (opcionSabor).
    """
    if(pcodigo[4]=="1"):
        opcionSabor="pollo"
    else:
        opcionSabor="carne"
    return opcionSabor

def obtenerTamanno(pcodigo):
    """
    Funcionalidad: Averiguar el tamaño de la repostería.
    Entradas: El código str(codigo).
    Salidas: El tamaño de la repostería (opcionTamanno).
    """
    if((pcodigo[5:7])=="PQ"):
        opcionTamanno="pequeña"
    elif((pcodigo[5:7])=="MD"):
        opcionTamanno="mediana"
    else:
        opcionTamanno="grande"
    return opcionTamanno

def obtenerSaborQueque(pcodigo):
    """
    Funcionalidad: Averiguar el sabor del queque.
    Entradas: El código str(codigo).
    Salidas: El sabor del queque (opcionSaborQ).
    """
    if((pcodigo[4:6])=="FR"):
        opcionSaborQ="fresa-chocolate"
    elif((pcodigo[4:6])=="VN"):
         opcionSaborQ="vainilla"
    elif((pcodigo[4:6])=="CM"):
         opcionSaborQ="caramelo"
    else:
        opcionSaborQ="chocolate"
    return opcionSaborQ

def obtenerTallaQueque(pcodigo):
    """
    Funcionalidad: Averiguar el tamaño del queque.
    Entradas: El código str(codigo).
    Salidas: El tamaño del queque (opcionTalla).
    """
    if((pcodigo[2:4])=="GR"):
       opcionTalla="grande"
    else:
        opcionTalla="pequeño"
    return opcionTalla

        
        
        
    
    
        
        
