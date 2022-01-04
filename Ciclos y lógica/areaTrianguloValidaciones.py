########################################################################
# Elaborado por: Mónica Alfaro P
# Fecha de creación: 11/03/2020 12:40pm
# Fecha de última modificación: 11/03/2020 XX:XX
# Versión: 3.8.1
########################################################################

#Ejemplo de definición de una función:
#Funcionalidad: Calcular el área del triángulo.
#Entrada: base(int), altura(int)
#Salida: Área del triángulo: area(float)

def calcularArea (pbase, paltura): #responsibilidad = determinar el área
    area=(pbase*paltura)/2
    return area

def calcularAreaAux (pbase, paltura): #responsibilidad = validaciones
    if(isinstance(pbase, int) and isinstance(paltura, int)):
        if(pbase!=0)and(paltura!=0):
            print('El resultado del área es: ', calcularArea(pbase, paltura))
            return ""
        else:
            return "Los datos de entrada deben ser únicamente enteros."
        
def mostrarAlUsuario (): #responsabilidad = pedir datos y mostrar salidas al usuario
    base=int(input("Indique el valor de la base: "))
    altura=int(input("Indique el valor de la altura: "))
    print(calcularAreaAux(base,altura))
    return ""

#Programa principal
print(mostrarAlUsuario())
