########################################################################
# Elaborado por: Mónica Alfaro P y Jennifer Alvarado Brenes.
# Fecha de creación: 15/05/2020 10:10am
# Fecha de última modificación: XX/XX/2020 XX:XX
# Versión: 3.8.2
########################################################################

#Importación de librerías:

from libreria_MonicaJennifer import *

import re

########################################################################

#Definición de una función:
def validarCodigo(codigo1):
    """
    Funcionalidad: Validación de datos ingresados.
    Entradas: El código str(codigo).
    Salidas: La opcion int(opcion).
    """ 
    opcion=0
    if re.match("RE",codigo1[0:2]):
            if re.match(r"(RE)(D|S)[1-6]$",codigo1):
                opcion=1
            elif re.match(r"(RE)(D|S)(7)[1-2](PQ|MD|GD)$",codigo1):
                opcion=2
            else:
                opcion=5
    elif re.match(r"(QE)(GR|PQ)(FR|VN|CM|CE)$", codigo1):
            opcion=3
    elif re.match(r"TCAGR$",codigo1):
            opcion=4
    else:
        opcion=5
        
    return opcion

def ingresarCodigo():
    """
    Funcionalidad: E/S de datos.
    Entradas: El código str(codigo).
    Salidas: La información sobre la repostería selecta en el código.
    """   
    while True:
        try:
            #Llama a mostrarOpciones() aquí
            print("\nBienvenido al sistema de Spoon:\n")
            codigo=input("Indique el código de la merienda: ")
            codigo=codigo.upper()
            #Aquí iría el menú :)
            if((validarCodigo(codigo))<5):
                if ((validarCodigo(codigo))<3):
                    print("\nLa orden:\n"+
                          "Usted solicita una repostería de sabor "+obtenerOpcionRepos(codigo)+
                          ", correspondiente a "+obtenerRepos(codigo)+".")
                    if((validarCodigo(codigo))==2):
                        print("El sabor es de "+saborRepos(codigo)+", de tamaño "+obtenerTamanno(codigo)+".\n")
                    #return False
        
                elif ((validarCodigo(codigo))==3):
                    print("\nLa orden:\n"+
                          "Usted solicita un queque de sabor de "+obtenerSaborQueque(codigo)+
                          ", de tamaño: "+obtenerTallaQueque(codigo)+".\n")
                    #return False
                
                elif ((validarCodigo(codigo))==4):
                    print("\nLa orden:\n"+
                          "Usted solicita una torta chilena, de tamaño: grande.\n")
                    #return False
            else:
                print("Ingrese un código que sea válido de acuerdo a lo propuesto en el menú.")
                
            
        except KeyboardInterrupt:
                print("El valor que ingresó es inválido.")
                continue
def mostrarOpciones():
    """
    Funcionalidad: Mostrar opciones de los productos.
    Entradas: 
    Salidas: La información sobre las opciones de los productos de la repostería.
    """
     
    """
    Aquí mostraría en bonito las opciones que tiene el usuario para realizar el código, tiene que ponerlo nice xd:
    Repostería:
    Opciones de repostería:
    S = Salado
    D = Dulce
    Tipos de repostería:
        1. Nidito
        2. Palito de queso
        3. Orejita
        4. Biscuit
        5. Crocante
        6. Enchilada
        7. Empanada
            Sabor de la repostería (SÓLO EMPANADAS):
                1. Pollo
                2. Carne
            Únicos tamaños de empanadas:
                PQ = Pequeña
                MD = Mediana
                GD = Grande
    Queque:
    Opciones de queque:
    Talla del queque:
        GR = Grande, 12 porciones
        PQ = Pequeño 4 porciones
    Sabor:
        FR = Fresa-chocolate
        VN = Vainilla
        CM = Caramelo
        CE = Chocolate

    Torta chilena:
    TCAGR = Usted solicita una torta chilena, de tamaño: grande.
    """
    return
   
#Programa Principal
ingresarCodigo()

##menu=True
##while menu:
##    menuPrinc()
##    menuOpcion=input("Ingrese una opción del menú principal: ")
##    if (menuOpcion=="1"):
##            ingresarDatos1()
##            
##    elif (menuOpcion=="2"):
##            ingresarDatos2()
##            
##    elif (menuOpcion=="3"):
##            ingresarDatos3()
##    
##    elif (menuOpcion=="4"):
##            ingresarDatos4()
##            
##    elif (menuOpcion=="5"):
##            ingresarDatos5()
##            
##    elif (menuOpcion=="6"):
##            ingresarDatos6()
##        
##    elif (menuOpcion=="7"):
##            menu=False
##    else:
##        print("Esa opción no existe, ingrese otra. \n")
