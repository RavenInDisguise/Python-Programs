# Elaborado por: Mónica Alfaro P
# Fecha de creación: 06/03/2020 10:10am
# Fecha de última modificación: 06/03/2020 10:20am
# Versión: 3.7.4

# Algoritmo que calcula el anno de nacimiento
nombre=(input("¿Cuál es su nombre?: ")) #Entradas
apellido=(input(nombre+ ", ¿cuál es su apellido?: ")) #Entradas
edad=int(input(nombre+ " "+apellido+", ¿cuál es su edad?: ")) #Entradas
for i in range(1,edad+1):
    print("Voy por ",i)
inicio=2020
anno=inicio-edad #Proceso

while inicio>=anno:
    print(inicio)
    inicio-=1
print(nombre+ " "+apellido+" "+"usted nació en: ",anno) #Salida
if anno>=2000:
    print("Usted nació en este siglo.")
else:
    print("Usted es del siglo pasado.")

