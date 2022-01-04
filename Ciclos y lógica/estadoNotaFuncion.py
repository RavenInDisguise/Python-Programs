########################################################################
# Elaborado por: Mónica Alfaro P
# Fecha de creación: 11/03/2020 12:20pm
# Fecha de última modificación: 11/03/2020 12:25pm
# Versión: 3.8.1
########################################################################

#Ejemplo de definición de una función:
#Funcionalidad: Calcular el estado del estuiante de acuerdo a su nota.
#Entrada: int(pnota).
#Salida: Su estado: "Reprobado" o "Aprobado".
def estadoNota(pnota):
    if(pnota>=8):
        print("Aprobado")
        return
    else:
        print("Reprobado")
        return

#Programa principal
nota=int(input("Ingrese su nota: "))
estadoNota(nota)
