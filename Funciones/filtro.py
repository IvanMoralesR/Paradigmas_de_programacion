#################
#uso de filtros
#################

########################################################
#hacer una lista de los números por arriba del promedio
########################################################

#Modulo de estadística
import statistics as stat

bigdata = [1.3,2.7,0.8,4.1,4.3,-0.1]
prom= stat.mean(bigdata)
print(prom)

#########################################################################
#Hazme una ista de elementos que cumplan la condición x > promedio
#filter(condición,datos)
#########################################################################
print(list(filter(lambda x : x> prom, bigdata)))

###################
#Limpiar los datos
###################

paises = ["","Argentina","","Chile","","Brasil","México","","Colombia","","","Cuba"]

###################################
#Filtrar lo que no contiene nada
###################################
print(list(filter(None,paises)))
