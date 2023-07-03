#############################################################
# Ejemplo de comunicación bloqueda a un arregllo compartido
# Uso de candados (locks)
#############################################################

from multiprocessing import Process, Array, Lock
import time

def sm100(nums, cand):
    for i in range(100):
        time.sleep(0.01)
        #Usando candado
        for i in range(len(nums)):
            # no se puede acceder a lo que está dentro del candado desde otro proceso
            # al mimo tiempo

            with cand:
                # Hacer la operación 
                nums[i] +=1

if __name__ == "__main__":
    ############################################################
    #El candado es para evitar que los procesos se empalmen OwO
    ############################################################
    cand = Lock()

    #Número común de procesos d de dobles
    numsComp= Array('d',[0.0, 100.0, 200.0])

    # ":" quiere decir todos los elementos
    print("Al principio vale= ", numsComp[:])

    #Dos procesos
    p1 = Process(target=sm100, args=(numsComp,cand))
    p2 = Process(target=sm100, args=(numsComp,cand))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Al final vale= ", numsComp[:])


