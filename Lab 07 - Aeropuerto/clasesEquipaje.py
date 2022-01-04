##########################################################################
#Elaborado por Mónica Alfaro Parrales y Jennifer Alvarado Brenes
#Inicio 04/07/2020 01:20 pm
#Última modificación 04/07/2020 22:50 pm
#Versión 3.8.2
##########################################################################

class Equipaje:
    def __init__(atri):
        atri.codigo=""
        atri.peso=0
        atri.tamano=False
        atri.fragilidad=False
        atri.descripcion=""
        atri.estado=0
       
    def asignarCodigo(atri,pcodigo):
        """
        Funcionalidad: Asigna el código ingresado al atributo.
        Entradas: Dato ingresado.
        Salidas: El atributo con el dato.
        """
        atri.codigo=pcodigo
       
    def asignarPeso(atri,ppeso):
        """
        Funcionalidad: Asigna el peso ingresado al atributo.
        Entradas: Dato ingresado.
        Salidas: El atributo con el dato.
        """
        atri.peso=ppeso
    
    def asignarTamano(atri,ptamano):
        """
        Funcionalidad: Asigna el tamaño ingresado al atributo.
        Entradas: Dato ingresado.
        Salidas: El atributo con el dato.
        """
        if ptamano==1:
            atri.tamano=True #de mano
        else:
            atri.tamano=False #grande
       
    def asignarFragilidad(atri,pfragilidad):
        """
        Funcionalidad: Asigna la fragilidad ingresado al atributo.
        Entradas: Dato ingresado.
        Salidas: El atributo con el dato.
        """
        if pfragilidad==1:
            atri.fragilidad=True #frágil
        else:
            atri.fragilidad=False #fuerte

    def asignarDescripcion(atri,pdescripcion):
        """
        Funcionalidad: Asigna la descripción ingresado al atributo.
        Entradas: Dato ingresado.
        Salidas: El atributo con el dato.
        """
        atri.descripcion=pdescripcion

    def asignarEstado(atri,pestado):
        """
        Funcionalidad: Asigna el estado ingresado al atributo.
        Entradas: Dato ingresado.
        Salidas: El atributo con el dato.
        """
        if pestado==1:
            atri.estado="Recibido"
        elif pestado==2:
            atri.estado="Entregado"
        elif pestado==3:
            atri.estado="No entregado"
        else:
            atri.estado="Perdido-avería"
    def obtenerCodigo(atri):
        """
        Funcionalidad: Obtiene el código del atributo.
        Entradas: El atributo.
        Salidas: El dato.
        """
        return atri.codigo
    def obtenerPeso(atri):
        """
        Funcionalidad: Obtiene el peso del atributo.
        Entradas: El atributo.
        Salidas: El dato.
        """
        return atri.peso
    def obtenerTamano(atri):
        """
        Funcionalidad: Obtiene el tamaño del atributo.
        Entradas: El atributo.
        Salidas: El dato.
        """
        return atri.tamano
    def obtenerFragilidad(atri):
        """
        Funcionalidad: Obtiene la fragilidad del atributo.
        Entradas: El atributo.
        Salidas: El dato.
        """
        return atri.fragilidad
    def obtenerDescripcion(atri):
        """
        Funcionalidad: Obtiene la descripción del atributo.
        Entradas: El atributo.
        Salidas: El dato.
        """
        return atri.descripcion
    def obtenerEstado(atri):
        """
        Funcionalidad: Obtiene el estado del atributo.
        Entradas: El atributo.
        Salidas: El dato.
        """
        return atri.estado
            


