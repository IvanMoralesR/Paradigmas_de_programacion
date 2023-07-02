from multiprocessing import Process 
import os
import math
import time

def calc():
    for i in range(0, 4000000):
        math.sqrt(i)

procesos = []
cpus= os.cpu_count()

print("Núcleos en tu CPU ", cpus)
for i in range(cpus):
    print("registranso el proceso %d" % i)
    procesos.append(Process(target=calc))

start= time.time()

for proceso in procesos:
    proceso.start()     #inicializa los procesos
for proceso in procesos:
    proceso.join()     #no olvidar el start

end= time.time()
print("Se tardó: ", end-start)
