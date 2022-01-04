#Tarea moral recursividad:

#Fibonacci: Ejemplo por linuxhispano.net

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

   
print('Fibonacci de orden 10:',fib(10))
   
#Sumatoria recursiva

def sumatoriaRec(num):
    if num==0:
        return 0
    else:
        return num%10 + sumatoriaRec(num-1)

print("La sumatoria del número es: ",sumatoriaRec(3))

#Sumatoria recursiva de un intervalo

def sumatoriaRec(num,num2):
    if num==num2:
        return 0
    else:
        return num%10 + sumatoriaRec(num+1,num2)

print("La sumatoria del número con intervalo es: ",sumatoriaRec(0,7))
