########################################################################
# Elaborado por: Mónica Alfaro P
# Fecha de creación: 11/03/2020 11:35am
# Fecha de última modificación: 11/03/2020 11:45am
# Versión: 3.8.1
########################################################################

#Ejemplo de definición de una función:
#Funcionalidad: Calcula el area de un triángulo
#Entrada: base(int), altura(int)
#Salida: Área del número(int)

def areaTriangulo (pbase, paltura):
    area=(pbase * paltura)/2
    return area

#Programa principal
base=int(input("Ingrese una base: "))
altura=int(input("Ingrese una altura: "))
print("El área del triángulo es: ",int(areaTriangulo (base, altura)))
