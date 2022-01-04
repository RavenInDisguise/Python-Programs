###################################################################################
#Elaborado por Jennifer A
#Inicio 29/07/2020 12:20 pm
#Última modificación 29/07/2020
#Versión 3.8.2
###################################################################################

#Reto 1 ###########################################################################
def insert_d(ref, ele, lista,listaNueva=[]):
    if lista==[]:
        return listaNueva
    else:
        listaNueva=listaNueva+[lista[0]]
        if lista[0]==ref:
            return insert_d(ref, ele, lista[1:],listaNueva=listaNueva+[ele])
        else:
            return insert_d(ref, ele, lista[1:],listaNueva)
def reto1():
    prueba1=[("x","y",["a","b","c","x","d","e"]),(4,5,[1,2,3,4,6,7,4,8])]
    print("Reto 1 - Agregar valor luego de otro predefinido\n")
    for prueba in prueba1:
        ref=prueba[0]
        ele=prueba[1]
        lista=prueba[2]
        print(prueba)
        print(str(insert_d(ref,ele,lista))+"\n")
reto1()
#Reto 2 ###########################################################################
def alternarParesImpares(lista):
    if len(lista)==1:
        return True
    elif (lista[0]%2==0 and lista[1]%2!=0 or lista[0]%2!=0 and lista[1]%2==0):
        return alternarParesImpares(lista[1:])
    else:
        return False

def reto2():
    prueba1=[[2,5,8,7,10],[1,2,3,4,6],[1,2,3,4,5]]
    print("Reto 2 - Verificar si los elementos se alternan entre pares e impares\n")
    for prueba in prueba1:
        print(prueba)
        print(alternarParesImpares(prueba),"\n")
reto2()
#Reto 3 ###########################################################################
def separar(lista,index=0,listaNueva=[[],[]]):
    if len(lista)==index:
        return listaNueva
    else:
        elemento=lista[index]
        if index%2==0:
            listaNueva[1]=listaNueva[1]+[elemento]
        else:
            listaNueva[0]=listaNueva[0]+[elemento]
        return separar(lista,index+1,listaNueva)
def reto3():
    lista3=["a","b","c","d","e"]
    print("Reto 3 -  Separar indices pares e impares\n")
    print(lista3)
    print(str(separar(lista3))+"\n")
reto3()
#Reto 4 ###########################################################################
def repetirValores(lista,num,contador=1,lista2=[]):
    if lista==[]:
        return lista2
    elif contador==num:
        return repetirValores(lista[1:],num, 1, lista2=lista2+[lista[0]])     
    else:
        return repetirValores(lista,num,contador+1, lista2=lista2+[lista[0]])

def reto4():
    prueba1=[([1,3,3,7],2)]
    print("Reto 4 - Duplicar valores de una lista según un número\n")
    for prueba in prueba1:
        print(prueba)
        print(repetirValores(prueba[0],prueba[1]),"\n")
reto4()
#Reto 5 ###########################################################################
def listaAscendente(lista,var=True):
    if len(lista)==2:
        if lista[0]<lista[1]:
            var=True
        else:
            var=False
        return var
    else:
        if lista[0]<lista[1]:
            var=True
            return listaAscendente(lista[1:],var)
        else:
            var=False
            return var
def reto5():
    prueba5=[[2,4,5,6,7],[8,7,2,4,5]]
    print("Reto 5 - Lista Ascendente\n")
    for prueba in prueba5:
        print(prueba)
        print(str(listaAscendente(prueba))+"\n")
reto5()
#Reto 6 ###########################################################################
def split(lista,elemento,lista2=[],lista3=[]):
    if lista==[]:
       if lista3!=[]:
           lista2.append(lista3)
       return lista2
    if(lista[0]==elemento):
        lista2.append(lista3)
        return split(lista[1:],elemento, lista2, [])
    lista3.append(lista[0])
    return split(lista[1:],elemento,lista2,lista3)

def reto6():
    prueba1=[([],"x"),([1,4,7,"x",1,2,3],"x"),([1,4,7,"x","x",1,2,3],"x"),([1,4,7,"x","x","x",1,2,3],"x"),([1,4,7,"x","x","x",1,2,3,"x"],"x")]
    print("Reto 6 - Generar un split según un valor dado\n")
    for prueba in prueba1:
        print(prueba)
        print(split(prueba[0],prueba[1]),"\n")
#reto6()
