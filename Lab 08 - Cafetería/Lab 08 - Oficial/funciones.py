##########################################################################
#Elaborado por: Mónica Alfaro Parrales y Jennifer Alvarado Brenes
#Inicio: 22/07/2020 12:10 pm
#Última modificación: 22/07/2020 22:00 pm
#Versión 3.8.2
##########################################################################

#Importación de librerías:

from clasesBebida import *

##########################################################################

#Funciones 

def generarListaIngr(pingredientes):
    """
    Funcionalidad: Generar una lista con los ingredientes escritos.
    Entradas: Los ingredientes str(pingredientes).
    Salidas: La lista de los ingredientes list(ingredientesLista).
    """
    ingredientesLista=[]
    if("," in pingredientes):
        ingredientesLista=pingredientes.split(",")
    else:
        ingredientesLista=[pingredientes]
    return ingredientesLista

def reconocerTipo(pcodigo):
    """
    Funcionalidad: Reconocer el tipo de bebida.
    Entradas: El código str(pcodigo).
    Salidas: 1/2
    """
    if(pcodigo[0]=="f"):
        return 1
    else:
        return 2
    
def generarTipoCal(tipoCal):
    """
    Funcionalidad: Generar el tipo de bebida caliente.
    Entradas: El tipo de bebida caliente int(tipoCal).
    Salidas: Chocolate/Té/Café/Aguadulce.
    """
    if(tipoCal==1):
        return "Chocolate"
    elif(tipoCal==2):
        return "Té"
    elif(tipoCal==3):
        return "Café"
    else:
        return "Aguadulce"

def generarBool2(pcategoria):
    """
    Funcionalidad: Generar un booleano según los datos ingresados por el usuario (1 o 2).
    Entradas: La categoria str(pcategoria).
    Salidas: True/False.
    """
    if(pcategoria=="1"):
        return True
    else:
        return False
    
def generarBool(phielo):
    """
    Funcionalidad: Generar un booleano según los datos ingresados por el usuario (sí o no).
    Entradas: El dato del hielo str(hielo).
    Salidas: True/False.
    """
    if(phielo.lower()=="sí" or phielo.lower()=="si"):
        return True
    else:
        return False

def generarSiNo(phielo):
    """
    Funcionalidad: Generar el dato sí o no, según un booleano.
    Entradas: El hielo bool(phielo).
    Salidas: Sí/No
    """
    if(phielo==True):
        return "Sí"
    else:
        return "No"
    
def generarTamanno(tamanno):
    """
    Funcionalidad: Generar el str "Pequeño", "Mediano" o "Grande", sgeún un int.
    Entradas: El tamaño (int).
    Salidas: "Pequeño", "Mediano" o "Grande".
    """
    if(tamanno==1):
        return "Pequeño"
    elif(tamanno==2):
        return "Mediano"
    else:
        return "Grande"

def generarCategoria(categoria):
    """
    Funcionalidad: Generar los valores de categoria según un bool.
    Entradas: La categoria bool(categoria).
    Salidas: Natural/Gaseosa.
    """
    if(categoria==True):
        return "Natural"
    else:
        return "Gaseosa"

def borrarBebida(lista,pcodigo):
    """
    Funcionalidad: Borrar una bebida según el código.
    Entradas: La lista list(lista) y el código str(pcodigo).
    Salidas: La bebida eliminada.
    """
    for bebida in lista:
        if(bebida.obtenerCodigo()==pcodigo):
            lista=lista.remove(bebida)
            print("Bebida exitosamente eliminada.")
            return 
        
def cambiarPrecio(listaBebida,codigo,precio):
    """
    Funcionalidad: Buscar el código en la lista y cambiarle el precio.
    Entradas: Lista, código y precio nuevo.
    Salidas: Lista con el precio cambiado en el código especificado.
    """
    for bebida in listaBebida:
        if bebida.obtenerCodigo()==codigo:
            bebida.asignarPrecio(precio)
    return 

def mostrarTodaBebida(lista):
    """
    Funcionalidad: Mostrar todas las bebidas.
    Entradas: La lista de objetos list(lista).
    Salidas: Los datos de las bebidas calientes.
    """
    if(lista==[]):
        print("No hay bebidas registradas.")
        return
    for bebida in lista:
        ingrediente2=""
        codBeb=bebida.obtenerCodigo()
        print("\n☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕")
        print("\nCódigo: "+str(bebida.obtenerCodigo()))
        print("Nombre: "+str(bebida.obtenerNombre()))
        ingredientes=bebida.obtenerIngredientes()
        print("Ingredientes:")
        for ingrediente in ingredientes:
            ingrediente2=ingrediente.strip()
            ingrediente2=ingrediente2.capitalize()
            print("*"+ingrediente2)
        print("Precio en colones: "+str(bebida.obtenerPrecio()))
        tamanno=bebida.obtenerTamanno()
        tamanno=generarTamanno(tamanno)
        print("Tamaño: ",tamanno)
        if(reconocerTipo(codBeb)==1):
            hielo=bebida.obtenerHielo()
            hielo=generarSiNo(hielo)
            print("Hielo:",hielo)
            categoria=bebida.obtenerCategoria()
            categoria=generarCategoria(categoria)
            print("Categoría: "+categoria)
        else:
            tipoCal=bebida.obtenerTipoCaliente()
            tipoCal=generarTipoCal(tipoCal)
            print("Tipo:",tipoCal)  
    return

def mostrarBebCaliente(lista):
    """
    Funcionalidad: Mostrar las bebidas calientes.
    Entradas: La lista de objetos list(lista).
    Salidas: Los datos de las bebidas calientes.
    """
    contador=0
    if(lista==[]):
        print("No hay bebidas registradas.")
        return
    for bebida in lista:
        codBeb=bebida.obtenerCodigo()
        if(reconocerTipo(codBeb)==2):
            codBeb=bebida.obtenerCodigo()
            print("\n☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕")
            print("\nCódigo: "+str(bebida.obtenerCodigo()))
            print("Nombre: "+str(bebida.obtenerNombre()))
            ingredientes=(bebida.obtenerIngredientes())
            print("Ingredientes:")
            for ingrediente in ingredientes:
                ingrediente2=ingrediente.strip()
                ingrediente2=ingrediente2.capitalize()
                print("*"+ingrediente2)
            print("Precio en colones: "+str(bebida.obtenerPrecio()))
            tamanno=bebida.obtenerTamanno()
            tamanno=generarTamanno(tamanno)
            print("Tamaño: ",tamanno)
            tipoCal=bebida.obtenerTipoCaliente()
            tipoCal=generarTipoCal(tipoCal)
            print("Tipo:",tipoCal)
            contador+=1
    if(contador==0):
        print("No hay bebidas calientes registradas.")
    return

def mostrarBebFria(lista):
    """
    Funcionalidad: Mostrar las bebidas frías.
    Entradas: La lista de objetos list(lista).
    Salidas: Los datos de las bebidas frías.
    """
    contador=0
    if(lista==[]):
        print("No hay bebidas registradas.")
        return
    for bebida in lista:
        codBeb=bebida.obtenerCodigo()
        if(reconocerTipo(codBeb)==1):
            codBeb=bebida.obtenerCodigo()
            print("\n☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕")
            print("\nCódigo: "+str(bebida.obtenerCodigo()))
            print("Nombre: "+str(bebida.obtenerNombre()))
            ingredientes=(bebida.obtenerIngredientes())
            print("Ingredientes:")
            for ingrediente in ingredientes:
                ingrediente2=ingrediente.strip()
                ingrediente2=ingrediente2.capitalize()
                print("*"+ingrediente2)
            print("Precio en colones: "+str(bebida.obtenerPrecio()))
            tamanno=bebida.obtenerTamanno()
            tamanno=generarTamanno(tamanno)
            print("Tamaño: ",tamanno)
            hielo=bebida.obtenerHielo()
            hielo=generarSiNo(hielo)
            print("Hielo: ",hielo)
            categoria=bebida.obtenerCategoria()
            categoria=generarCategoria(categoria)
            print("Categoría: ",categoria)
            contador+=1
    if(contador==0):
        print("No hay bebidas frías registradas.")
    return

def mostrarBebCafe(lista):
    """
    Funcionalidad: Mostrar los datos de las bebidas que son cafés.
    Entradas: La lista de objetos list(lista).
    Salidas: Los datos del café.
    """
    contador=0
    if(lista==[]):
        print("No hay bebidas registradas.")
        return
    for bebida in lista:
        codBeb=bebida.obtenerCodigo()
        if(reconocerTipo(codBeb)==2):
            codBebCal=bebida.obtenerTipoCaliente()
            if(codBebCal==3):
                print("\n☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕")
                print("\nCódigo: "+str(bebida.obtenerCodigo()))
                print("Nombre: "+str(bebida.obtenerNombre()))
                ingredientes=bebida.obtenerIngredientes()
                print("Ingredientes:")
                for ingrediente in ingredientes:
                    ingrediente2=ingrediente.strip()
                    ingrediente2=ingrediente2.capitalize()
                    print("*"+ingrediente2)
                print("Precio en colones: "+str(bebida.obtenerPrecio()))
                tamanno=bebida.obtenerTamanno()
                tamanno=generarTamanno(tamanno)
                print("Tamaño: ",tamanno)
                contador+=1
    if(contador==0):
        print("No hay cafés registrados.")
    return
            
                
            


