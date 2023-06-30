from mpi4py import MPI
import math as ewe

waka=MPI.COMM_WORLD
size= waka.Get_size()
rank= waka.Get_rank()

n=40
x=range(n)
m=int(ewe.ceil(float(len(x))/size))
x_chunk= list(x[rank*m:(rank+1)*m])
r_chunk= list(map(ewe.sqrt, x_chunk))

#####################################
#Una sola lista de rodos los datos
####################################
r= waka.allreduce(r_chunk)

##############################
#Una matíz con odos los datos
##############################
rr= waka.allgather(r_chunk)

###################################
#Una matriz con todos los datos
###################################
rrr= waka.gather(r_chunk,root=1)

if rank==0:
    print(r)
    print(rr)
    print(rrr)
if rank==1:
    print(rrr)


