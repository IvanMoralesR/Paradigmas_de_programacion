#Ejemplo de comunicaión bloqueada a una misma variable compartida

from multiprocessing import Process, Value, Lock
import time

def sm100(num, cand):
    for i in range(100):
        time.sleep(0.01)
        #Usando candado para que no se lo roben
        with cand:
            # Hacer la operación
            num.value += 1

if __name__=="__main__":

    # Candado para evitar que dos procesos se empalmen
    cand = Lock()
    # Número común a los procesos, i de entero, comienza siendo 0
    numComp= Value('i', 0)
    print("Al principio vale= ", numComp.value)

    #Dos procesos
    p1 = Process(target=sm100, args=(numComp,cand))
    p2 = Process(target=sm100, args=(numComp,cand))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Al final vale ", numComp.value)

