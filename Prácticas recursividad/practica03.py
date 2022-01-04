def multiplosDigitos(num,dig):
    if num==0:
        return 0
    elif(num%10%dig==0):
       return num%10 + multiplosDigitos(num//10,dig)
    else:
        return multiplosDigitos(num//10,dig)

#print(multiplosDigitos(666,3))

def formarNumPar(num):
    if num==0:
        return 0
    elif((num%10)%2==0):
        return 10*formarNumPar(num//10)+num%10
    else:
        return formarNumPar(num//10)    

#print(formarNumPar(2552180))

    
def formarNumPar2(num,num2=0,exp=0):
    if num==0:
        return num2
    elif((num%10)%2==0):
        num2=num2+(num%10 * 10 ** exp)
        return formarNumPar2(num//10, num2, exp+1) 
    else:
        return formarNumPar2(num//10, num2, exp)    

print(formarNumPar2(2552180))


def encontrarNumMenor(num,menor=9):
    if num==0:
        return menor
    elif(menor>num%10):
        return encontrarNumMenor(num//10,num%10)
    else:
        return encontrarNumMenor(num//10,menor)

print(encontrarNumMenor(999))


