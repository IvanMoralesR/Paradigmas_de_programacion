
from mpi4py import MPI
import numpy as ewe
comm= MPI.COMM_WORLD
rank= comm.Get_rank()

#Tamaño del arreglo
n=10
if rank ==0:
    #Arreglo de enteros del 0 al n-1
    data= ewe.arange(n, dtype='i')
else:
    #Arreglo vacío de enteros de tamaño n
    data= ewe.empty(n, dtype='i')

#########################################
#Broadcast pro que indca el tipo de dato 
#Optimizado para comunicaión rápida
#########################################
comm.Bcast([data,MPI.INT], root=0)

#################################
#Asegurarse que toso salío bien
#################################

for i in range(n):
    assert data[i]==i
print(data)
