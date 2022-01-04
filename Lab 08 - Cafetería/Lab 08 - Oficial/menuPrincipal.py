##########################################################################
#Elaborado por: Mónica Alfaro Parrales y Jennifer Alvarado Brenes
#Inicio: 22/07/2020 12:10 pm
#Última modificación: 23/07/2020 16:30 
#Versión 3.8.2
##########################################################################

#Importación de librerías:

from clasesBebida import *
from funciones import *
from funcionesArchivos import *
import re
import time
import sys
import pickle

##########################################################################

#Laboratorio 08 - Cafetería (POOH)

##########################################################################

#Funciones de archivos:

listaBebida=[]

#Validaciones:

def validarBebidaCal(tipoBebidaCaliente):
    """
    Funcionalidad: Validar si el valor ingresado está entre 1 y 4.
    Entradas: El tipo de bebida caliente str(tipoBebidaCaliente).
    Salidas: True/None.
    """
    if(tipoBebidaCaliente.isdigit()):
        tipoBebidaCaliente=int(tipoBebidaCaliente)
        if(0<tipoBebidaCaliente<=4):
            return True

def validarTipoBebida(tipoBebida):
    """
    Funcionalidad: Validar si el valor ingresado está entre 1 y 2.
    Entradas: El tipo de bebida str(tipoBebida).
    Salidas: True/None.
    """
    if(tipoBebida.isdigit()):
        tipoBebida=int(tipoBebida)
        if(0<tipoBebida<=2):
            return True

def validarTamanno(tamannoBebida):
    """
    Funcionalidad: Validar si el valor ingresado está entre 1 y 3.
    Entradas: El tamaño de la bebida str(tamannoBebida).
    Salidas: True/None.
    """
    if(tamannoBebida.isdigit()):
        tamannoBebida=int(tamannoBebida)
        if(0<tamannoBebida<=3):
            return True

def validarPrecio(pprecio):
    """
    Funcionalidad: Validar si el valor ingresado está entre 1 y 2500.
    Entradas: El precio de la bebida float(pprecio).
    Salidas: True/None.
    """
    if (0<pprecio<2500):
        return True

def validarRespuesta(hielo):
    """
    Funcionalidad: Validar si la respuesta ingresada es según se indica.
    Entradas: La respuesta sobre si se desea hielo str(hielo).
    Salidas: True/None.
    """
    hielo=hielo.lower()
    if(hielo=="si" or hielo=="sí" or hielo=="no"):
        return True
    
def validarIngredientes(pvariable):
    """
    Funcionalidad: Validar si los ingredientes tienen caracteres extraños además de la coma.
    Entradas: Los ingredientes str(pvariable).
    Salidas: True/None.
    """
    pvariable=pvariable.lower()
    for valor in pvariable:
        if(re.match("([0-9]|[^a-zA-z , ´ á é í ó ú ñ])",valor)):
            return False
    return True

def validarNombre(pvariable):
    """
    Funcionalidad: Validar si el nombre no presenta caracteres extraños.
    Entradas: El nombre de la bebida str(pvariable).
    Salidas: True/None.
    """
    pvariable=pvariable.lower()
    for valor in pvariable:
        if(re.match("([0-9]|[^a-zA-z á é í ó ú ñ])",valor)):
            return False
    return True

def validarEspacios(pvariable):
    """
    Funcionalidad: Validar que el usuario escriba algo.
    Entradas: El dato escrito str(pvariable).
    Salidas: True/None.
    """
    if(pvariable.isspace() or pvariable==""):
        return False
    else:
        return True

def validarExistencia(lista,pcodigo):
    """
    Funcionalidad: Validar si el código ya existe.
    Entradas: La lista list(lista) y el código ingresado str(pcodigo).
    Salidas: True/False.
    """
    for bebida in lista:
        if(bebida.obtenerCodigo()==pcodigo):
            return False
    return True

def validarCodigo(pcodigo):
    """
    Funcionalidad: Validar que el código esté bien ingresado.
    Entradas: El código ingresado str(pcodigo).
    Salidas: True/None.
    """
    if (re.match("^(c|f)[0-9]{2}$",pcodigo)):
        return True

##########################################################################

#Funciones principales:

def mostrarCafés(listaBebida):
    """
    Funcionalidad: Mostrar todos los cafés en la lista.
    Entradas: La lista de objetos list(listaBebida).
    Salidas: Los datos de los cafés.
    """
    try:
        print("\n       ☕ Mostrar cafés ☕")
        mostrarBebCafe(listaBebida)
    except:
        print("Datos ingresados incorrectos.")

    
def mostrarFrias(listaBebida):
    """
    Funcionalidad: Mostrar todas las bebidas frías.
    Entradas: La lista de objetos list(listaBebida).
    Salidas: Los datos de las bebidas frías.
    """
    try:
        print("\n       ☕ Mostrar bebidas frías ☕")
        mostrarBebFria(listaBebida)
    except:
        print("Datos ingresados incorrectos.")
        

def mostrarCalientes(listaBebida):
    """
    Funcionalidad: Mostrar todas las bebidas calientes.
    Entradas: La lista de objetos list(listaBebida).
    Salidas: Los datos de las bebidas calientes.
    """
    try:
        print("\n       ☕ Mostrar bebidas calientes ☕")
        mostrarBebCaliente(listaBebida)
    except:
        print("Datos ingresados incorrectos.")
    

def mostrarInventario(listaBebida):
    """
    Funcionalidad: Mostrar todos los datos de las bebidas.
    Entradas: La lista de objetos list(listaBebida).
    Salidas: Los datos de todas las bebidas.
    """
    try:
        print("\n          ☕ Mostrar todas bebidas ☕")
        mostrarTodaBebida(listaBebida)
    except:
        print("Datos ingresados incorrectos.")
        
                
def modificarPrecio(listaBebida):
    """
    Funcionalidad: Pasar el código por las validaciones y cambiar su precio.
    Entradas: Lista.
    Salidas: Lista con el precio cambiado en el código especificado.
    """
    try:
        print("\n          ☕ Cambio de precio ☕")
        while True:
            codigoBebida=input("\nIngrese el código de su bebida: ")
            if(validarCodigo(codigoBebida)):
                if(validarExistencia(listaBebida,codigoBebida))==False:
                    while True:
                        precioNuevo=int(input("Ingrese el nuevo precio: "))
                        if validarPrecio(precioNuevo):
                            cambiarPrecio(listaBebida,codigoBebida,precioNuevo)
                            graba("Bebidas",listaBebida)
                            print("El precio fue cambiado exitosamente.")
                            return False
                        else:
                            print("Ingrese un precio válido menos a 2500.")
                            continue
                else:
                    print("El código de la bebida no se encuentra registrado.")
                    continue
            else:
                print("El código ingresado no tiene el formato correcto.")
                continue
    except:
        print("Datos ingresados incorrectos.")
    

def eliminarBebidas(listaBebida):
    """
    Funcionalidad: Eliminar las bebidas.
    Entradas: La lista de objetos list(listaBebida).
    Salidas: Los datos eliminados.
    """
    try:
        print("\n          ☕ Eliminar bebidas ☕")
        while True:
            codigo=input("\nIngrese el código de la bebida: ")
            codigo=codigo.strip()
            if (validarExistencia(listaBebida,codigo)==False):
                print("El código ingresado existe.")
                borrarBebida(listaBebida,codigo)
                graba("Bebidas",listaBebida)
                return False
            else:
                print("El código ingresado no existe.")
                continue
    except:
        print("Datos ingresados incorrectos.")
 
def ingresarBebidas(listaBebida):
    """
    Funcionalidad: Ingresar las bebidas.
    Entradas: La lista de objetos list(listaBebida).
    Salidas: Los datos ingresados.
    """
    try:
        print("\n          ☕Ingreso de bebidas ☕")
        print(
                        """
Ingrese el código de su bebida con el siguiente formato:

                    letra##

Donde "letra" debe ser una de las siguientes y en minúscula:
                    f)Frío
                    c)Caliente
                        
                        """)
        while True:
            codigoBebida=input("\nIngrese el código de su bebida: ")
            if(validarCodigo(codigoBebida)):
                if(validarExistencia(listaBebida,codigoBebida)):
                    while True:
                        nombreBebida=input("\nIngrese el nombre de su bebida: ")
                        if(validarEspacios(nombreBebida) and validarNombre(nombreBebida)):
                           nombreBebida=nombreBebida.capitalize()
                           while True:
                                ingredientesBebida=input("\nIngrese los ingredientes de su bebida separados por comas: ")
                                if(validarEspacios(ingredientesBebida) and validarIngredientes(ingredientesBebida)):
                                    while True:
                                        ingredientesLista=generarListaIngr(ingredientesBebida)
                                        try:
                                            precioBebida=float(input("\nIngrese el precio de la bebida (menor de 2500): "))
                                            if(validarPrecio(precioBebida)):
                                                while True:
                                                    print("""
¿Qué tamaño de bebida desea?
1) Pequeño
2) Mediana
3) Grande
                                                                   """)
                                                    tamannoBebida=input("Ingrese el tamaño de bebida que desea: ")
                                                    if(validarTamanno(tamannoBebida)):
                                                       while True:
                                                        if(reconocerTipo(codigoBebida)==1):
                                                            tipoBebida=1
                                                            print("\n¿Desea hielo en su bebida fría?")
                                                            hielo=input("Escriba sí o no: ")
                                                            if(validarRespuesta(hielo)):
                                                                hielo=generarBool(hielo)
                                                                while True:
                                                                 print("""
¿Qué tipo de bebida desea?
1) Natural
2) Gaseosa
                                                                       """)
                                                                 tipoBebidaFria=input("Ingrese el tipo de bebida que desea: ")
                                                                 if(validarTipoBebida(tipoBebidaFria)):
                                                                    tipoBebidaFria=generarBool2(tipoBebidaFria)
                                                                    while True:
                                                                        bebidaFria=Fria(codigoBebida,tipoBebida,nombreBebida,
                                                                        ingredientesLista,precioBebida,int(tamannoBebida),hielo,tipoBebidaFria)
                                                                        listaBebida.append(bebidaFria)
                                                                        graba("Bebidas",listaBebida)
                                                                        return False
                                                                 else:
                                                                     print("Ingrese un 1 o 2.")
                                                                     continue
                                                            else:
                                                                print("Ingrese sí o no.")
                                                                continue
                                                        else:
                                                             tipoBebida=2
                                                             print("""
¿Qué tipo de bebida caliente desea?
1) Chocolate
2) Té
3) Café
4) Aguadulce
                                                                       """)
                                                             tipoBebidaCaliente=input("Ingrese el tipo de bebida: ")
                                                             if(validarBebidaCal(tipoBebidaCaliente)):
                                                                 while True:
                                                                    bebidaCaliente=Caliente(codigoBebida,tipoBebida,nombreBebida,
                                                                    ingredientesLista,precioBebida,int(tamannoBebida),int(tipoBebidaCaliente))
                                                                    listaBebida.append(bebidaCaliente)
                                                                    graba("Bebidas",listaBebida)
                                                                    return False
                                                             else:
                                                                 print("Ingrese un 1, 2, 3 o 4.")
                                                                 continue   
                                                    else:
                                                        print("Ingrese un 1, 2 o 3.")
                                                        continue
                                            else:
                                                print("Ingrese un precio menor a 2500 y mayor que 0.")
                                                continue
                                        except ValueError:
                                            print("Ingrese un número.")
                                            continue                 
                                else:
                                    print("Por favor ingrese al menos un ingrediente y sin números, ni otros caracteres además de la coma.")
                                    continue
                        else:
                            print("Por favor ingrese un nombre sin números ni carácteres extraños.")
                            continue
                else:
                    print("El código ya existe.")
                    continue
            else:
                print("El código fue ingresado incorrectamente.")
                continue
            return False
    except xxx:
        print("Datos ingresados incorrectos.")

def menuMostrar(listaBebida):
    """
    Funcionalidad: Mostrar el menú de mostreo de datos.
    Entradas: Opción escogida del menú.
    Salidas: Los valores que retorne cada función llamada en el menú.
    """
    menu=True
    while menu:
        print(
            """
⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘
⌘                                                                ⌘
⌘                   Menú de mostreo de datos                     ⌘
⌘                                                                ⌘
⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘
⌘                                                                ⌘
⌘ 1.  Información de todas las bebidas frías                     ⌘
⌘ 2.  Información de todas las bebidas calientes                 ⌘
⌘ 3.  Información de todos los cafés                             ⌘
⌘ 4.  Volver al menú principal                                   ⌘
⌘                                                                ⌘
⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘
        """)

        menuOpcion=input("\nღIngrese una opción del menú de mostreo: ")
        if (menuOpcion=="1"):
                mostrarFrias(listaBebida) 
        elif (menuOpcion=="2"):
                mostrarCalientes(listaBebida)
        elif (menuOpcion=="3"):
                mostrarCafés(listaBebida)
        elif (menuOpcion=="4"):
                menuPrincipal()         
        else:
            print("Esa opción no existe, ingrese otra.\n")
    return

def menuPrincipal():
    """
    Funcionalidad: Mostrar el menú principal.
    Entradas: Opción escogida del menú.
    Salidas: Los valores que retorne cada función llamada en el menú.
    """
    archivo="Bebidas"
    listaBebida=lee(archivo)
    menu=True
    while menu:
        print(
            """
⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘
⌘                                                                ⌘
⌘                     Menú principal                             ⌘
⌘                                                                ⌘
⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘
⌘                                                                ⌘
⌘ 1.  Registrar bebida                                           ⌘
⌘ 2.  Eliminar bebida                                            ⌘
⌘ 3.  Cambiar precio                                             ⌘
⌘ 4.  Mostrar inventario completo                                ⌘
⌘ 5.  Mostrar un tipo de producto                                ⌘
⌘ 6.  Salir                                                      ⌘
⌘                                                                ⌘
⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘
        """)

        menuOpcion=input("\nღIngrese una opción del menú principal: ")
        if (menuOpcion=="1"):
                ingresarBebidas(listaBebida) 
        elif (menuOpcion=="2"):
                eliminarBebidas(listaBebida)
        elif (menuOpcion=="3"):
                modificarPrecio(listaBebida)
        elif (menuOpcion=="4"):
                mostrarInventario(listaBebida)
        elif (menuOpcion=="5"):
                menuMostrar(listaBebida)
        elif (menuOpcion=="6"):
                graba("Bebidas",listaBebida)
                print("...")
                time.sleep(3)
                print("""
ღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღ
ღ                                                                             ღ
ღ                                ¡Adiós!                                      ღ
ღ                                                                             ღ
ღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღ
                      """)
                sys.exit()       
        else:
            print("Esa opción no existe, ingrese otra.\n")
    return


print(" ☕ Bienvenido al sistema de registro de bebidas ☕")
menuPrincipal()
