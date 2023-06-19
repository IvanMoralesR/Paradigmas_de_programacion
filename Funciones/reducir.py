###############################################
#Uso de reducciones (colapsar resultados)
###############################################

################################################
#Multiplicaión de todos ls números de la lista
################################################

from functools import reduce

bigdata = [2,3,5,7,11,13,17,19,23,29]

#############
#Función x*y
#############

multiplicar = lambda x,y: x*y

print(reduce(multiplicar,bigdata))

##########################################################
#Reduce le aplia a la función por pare a los resultados y 
#el siguiente elemenro comenzando con los dos primeros 
#elementos.
##########################################################


