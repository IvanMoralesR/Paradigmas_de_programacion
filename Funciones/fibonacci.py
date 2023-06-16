##############################
#Herramietas para memoización
##############################

from functools import lru_cache

def fSlow(n):
    if n==1:
        return 1
    if n==2:
        return 1
    if n>2:
        return fSlow(n-1) + fSlow(n-2)
for i in range (1,36):
    print (str(i) + ":", fSlow(i))

########################################################
# Optimización 2: uso de conjuntos para guardar valores
#######################################################

######################
#cojunto de fibo UwU
######################

fibonaccis={}
def fibo(n):
    #########################################
    # Revisa si ya existe y regresa el valor
    #########################################
    if n in fibonaccis:
        return fibonaccis[n]

    if n==1:
        valor = 1
    elif n==2:
        valor = 1
    elif n>2:
        valor = fibo(n-1) + fibo(n-2)

    ###########
    #Guárdalo
    ###########

    fibonaccis[n] = valor
    return valor
for i in range (1,10001):
    print(str(i) + ":", fibo(i))

########################################
# Uso de decoradoree para memoizacion
# maxsize: es cuantos anteriores guarda
########################################
@lru_cache(maxsize = 3)
def nfibo(n):
    if type(n) != int:
        raise TypeError("n debe ser entero positivo")
    if n<1:
        raise ValueError("n debe ser positivo")
    if n==1:
        return 1
    elif n==2:
        return 1
    elif n>2:
        return nfibo(n-1) + nfibo(n-2)
for i in range(1,10001):
    print(str(i) + ":", nfibo(i))


            
