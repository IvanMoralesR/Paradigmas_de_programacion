######################################
#mpirun -n 4 python3 tareas mpi.py
######################################
from mpi4py import MPI

#########################
#Objeto de comunicadores
#########################
comm = MPI.COMM_WORLD

########################
#Cuántos somos en total
########################

size = comm.Get_size()

###########
#Quén soy
##########

rank= comm.Get_rank()

#############################
#Si yo soy el cero hago esto
#############################
if rank == 0:
    print("Yo soy el proceso 0")

################################
#si soy el proceso 1 hago esto
################################

elif rank == 1:
    print("yo soy el proceso 1")

##############################################
#si yo no soy ni el uno ni el dos hago esto 
##############################################
else:
    print("yo no soy ninguno de los primeros 2 procesos")

print("Repotándome, soy el proceso ", str(rank), " de ", str(size), " UwU")
