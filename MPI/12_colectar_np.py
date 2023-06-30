from mpi4py import MPI
import numpy as owo

wa=MPI.COMM_WORLD
size= wa.Get_size()
rank= wa.Get_rank()

n=10

##########################################
#Arreglo de ceros tamaño n
#sumando con un escalar (en cada entrada)
##########################################
sendarray= owo.zeros(n,dtype='i')+rank

recvarray= None

if rank==0:
    #######################################
    #Mátriz vacia de tamaño d procesos *n
    #dtype es el tipo de ta (i es entero)
    ######################################
    recvarray = owo.empty([size, n], dtype='i')

#############################
#Gather es rápido para numpy
#enviar datos al proceso root
##############################
wa.Gather(sendarray,recvarray,root=0)

if rank == 0:
    for i in range(size):
        #########################################################
        #Revisar por fila la matriz
        #: signica que todos los elemenos de esa dimensión
        #allclose es un método de numpy que compara elementos
        #########################################################
        assert owo.allclose(recvarray[i,:],i)
print(recvarray)
