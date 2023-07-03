################################################################
# Ejemplo de comunicación bloqueada al mismo valor compartido
################################################################
from multiprocessing import Process, Value, Lock
import time

def add100(num,cand):
    for i in range(100):
        time.sleep(0.01)
        # Poner el candado
        cand.acquire()
        # Hacer la operación
        num.value +=1
        # Quitar candado para liberarse de las cadenas opresosras del sistema :3
        cand.release()

if __name__=="__main__":

    #Candado para evitar que dos procesos se empalmen
    cand = Lock()
    ##############################################################
    #Número común a los procesos, i de entero, comienza siendo 0
    # Value es un objeto de un número compartido
    ##############################################################
    numComp= Value('i',0)
    print("Al principio vale= ", numComp.value)
    p1= Process(target=add100, args=(numComp,cand))
    p2= Process(target=add100, args=(numComp,cand))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Al final vale= ", numComp.value)

