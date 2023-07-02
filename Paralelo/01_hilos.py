
from threading import Thread as owo
import os
import math
import time

def calc():
    for i in range(0,4000000):
        math.sqrt(i)

threads = []
cpus = os.cpu_count() #numero de nucleo del procesador
print("Núcleos en tu CPU, ", cpus)
for i in range (cpus):
    print("registrando el hilo %d " % i)
    threads.append(owo(target=calc))

start = time.time()

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

end= time.time()

print("se tardó: ",end-start)

