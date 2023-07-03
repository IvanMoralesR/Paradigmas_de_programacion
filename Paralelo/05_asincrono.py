import multiprocessing as mp
import numpy as np
import time

def my_function(i, param1, param2, param3):
    
    # calcula un polinomio
    result = param1**2 + param2 + param3
    time.sleep(2) #se hace tonta 2 segundos
    return (i,result)

def  get_result(result):
    # se inscriben en la lista global
    # (mal estilo de programaión)
    global results
    results.append(result)

#####################
# Programa principal
#####################
if __name__=="__main__":

    # Matriz 10x3 números al azar
    params = np.random.random((10,3))*100.0
    results = []
    ts= time.time()

    # un grupo de procesos (pool)
    pool = mp.Pool(mp.cpu_count())

    #loop de promerra dimesión del arreglo
    for i in range(0, params.shape[0]):
    #Correr asincrónamente My_functions con argumentos args y cuando termine correr get_resul
        pool.apply_async(my_function, args = (i, params[i, 0], params[i, 1], params[i, 2]), callback = get_result)

    #cerar el grupo
    pool.close()

    #Esperar a que termine el grupo
    pool.join()

    print("tiempo en paralelo = ", time.time() - ts)
    print(results)

