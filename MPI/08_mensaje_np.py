from mpi4py import MPI
import numpy as uwu

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

#############################################
# Se indica el tipo de datos explicitamente 
#############################################

##########################
# EJEMPLO 1 USANDO ENTEROS
###########################
if rank == 0:
     ###############################
     #arreglo de enteros de 0 al 9
     ##############################
     data = uwu.arange(10, dtype='i')
     ################################################
     # Envío bloqueante especificando el tipo de dato
     #################################################
     comm.Send([data, MPI.INT], dest=1, tag=77)

elif rank== 1:
    data= uwu.empty(10, dtype='i')
    comm.Recv([data,MPI.INT], source=0, tag=77)
    print(data)

########################################################################################
#Tambien se puede sin decir el tipo de dato pero se deben coincidir el tipo de arreglos
#a los extremos del mensaje
#######################################################################################

#################################
#Ejemplo 2 usando flotantes
#################################

if rank == 0:
    data= uwu.arange(10, dtype= uwu.float64)
    comm.Send(data, dest=1, tag=13)
elif rank == 1:
    data = uwu.empty(10, dtype=uwu.float64)
    comm.Recv(data, source=0, tag= 13)
    print(data)
