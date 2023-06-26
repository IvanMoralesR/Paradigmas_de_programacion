#forma compacta de random_nb

import numpy as np
from mpi4py import MPI
comm= MPI.COMM_WORLD
rank= comm.Get_rank()

randNum = np.zeros(1)

if rank == 1:
    dst= 0
    src= 0
if rank == 0:
    dst= 1
    src =1
randNum= np.random.random.random_sample(1)
print("Process", rank, "drew the number", randNum[0])
comm.Isend(randNum, dest=dst)
req= comm.Ircv(randNum, source=src)
req.Wait()
print("Process", rank, "recived the number", ranNum[0])
