from mpi4py import MPI

zapato=MPI.COMM_WORLD
size= zapato.Get_size()
rank= zapato.Get_rank()

data = (rank+1)**2

################################################
#Maden susu datos al proceso root=0 (en order)
################################################
datas= zapato.gather(data, root=0)

################################
#Asegurarse que todo funcione
################################
if rank== 0:
    for i in range(size):
        assert datas[i] == (i+1)**2
else:
    assert datas is None
print(data)
