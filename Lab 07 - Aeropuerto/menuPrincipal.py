##########################################################################
#Elaborado por: Mónica Alfaro Parrales y Jennifer Alvarado Brenes
#Inicio: 04/07/2020 01:20 pm
#Última modificación: 04/07/2020 22:00
#Versión 3.8.2
##########################################################################

#Importación de librerías:

from clasesEquipaje import *
from funciones import *
import re
import time
import sys

##########################################################################

#Laboratorio 07 - Equipaje (POO)

def validarCed(cedula):
    """
    Funcionalidad: Validar la cédula ingresada.
    Entradas: Cédula str(cedula).
    Salidas: True/False.
    """
    if len(cedula)==9:
        for numero in cedula:
            if numero.isdigit():
                continue
            else:
                return False
        return True
    else:
        return False
    
def validarCod(codigo):
    """
    Funcionalidad: Validar el código ingresado.
    Entradas: Código str(codigo).
    Salidas: True/None.
    """
    if(re.findall("^\w{4}(-)[0-9]{9}$",codigo)):
        return True

def validarPeso(peso):
    """
    Funcionalidad: Validar el peso ingresado.
    Entradas: Peso str(peso).
    Salidas: True/None.
    """
    if(peso>0):
        return True

def validarTamano(tamano):
    """
    Funcionalidad: Validar el tamaño ingresado.
    Entradas: Tamaño str(tamano).
    Salidas: True/None.
    """
    if(tamano==1 or tamano==2):
        return True
    
def validarEstado(estado):
    """
    Funcionalidad: Validar el estado ingresado.
    Entradas: Estado str(estado).
    Salidas: True/None.
    """
    if(1<=estado<=4):
        return True
    
def ingresarMaleta(listaEquipajes):
    """
    Funcionalidad: Ingresar las maletas.
    Entradas: La lista de equipajes list(listaEquipajes).
    Salidas: La lista llena con los valores ingresados.
    """
    while True:
        try:
            equipaje=Equipaje()
            vcodigo=input("\nIngrese el código de su equipaje (4 caracteres del código de vuelo - su número de cédula): ")
            vcodigo=vcodigo.strip()
            if(validarCod(vcodigo)):
                if buscarCodigo(listaEquipajes,vcodigo):
                    while True:
                        equipaje.asignarCodigo(vcodigo)
                        print("\nEl peso se tomará como el número de kg, puede llevar decimales.")
                        vpeso=float(input("Ingrese el peso de su equipaje: "))
                        if(validarPeso(vpeso)):
                            while True:
                                equipaje.asignarPeso(vpeso)
                                print("\nEl tamaño se tomará como 1 si es maleta de mano o 2 si es equipaje grande.")
                                print("""
                                1. De mano.
                                2. Grande.
                                """)
                                vtamano=int(input("Ingrese el tamaño de su equipaje: "))
                                if(validarTamano(vtamano)):
                                    while True:
                                        equipaje.asignarTamano(vtamano)
                                        print("\nEste dato se tomará como 1 si es frágil o 2 si no es frágil.")
                                        print("""
                                1. Frágil.
                                2. No frágil.
                                """)
                                        vfragilidad=int(input("Indique la fragilidad de su equipaje: "))
                                        if(validarTamano(vfragilidad)):
                                            while True:
                                                equipaje.asignarFragilidad(vfragilidad)
                                                print("\nEl estado se su maleta tiene las siguientes opciones.")
                                                print("""
                                1. Recibido.
                                2. Entregado.
                                3. No entregado.
                                4. Perdido - avería. """)
                                                vestado=int(input("\nIngrese el estado de su equipaje: "))
                                                if(validarEstado(vestado)):
                                                    while True:
                                                        equipaje.asignarEstado(vestado)
                                                        print("\nEscriba la apariencia de su equipaje.")
                                                        vdescripcion=input("Ingrese la descripción: ")
                                                        vdescripcion=vdescripcion.capitalize()
                                                        equipaje.asignarDescripcion(vdescripcion)
                                                        listaEquipajes.append(equipaje)
                                                        return False,listaEquipajes
                                                else:
                                                    print("Ingrese un valor entre 1 y 4.")
                                                    continue
                                        else:
                                            print("Ingrese un valor entre 1 y 2.")
                                            continue
                                else:
                                    print("Ingrese un valor entre 1 y 2.")
                                    continue
                        else:
                            print("Ingrese un peso mayor de 0 y sin escribir la abreviatura 'kg'.")
                            continue
                else:
                    print("La maleta ya está registrada.")
                    continue
            else:
                print("Ingrese un código válido: alfanumérico de 4 cifras con un guión y con la cédula (sin caracteres extras, ni espacios).")
                continue
           
        except ValueError:
            print("Ingrese un número válido.")
            continue        
        
def eliminarMaleta(listaEquipajes):
    """
    Funcionalidad: Eliminar la maleta.
    Entradas: Código str(elimCodigo) y la lista list(listaEquipajes). 
    Salidas: La maleta eliminada si cumple con los debidos requisitos.
    """
    while True:
        try:
            elimCodigo=input("\nIngrese el código de la maleta que desea eliminar: ")
            elimCodigo=elimCodigo.strip()
            if(validarCod(elimCodigo)):
                while True:
                    if(buscarCodigo(listaEquipajes,elimCodigo)==False):
                        eliminarMaletas(listaEquipajes,elimCodigo)
                    else:
                        print("La maleta no existe en el registro.")
                    return False
            else:
                print("Ingrese un código válido: alfanumérico de 4 cifras con un guión y con la cédula (sin caracteres extras, ni espacios).")
                continue           
        except:       
            print("Ingrese un valor válido.")
            continue

def modificarPeso(listaEquipajes):
    """
    Funcionalidad: Modificar peso.
    Entradas: Código str(vcodigo) y la lista list(listaEquipajes). 
    Salidas: El peso modificado si cumple los requisitos.
    """
    while True:
        try:
             vcodigo=input("\nIngrese el código de su equipaje (4 caracteres del código de vuelo - su número de cédula): ")
             vcodigo=vcodigo.strip()
             if(validarCod(vcodigo)):
                if buscarCodigo(listaEquipajes,vcodigo)==False:
                    while True:
                         print("\nEl peso se tomará como el número de kg, puede llevar decimales.")
                         vpeso=float(input("Ingrese el peso de su equipaje: "))
                         if(validarPeso(vpeso)):
                             modificarPesos(listaEquipajes,vpeso,vcodigo)
                         else:
                            print("Ingrese un peso mayor de 0 y sin escribir la abreviatura 'kg'.")
                            continue
                         return False
                             
                else:
                    print("La maleta no existe en el registro.")
                    return False
             else:
                print("Ingrese un código válido: alfanumérico de 4 cifras con un guión y con la cédula (sin caracteres extras, ni espacios).")
                continue     
                
        except:
            print("Ingrese un valor válido.")
            continue

def modificarTamano(listaEquipajes):
    """
    Funcionalidad: Modificar tamaño.
    Entradas: Código str(vcodigo) y la lista list(listaEquipajes).
    Salidas: El tamaño modificado si cumple los requisitos.
    """
    while True:
        try:
             vcodigo=input("\nIngrese el código de su equipaje (4 caracteres del código de vuelo - su número de cédula): ")
             vcodigo=vcodigo.strip()
             if(validarCod(vcodigo)):
                if buscarCodigo(listaEquipajes,vcodigo)==False:
                    while True:
                         print("\nEl tamaño se tomará como 1 si es maleta de mano o 2 si es equipaje grande.")
                         print("""
                         1. De mano.
                         2. Grande.
                         """)
                         vtamano=int(input("Ingrese el tamaño de su equipaje: "))
                         if(validarTamano(vtamano)):
                             modificarTamanos(listaEquipajes,vtamano,vcodigo)
                         else:
                             print("Ingrese un valor entre 1 y 2.")
                             continue
                         return False
                else:
                    print("La maleta no existe en el registro.")
                    return False
             else:
                print("Ingrese un código válido: alfanumérico de 4 cifras con un guión y con la cédula (sin caracteres extras, ni espacios).")
                continue     
                
        except:
            print("Ingrese un valor válido.")
            continue

def modificarFragil(listaEquipajes):
    """
    Funcionalidad: Modificar fragilidad.
    Entradas: Código str(vcodigo) y la lista list(listaEquipajes).
    Salidas: La fragilidad modificada si cumple los requisitos.
    """
    while True:
        try:
             vcodigo=input("\nIngrese el código de su equipaje (4 caracteres del código de vuelo - su número de cédula): ")
             vcodigo=vcodigo.strip()
             if(validarCod(vcodigo)):
                if buscarCodigo(listaEquipajes,vcodigo)==False:
                    print("\nEste dato se tomará como 1 si es frágil o 2 si no es frágil.")
                    print("""
                    1. Frágil.
                    2. No frágil.
                    """)
                    vfragilidad=int(input("Indique la fragilidad de su equipaje: "))
                    if(validarTamano(vfragilidad)):
                         modificarFragilidad(listaEquipajes,vfragilidad,vcodigo)   
                    else:
                         print("Ingrese un valor entre 1 y 2.")
                         continue
                    return False
             else:
                print("Ingrese un código válido: alfanumérico de 4 cifras con un guión y con la cédula (sin caracteres extras, ni espacios).")
                continue     
                
        except:
            print("Ingrese un valor válido.")
            continue

def modificarEstado(listaEquipajes):
    """
    Funcionalidad: Modificar estado.
    Entradas: Código str(vcodigo) y la lista list(listaEquipajes).
    Salidas: El estado modificado si cumple los requisitos.
    """
    while True:
        try:
             vcodigo=input("\nIngrese el código de su equipaje (4 caracteres del código de vuelo - su número de cédula): ")
             vcodigo=vcodigo.strip()
             if(validarCod(vcodigo)):
                if buscarCodigo(listaEquipajes,vcodigo)==False:
                    print("\nEl estado se su maleta tiene las siguientes opciones.")
                    print("""
                    1. Recibido.
                    2. Entregado.
                    3. No entregado.
                    4. Perdido - avería. """)
                    vestado=int(input("\nIngrese el estado de su equipaje: "))
                    if(validarEstado(vestado)):
                         modificarEstados(listaEquipajes,vestado,vcodigo)   
                    else:
                         print("Ingrese un valor entre 1 y 2.")
                         continue
                    return False
             else:
                print("Ingrese un código válido: alfanumérico de 4 cifras con un guión y con la cédula (sin caracteres extras, ni espacios).")
                continue     
                
        except:
            print("Ingrese un valor válido.")
            continue

def modificarDescripcion(listaEquipajes):
    """
    Funcionalidad: Modificar descripción.
    Entradas: Código str(vcodigo) y la lista list(listaEquipajes).
    Salidas: La descripción modificada si cumple los requisitos.
    """
    while True:
        try:
             vcodigo=input("\nIngrese el código de su equipaje (4 caracteres del código de vuelo - su número de cédula): ")
             vcodigo=vcodigo.strip()
             if(validarCod(vcodigo)):
                if buscarCodigo(listaEquipajes,vcodigo)==False:
                   vdescripcion=input("Ingrese la descripción: ")
                   modificarDescrip(listaEquipajes,vdescripcion,vcodigo)   
                else:
                    print("La maleta no existe en el registro.")
                return False
             else:
                print("Ingrese un código válido: alfanumérico de 4 cifras con un guión y con la cédula (sin caracteres extras, ni espacios).")
                continue     
                
        except:
            print("Ingrese un valor válido.")
            continue       

def consultarPersona(listaEquipajes):
    """
    Funcionalidad: Consultar el equipaje por persona.
    Entradas: Cédula str(cedula) y la lista list(listaEquipajes).
    Salidas: La lista de maletas que le pertenece a esa persona.
    """
    while True:
        try:
            cedula=input("\nIngrese la cédula sin guiones ni espacios: ")
            if validarCed(cedula):
                print(str(consultarCedula(listaEquipajes,cedula)))
                return False
            else:
                print("Ingrese una cédula válida, sin guiones ni espacios.")
                continue
            
        except:
            print("Ingrese una cédula válida, sin guiones ni espacios.")
            continue
             
def menuModificarMaletas(listaEquipajes):
    """
    Funcionalidad: Mostrar el menú principal.
    Entradas: Opción escogida del menú.
    Salidas: Los valores que retorne cada función llamada en el menú.
    """
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
⌘ 1.  Modificar peso                                             ⌘
⌘ 2.  Modificar tamaño                                           ⌘
⌘ 3.  Modificar fragilidad                                       ⌘
⌘ 4.  Modificar descripción                                      ⌘
⌘ 5.  Modificar estado                                           ⌘               
⌘ 6.  Salir                                                      ⌘
⌘                                                                ⌘
⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘
        """)

        menuOpcion=input("\nღIngrese una opción del menú principal: ")
        if (menuOpcion=="1"):
                modificarPeso(listaEquipajes)
        elif (menuOpcion=="2"):
                modificarTamano(listaEquipajes)
        elif (menuOpcion=="3"):
                modificarFragil(listaEquipajes)
        elif (menuOpcion=="4"):
                modificarDescripcion(listaEquipajes)
        elif (menuOpcion=="5"):
                modificarEstado(listaEquipajes)
        elif(menuOpcion=="6"):
            menuPrincipal(listaEquipajes)
            
        else:
            print("Esa opción no existe, ingrese otra.\n")
    return
        
def menuConsultarMaletas(listaEquipajes):
    """
    Funcionalidad: Menú de consultas de maletas.
    Entradas: Valor del menú.
    Salidas: Los valores que retorne cada función llamada en el menú. 
    """
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
⌘ 1.  Maletas totales                                            ⌘
⌘ 2.  Maletas por persona                                        ⌘
⌘ 3.  Salir del programa                                         ⌘
⌘                                                                ⌘
⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘
        """)
        menuOpcion=input("\nღIngrese una opción del menú principal: ")
        if (menuOpcion=="1"):
            consultarTotal(listaEquipajes)
        elif (menuOpcion=="2"):
            consultarPersona(listaEquipajes)
        elif (menuOpcion=="3"):
            menuPrincipal(listaEquipajes)
        else:
            print("Esa opción no existe, ingrese otra.\n")
            continue
    return
  
def menuPrincipal(listaEquipajes):
    """
    Funcionalidad: Mostrar el menú principal.
    Entradas: Opción escogida del menú.
    Salidas: Los valores que retorne cada función llamada en el menú.
    """
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
⌘ 1.  Registrar maletas                                          ⌘
⌘ 2.  Eliminar maletas                                           ⌘
⌘ 3.  Modificar maletas                                          ⌘
⌘ 4.  Consultar maletas                                          ⌘
⌘ 5.  Salir del programa                                         ⌘
⌘                                                                ⌘
⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘
        """)

        menuOpcion=input("\nღIngrese una opción del menú principal: ")
        if (menuOpcion=="1"):
                ingresarMaleta(listaEquipajes) 
        elif (menuOpcion=="2"):
                eliminarMaleta(listaEquipajes)
        elif (menuOpcion=="3"):
                menuModificarMaletas(listaEquipajes)
        elif (menuOpcion=="4"):
                menuConsultarMaletas(listaEquipajes)
        elif (menuOpcion=="5"):
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

listaEquipajes=[]
print(" ღBienvenido al sistema de registro de maletas en el Aeropuertoღ")
menuPrincipal(listaEquipajes)
