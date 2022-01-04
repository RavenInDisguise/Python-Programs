#Elaborado por: Mónica Alfaro
#Fecha de creación: 29/04/20 10:50am
#Última modificación: 29/04/20 14:20pm
#Versión: 3.8.2

######################################################################################################################################################


#Función promedioLluvias:
"""
    Funcionalidad: Calcular el promedio de lluvias de la región Centro, mes con menor lluvia de la región Sur, registro del mes y promedio general.
    Entradas: float(RNO), float(RCE), float(RSU). Cantidad de lluvia por mes en la región Norte, Central y Sur, respectivamente.
    Salidas: int(PRORCE), int(MES), int(MERSU). Promedio general, promedio de lluvias de la región Centro, mes con menor lluvia de la región Sur y registro del mes, respectivamente.
"""
def promedioLluvias():
    i = 1
    ARSU = 0
    ARNO = 0
    MERSU = 500000
    ARCE = 0 
    while (i <= 12):
            print('\n')
            print("Mes",i,":")
            
           #Validación de datos:
            try:
                RNO=float(input("Por favor, inserte la cantidad de lluvia caida en la región Norte durante el mes: "))
                RCE=float(input("Por favor, inserte la cantidad de lluvia caida en la región Central durante el mes: "))
                RSU=float(input("Por favor, inserte la cantidad de lluvia caida en la región Sur durante el mes: "))

            except ValueError:
                print("Ingrese un número, por favor.")
                return
                

            ARNO = ARNO + RNO
            ARCE = ARCE + RCE
            ARSU = ARSU + RSU

            if(RSU < MERSU):
                MERSU= RSU
                MES = i
            else:
                    ""
            i=i+1
    else:
        PRORCE = ARCE/12
        impresionDatos(PRORCE, MES, MERSU)
        regionMayor(ARNO, ARCE, ARSU)
    return 

#Función impresionDatos:       
"""
    Funcionalidad: Imprimir los datos metereológicos recopilados en la función promedioLluvias.
    Entradas: int(PRORCEN, int(MES1), int(MERSUR).
    Salidas: Impresión de los datos.
"""    
def impresionDatos (PRORCEN,MES1, MERSUR):
    print('\n')
    print("Datos metereológicos de las regiones:  \n")
    print("Promedio región Centro: ", PRORCEN)
    print("Mes con menor lluvia en la región Sur: ", MES1)
    print("Registro menor del mes",MES1,"en la región Sur:", MERSUR)
    return

#Función regionMayor:       
"""
    Funcionalidad: Calcular la región con mayor cantidad de lluvia.
    Entradas: int(ARNOR), int(ARCEN), int(ARSUS). Cantidad de lluvia en promedio en la región Norte, Central y Sur, respectivamente.
    Salidas: La región con mayor cantidad de lluvias.
"""
def regionMayor(ARNOR, ARCEN, ARSUR):
    if(ARNOR > ARCEN):
        if(ARNOR > ARSUR):
            print("La región con mayor lluvia es la región Norte.")
        else: print("La región con mayor lluvia es la región Sur.")
    else: 
        if(ARCEN > ARSUR):
            print("La región con mayor lluvia es la región Centro.")
        else: 
            print("La región con mayor lluvia es la región Sur.")
    return

#Programa principal
print("Bienvenido al programa para calcular datos sobre las lluvias en las tres regiones principales de Argentina:")
promedioLluvias()

