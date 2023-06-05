#curvaZ conbre del archivo de la clase

##########################################
# Curva Z-splines en n dimensiones
##########################################
# Julian Sagredo ESFM IPN 2023
##########################################
import numpy as np
from curvaZ import Curva,zspline
import matplotlib.pyplot as plt
import math

######################
# Conjunto de puntos 
######################
#Numero de punto
nump:np.int32=8
#Dimensión
dim:np.int32=2
#Memoria para puntos
puntos=  np.zeros(dim*nump,dtype=np.float64)
#Parametrización
x= np.linespace(0.0,2*np.pi,nump+1)
