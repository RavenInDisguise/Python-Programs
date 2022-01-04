########################################################################
# Elaborado por: Mónica Alfaro P.
# Fecha de creación: 03/06/2020 14:10
# Fecha de última modificación: 04/06/2020 00:00
# Versión: 3.8.2
########################################################################

#Importación de librerías:

import re
import sys
from libreriaPlasma import *

########################################################################

#Definición lista original de donantes:

recuperadosDonantes=["303500620","101110218","412340987","267893456",
                     "154328765","534561234","187674329","265437654",
                     "243214321","187654321","187659870","687659870",
                     "887659870","945659823"]

########################################################################

#Función del menú:

########################################################################

def continuar():
    """
    Funcionalidad: Saber si continuar o no.
    Entradas: La respuesta (seguir).
    Salidas: Vuelve a ingresar código o acaba.
    """ 
    seguir=input("\nღDesea realizar esta acción nuevamente? (Sí/No) ")
    respuesta=seguirOno(seguir)
    if respuesta.isupper():
        return 
    elif respuesta.islower():
        menuPrinc()
    else:
        print("Ingrese Si/No ")
        continuar()

########################################################################

#Funciones del Lab:

########################################################################
        
#Proceso #1:       
        
def validarCantidad(pcantidad):
    """
    Funcionalidad: Validar si la cantidad ingresada es mayor cero.
    Entrada: La cantidad de cédulas que desea ingresar el usuario int(pcantidad).
    Salida: True/False.
    """
    if(pcantidad>0):
        return True
    
def ingresarCedulas():
    """
    Funcionalidad: Ingresar la cantidad de cédulas que desea agregar.
    Entrada: La cantidad que desea ingresar el usuario int(pcantidad) y la cédula int(cedula).
    Salida: Se muestra un mensaje de acuerdo a cómo fue el ingreso de datos (erróneo o no). 
    """
    while True:
        try:
            print("\nღProceso para agregar convalecientes donadores del día:")
            cantidad=int(input("Indique la cantidad de cédulas que desea agregar: "))
            contador=1
            if(validarCantidad(cantidad)):
                 while contador<=cantidad:
                     cedula=input("Ingrese la cédula sin espacios ni guiones: ")
                     salidas=listarCedulas(cedula,recuperadosDonantes)
                     if salidas[1]:
                         contador+=1
                     else:
                         contador
                 print("Números de cédula agregados efectivamente.")
                 continuar()
            else:
                print("El número ingresado debe ser mayor que 0.")
                continue
            
        except ValueError:
            print("Debe ingresar una cantidad y una cédula válida con números enteros, sin espacios ni guiones.")
            continue
        
########################################################################

#Proceso #2:
        
def ingresarCedulas2():
    """
    Funcionalidad: Decodifica un número de cédula para saber la provincia, tomo y asiento.
    Entrada: La cédula.
    Salida: Los datos (provincia, tomo y asiento).
    """
    while True:
        try:
            print("\nღProceso para decodificar donador:")
            cedula=int(input("Indique el número de cédula que desea averiguar: "))
            pcedula=str(cedula)
            indice=int(pcedula[0])
            if(validarCedula(cedula)):
                if not(buscarCedulas(cedula,recuperadosDonantes)):
                    if(indice<8):
                        print("Usted nació en la provincia de: "+str(generarProvincia(indice))+" en el tomo: "
                              +str(generarTomo(cedula))+" y el asiento: "+str(generarAsiento(cedula)))
                        continuar()
                    else:
                        print("Usted es parte de los "+str(generarProvincia(indice))+" en el tomo: "
                              +str(generarTomo(cedula))+" y el asiento: "+str(generarAsiento(cedula)))
                        continuar()
                else:
                    print("El donador no es un donante aún.")
                    continuar()
            else:
                print("Debe ingresar un número de cédula válido una cédula con números enteros, sin espacios ni guiones.")
                continue
            
        except ValueError:
            print("Debe ingresar una cédula con números enteros, sin espacios ni guiones.")
            continue

########################################################################

#Proceso #3:

def validarOpcion(popcion):
    """
    Funcionalidad: Verifica que la opción esté entre 0 y 10.
    Entrada: Número de opción.
    Salida: True (si es correcto) o False (si no cumple).
    """
    if(0<popcion<10):
        return True
    
def ingresarCedulas3():
    """
    Funcionalidad: Muestra el menú provincias y permite elegir una para ver sus cédulas.
    Entrada: Número de provincia.
    Salida: Las cédulas de los donantes de la provincia elegida.
    """
    while True:
        try:
            print("\nღProceso para mostrar cantidad de cédulas según la siguiente codificación:")
            print(
            """
⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘
⌘        ⌘                                                      ⌘
⌘ Código ⌘  Provincia                                           ⌘
⌘        ⌘                                                      ⌘     
⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘
⌘        ⌘                                                      ⌘
⌘  1     ⌘  San José                                            ⌘ 
⌘  2     ⌘  Alajuela                                            ⌘
⌘  3     ⌘  Cartago                                             ⌘  
⌘  4     ⌘  Heredia                                             ⌘  
⌘  5     ⌘  Guanacaste                                          ⌘
⌘  6     ⌘  Puntarenas                                          ⌘
⌘  7     ⌘  Limón                                               ⌘ 
⌘  8     ⌘  Nacionalizados o naturalizados (Extranjero)         ⌘
⌘  9     ⌘  Partida especial de nacimientos (Casos especiales)  ⌘
⌘        ⌘                                                      ⌘
⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘
            """)
            opcion=int(input("Ingrese la opción que desea mostrar: "))
            if(validarOpcion(opcion)):
                salida=listarDonadores(opcion,recuperadosDonantes)
                if(opcion<8):
                    print("Los donadores de la provincia de "+str(generarProvincia(opcion))+" son: "
                          +str(salida[0])+" con las cédulas:\n"
                          +str(salida[1]))
                    continuar()
                else:
                     print("Los donadores "+str(generarProvincia(opcion))+" son: "
                          +str(salida[0])+" con las cédulas:\n"
                          +str(salida[1]))
                     continuar() 
            else:
                print("El número ingresado debe ser mayor que cero y menor que nueve.")
                continue
                
        except ValueError:
            print("Debe ingresar una cantidad con números enteros.")
            continue
            
########################################################################

#Proceso #4:

def ingresarCedulas4():
    """
    Funcionalidad: Mostrar los donantes registrados en todo el país.
    Entrada: Provincia y lista de recuperados donantes.
    Salida: Los datos de los donantes totales.
    """
    while True:
        try:
            print("\nღProceso para mostrar los donadores totales del país:")
            contarProvincias(recuperadosDonantes,provincia)
            print("\n")
            break
            continuar()
        except:
            print("Dato inválido.")
            continue

########################################################################

#Proceso #5:

def validarOpcion2(popcion):
    """
    Funcionalidad: Verifica que la opción esté entre 0 y 3.
    Entrada: La opción.
    Salida: True (cumple) o False (cumple)
    """
    if(0<popcion<3):
        return True
        
def ingresarCedulas5():
    """
    Funcionalidad: Permite ver la listas de cédulas de donantes nacionalizados o de casos especiales.
    Entrada: Opción a elegir (1 para nacionalizados o 2 para extranjeros).
    Salida: Los datos de las cédulas de la opción elegida.
    """
    while True:
        try:
            print("\nღProceso para mostrar cantidad de cédulas según la siguiente codificación:")
            print(
            """
⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘
⌘         ⌘                                                     ⌘
⌘ Código  ⌘ Provincia                                           ⌘
⌘         ⌘                                                     ⌘
⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘
⌘         ⌘                                                     ⌘
⌘   1     ⌘ Nacionalizados o naturalizados (Extranjero).        ⌘
⌘   2     ⌘ Partida especial de nacimientos (Casos especiales). ⌘
⌘         ⌘                                                     ⌘
⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘
            """)
            opcion=int(input("Ingrese la opción que desea mostrar: "))
            if(validarOpcion2(opcion)):
                opcion=opcion+7
                salida=listarDonadores(opcion,recuperadosDonantes)
                if(opcion==1):
                    print("Los donadores de la provincia de "+str(generarProvincia(opcion))+" son: "
                          +str(salida[0])+" con las cédulas:\n"
                          +str(salida[1]))
                    continuar()
                else:
                     print("Los donadores "+str(generarProvincia(opcion))+" son: "
                          +str(salida[0])+" con las cédulas:\n"
                          +str(salida[1]))
                     continuar() 
            else:
                print("El número ingresado debe ser mayor que cero y menor que tres.\n")
                continue
                
        except ValueError:
            print("Debe ingresar una cantidad con números enteros.\n")
            continue     
    
        
########################################################################  

#Menú principal:


def menuPrinc():
    """
    Funcionalidad: Mostrar el menú principal.
    Entradas: Ninguna.
    Salidas: Opción escogida del menú.
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
⌘ 1.  Agregar convalecientes donadores del día.                  ⌘
⌘ 2.  Decodificar donador.                                       ⌘
⌘ 3.  Listar donadores según el Registro de Naturalizaciones.    ⌘
⌘ 4.  Donadores totales del país.                                ⌘
⌘ 5.  Listar donadores extranjeros.                              ⌘
⌘ 6.  Salir del programa.                                        ⌘
⌘                                                                ⌘
⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘
        """)

        menuOpcion=input("\nღIngrese una opción del menú principal: ")
        if (menuOpcion=="1"):
                ingresarCedulas()
        elif (menuOpcion=="2"):
                ingresarCedulas2()
                
        elif (menuOpcion=="3"):
                ingresarCedulas3()
        
        elif (menuOpcion=="4"):
                ingresarCedulas4()
                
        elif (menuOpcion=="5"):
                ingresarCedulas5()
                
        elif (menuOpcion=="6"):
            
                print("""
ღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღ
ღ                                                                             ღ
ღ  ¡Gracias por donar tu sangre, ahora fuiste tú, luego espero poder ser yo!  ღ
ღ                                                                             ღ
ღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღღ
                      """)
                sys.exit()       
        else:
            print("Esa opción no existe, ingrese otra.\n")
    return 

########################################################################

#Llamada al menú principal:

print(
    """
⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘
⌘                                                                     ⌘   
⌘ ¡Bienvenido al sistema para donadores sobre el suero convaleciente! ⌘ 
⌘                                                                     ⌘   
⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘⌘
      """)
menuPrinc()
        
