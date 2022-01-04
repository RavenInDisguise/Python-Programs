########################################################################
# Elaborado por: Mónica Alfaro P y Jennifer Alvarado Brenes.
# Fecha de creación: 15/05/2020 10:10am
# Fecha de última modificación: 17/05/2020 7:00pm
# Versión: 3.8.2
########################################################################

#Importación de librerías:

from libreria_MonicaJennifer import *

import re
import sys

########################################################################

#Definición de una función:
def continuar():
    """
    Funcionalidad: Saber si continuar o no.
    Entradas: La respuesta str(seguir).
    Salidas: Vuelve a ingresar código o acaba.
    """ 
    seguir=input("\n~¿Desea ingresar otro código? (Sí/No) ")
    respuesta=seguirOno(seguir)
    if respuesta.isupper():
        return ingresarCodigo()
    elif respuesta.islower():
        sys.exit()
    else:
        print("Ingrese Si/No ")
        continuar()
    
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
            
            print("""
          ▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃
          
                                  ☕ Μҽŋu Ѕpοοŋ  ☕
            ▧ Repostería (RE): 
            Puede ser:
            ღ Salada (S)
            ღ Dulce (D)
            Opciones de repostería:
             1. Nidito
             2. Palitos de queso
             3. Orejita
             4. Biscuit
             5. Crocante
             6. Enchilada
             7. Empanada
                 ▧ Las empanadas pueden ser de:
                 1. Pollo 
                 2. Carne 
                 ▧ Tamaño:
                 ღ Pequeña (PQ)
                 ღ Mediana (MD)
                 ღ Grande (GD) 
             
            ▧ Queques (QE):
            Tamaño:
            ღ Grande (GR) de 12 porciones
            ღ Pequeño (PQ) de 4 porciones
            Los sabores son:
            ღ Fresa con chocolate (FR)
            ღ Vainilla (VN)
            ღ Caramelo (CM)
            ღ Chocolate (CE)
            
            ▧ Torta chilena (TCAGR):
            Sólo hay de tamaño grande\n
          ▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃
            """)
            codigo=input("~Indique el código de la merienda: ")
            codigo=codigo.upper()
            if((validarCodigo(codigo))<5):
                if ((validarCodigo(codigo))<3):
                    print("\n~La orden:\n"+
                          "Usted solicita una repostería de sabor "+obtenerOpcionRepos(codigo)+
                          ", correspondiente a "+obtenerRepos(codigo)+".")
                        
                    if((validarCodigo(codigo))==2):
                        print("El sabor es de "+saborRepos(codigo)+", de tamaño "+obtenerTamanno(codigo)+".\n")

                    continuar()
        
                elif ((validarCodigo(codigo))==3):
                    print("\n~La orden:\n"+
                          "Usted solicita un queque de sabor de "+obtenerSaborQueque(codigo)+
                          ", de tamaño: "+obtenerTallaQueque(codigo)+".\n")
                    continuar()
                    
                elif ((validarCodigo(codigo))==4):
                    print("\n~La orden:\n"+
                          "Usted solicita una torta chilena, de tamaño: grande.\n")
                    continuar()
            else:
                print("Ingrese un código que sea válido de acuerdo a lo propuesto en el menú.")
             
            
        except KeyboardInterrupt:
                print("El valor que ingresó es inválido.")
                continue

opciones=True
while opciones:
    print("\n ☕ Bienvenido al sistema de Spoon ☕\n")
    print("1. Introducir un código")
    print("2. Salir del programa")
    menuOpcion=input("~¿Qué desea hacer a continuación? ")
    if (menuOpcion=="1"):
        ingresarCodigo()
    elif (menuOpcion=="2"):
        opciones=False 
    else:
        print("Opción inválida, elija otra.\n")
