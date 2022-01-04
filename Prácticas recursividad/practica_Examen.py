def generarBinario(num,valor=""):
    if num==0:
        return valor
    elif(num%2==0):
        return generarBinario(num//2,valor=str(0)+valor)
    else:
        return generarBinario(num//2,valor=str(1)+valor)
        
print(generarBinario(113))

def generarMultiplicacion(num):
    if num==0:
        return 1
    else:
        return num%10 * generarMultiplicacion(num//10)

print(generarMultiplicacion(628))

def voltearNumero(num, valor=0):
    if num==0:
        return valor
    else:
        return voltearNumero(num//10,valor=valor*10+num%10)

print(voltearNumero(5678))

def posicionPar(num, posicion, contador=1):
    if contador==posicion:
        if((num%10)%2==0):
            return True
        else:
            return False
    else:
        return posicionPar(num//10, posicion, contador+1)

print(posicionPar(92553,4))

def sumarValores(num2,num=0):
    if num>num2:
        return 0
    else:
        return (num+sumarValores(num2,num+1))

print(sumarValores(1000))
        
#Notas:

##def invertir():
##    a=int(input("Ingresar un Número: "))
##    x=0
##    y=(a%10==0)  #Aquí le damos el valor a la variable "y", True, o False, si el N° termina en 0.
##    z=len(str(a))
##    for i in range(z):
##        b=a%10
##        a=a//10
##        x=x*10+b 
##    if y:
##        x=str(x)
##        x='0'+x
##    return x
##
##print(invertir())

##10*formarParesRec(num//10))+num%10

