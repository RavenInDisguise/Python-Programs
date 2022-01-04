##########################################################################
#Elaborado por Mónica Alfaro Parrales y Jennifer Alvarado Brenes
#Inicio 22/07/2020 12:33pm
#Última modificación 22/07/2020 XX:XX 
#Versión 3.8.2
##########################################################################

class Bebida():
    #Definición atributos
    pcodigo=""
    ptipo=int
    pnombre=""
    pingredientes=[]
    pprecio=float
    ptamanno=int
    def __init__(atri,pcodigo,ptipo,pnombre,pingredientes,pprecio,ptamanno):
        atri.codigo=pcodigo
        atri.tipo=ptipo
        atri.nombre=pnombre
        atri.ingredientes=pingredientes
        atri.precio=pprecio
        atri.tamanno=ptamanno

    def asignarTipo(atri,ptipo):
        """
        Funcionalidad: Asigna el tipo ingresado al atributo.
        Entradas: Dato ingresado.
        Salidas: El atributo con el dato.
        """
        atri.tipo=ptipo
        
    def asignarCodigo(atri,pcodigo):
        """
        Funcionalidad: Asigna el código ingresado al atributo.
        Entradas: Dato ingresado.
        Salidas: El atributo con el dato.
        """
        atri.codigo=pcodigo
       
    def asignarNombre(atri,pnombre):
        """
        Funcionalidad: Asigna el nombre ingresado al atributo.
        Entradas: Dato ingresado.
        Salidas: El atributo con el dato.
        """
        atri.nombre=pnombre
       
    def asignarIngredientes(atri,pingredientes):
        """
        Funcionalidad: Asigna los ingredientes ingresados al atributo.
        Entradas: Dato ingresado.
        Salidas: El atributo con el dato.
        """
        atri.ingredientes=pingredientes
    
    def asignarPrecio(atri,pprecio):
        """
        Funcionalidad: Asigna el precio ingresado al atributo.
        Entradas: Dato ingresado.
        Salidas: El atributo con el dato.
        """
        atri.precio=pprecio
       
    def asignarTamanno(atri,ptamanno):
        """
        Funcionalidad: Asigna el tamaño ingresado al atributo.
        Entradas: Dato ingresado.
        Salidas: El atributo con el dato.
        """
        atri.tamanno=ptamanno

    def obtenerCodigo(atri):
        """
        Funcionalidad: Obtiene el código del atributo.
        Entradas: El atributo.
        Salidas: El dato.
        """
        return atri.codigo
    
    def obtenerTipo(atri):
        """
        Funcionalidad: Obtiene el tipo del atributo.
        Entradas: El atributo.
        Salidas: El dato.
        """
        return atri.tipo

    def obtenerNombre(atri):
        """
        Funcionalidad: Obtiene el nombre del atributo.
        Entradas: El atributo.
        Salidas: El dato.
        """
        return atri.nombre
    
    def obtenerIngredientes(atri):
        """
        Funcionalidad: Obtiene los ingredientes del atributo.
        Entradas: El atributo.
        Salidas: El dato.
        """
        return atri.ingredientes
    
    def obtenerPrecio(atri):
        """
        Funcionalidad: Obtiene el precio del atributo.
        Entradas: El atributo.
        Salidas: El dato.
        """
        return atri.precio
    
    def obtenerTamanno(atri):
        """
        Funcionalidad: Obtiene el tamaño del atributo.
        Entradas: El atributo.
        Salidas: El dato.
        """
        return atri.tamanno
    
    def obtenerTodos(atri):
        """
        Funcionalidad: Obtiene todo del atributo.
        Entradas: El atributo.
        Salidas: El dato.
        """
        return atri.nombre,atri.ingredientes,atri.precio,atri.tamanno

class Fria(Bebida):
    #Definición atributos
    phielo=bool
    pcategoria=bool
    def __init__(atri,pcodigo,ptipo,pnombre,pingredientes,pprecio,ptamanno,phielo,pcategoria):
        atri.hielo=phielo
        atri.categoria=pcategoria
        Bebida.__init__(atri,pcodigo,ptipo,pnombre,pingredientes,pprecio,ptamanno)

    def asignarHielo(atri,phielo):
        """
        Funcionalidad: Asigna el hielo ingresado al atributo.
        Entradas: Dato ingresado.
        Salidas: El atributo con el dato.
        """
        atri.phielo=phielo

    def asignarCategoria(atri,pcategoria):
        """
        Funcionalidad: Asigna la categoría ingresada al atributo.
        Entradas: Dato ingresado.
        Salidas: El atributo con el dato.
        """
        atri.pcategoria=pcategoria

    def obtenerHielo(atri):
        """
        Funcionalidad: Obtiene el hielo del atributo.
        Entradas: El atributo.
        Salidas: El dato.
        """
        return atri.hielo
    
    def obtenerCategoria(atri):
        """
        Funcionalidad: Obtiene la categoría del atributo.
        Entradas: El atributo.
        Salidas: El dato.
        """
        return atri.categoria

    def obtenerTodoFrio(atri):
        """
        Funcionalidad: Obtiene todo del atributo.
        Entradas: El atributo.
        Salidas: El dato.
        """
        return Bebida.obtenerTodo(atri),atri.hielo,atri.categoria

class Caliente(Bebida):
    #Definición atributos
    tipoCaliente=int
    def __init__(atri,pcodigo,ptipo,pnombre,pingredientes,pprecio,ptamanno,ptipoCaliente):
        atri.tipoCaliente=ptipoCaliente
        Bebida.__init__(atri,pcodigo,ptipo,pnombre,pingredientes,pprecio,ptamanno)

    def asignarTipoCaliente(atri,ptipoCaliente):
        """
        Funcionalidad: Asigna el tipo de bebida caliente ingresado al atributo.
        Entradas: Dato ingresado.
        Salidas: El atributo con el dato.
        """
        atri.tipoCaliente=ptipoCaliente
            
    def obtenerTipoCaliente(atri):
        """
        Funcionalidad: Obtiene el tipo de bebida caliente ingresado al atributo.
        Entradas: Dato ingresado.
        Salidas: El atributo con el dato.
        """
        return atri.tipoCaliente

    
        
            
