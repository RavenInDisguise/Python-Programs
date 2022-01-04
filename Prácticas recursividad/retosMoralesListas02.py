def insert_d(ref, ele, lista,nuevaLista=[]):
    if lista==[]:
        return nuevaLista
    if lista[0]==ref:
        return insert_d(ref, ele, lista[1:],nuevaLista=nuevaLista+[lista[0]]+[ele])
    else:
        return insert_d(ref, ele, lista[1:],nuevaLista=nuevaLista+[lista[0]])

#print(insert_d(4, 5, [1,2,3,4,6,7,4,8]))
#print(insert_d("x", "y", ["a","b","c","x","d","e"]))

def separa(lista,contador=1,pares=[],impares=[]):
    if lista==[]:
        return [pares,impares]
    if(contador%2==0):
        pares.append(lista[0])
        return separa(lista[1:],contador+1,pares,impares)
    else:
        impares.append(lista[0])
        return separa(lista[1:],contador+1,pares,impares)

#print(separa(["a","b","c","d","e"]))

def ordenAsc(lista):
    if len(lista)==1:
        return True
    elif(lista[0]<lista[1]):
       return ordenAsc(lista[1:])
    else:
        return False
    
#print(ordenAsc([2,4,5,6,7]))
#print(ordenAsc([8,7,2,4,5]))

def alternarParesImpares(lista):
    if len(lista)==1:
        return True
    elif (lista[0]%2==0 and lista[1]%2!=0 or lista[0]%2!=0 and lista[1]%2==0):
        return alternarParesImpares(lista[1:])
    else:
        return False

#print(alternarParesImpares([1,2,3,6,5,5]))

def repetirValores(lista,num,contador=1,lista2=[]):
    if lista==[]:
        return lista2
    elif contador==num:
        return repetirValores(lista[1:],num, 1, lista2=lista2+[lista[0]])     
    else:
        return repetirValores(lista,num,contador+1, lista2=lista2+[lista[0]])

#print(repetirValores([1,3,3,7],2))

def interseccionListas(lista1,lista2,index=0,listaN=[]):
    if lista1==[]:
        return listaN
    
    if (len(lista2)==index):
        return interseccionListas(lista1[1:],lista2,0,listaN)
    
    elif(lista1[0]==lista2[index]):
         return interseccionListas(lista1[1:],lista2,index+1,listaN=listaN+[lista1[0]])

    elif(lista1[0]!=lista2[index]):
         return interseccionListas(lista1,lista2,index+1,listaN)

#print(interseccionListas([1,-3,5,2,-4,6],[1,6]))

def diferenciaListas(lista1,lista2,index=0,listaN=[]):
    if lista1==[]:
        return listaN
    
    if (len(lista2)==index):
        return diferenciaListas(lista1,lista2,0,listaN)
    
    elif(lista1[0]==lista2[index]):
         return diferenciaListas(lista1[1:],lista2,index+1,listaN)

    elif(lista1[0]!=lista2[index]):
         return diferenciaListas(lista1[1:],lista2,index+1,listaN=listaN+[lista1[0]])
    
#print(diferenciaListas([1,-3,5,2,-4,6],[1,6]))

def eliminarDuplicados(lista,index=1,nuevaLista=[]):
    if lista==[]:
        return nuevaLista
    
    if(len(lista)==index-1) or (len(lista)==index):
        return eliminarDuplicados(lista,0,nuevaLista=nuevaLista+[lista[0]])
    
    if(lista[0]==lista[index]):
        return eliminarDuplicados(lista[1:],index+1,nuevaLista)
    
    elif(lista[0]!=lista[index]):
        return eliminarDuplicados(lista,index+1,nuevaLista)

print(eliminarDuplicados([1,2,3,4,2,5,6,3,8]))
