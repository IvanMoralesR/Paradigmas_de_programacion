################################################
# Cálcualo de curva Z-spline en n dimeciones
################################################
#Ivan plagiando a sagredo \(^_^)/
################################################

import numpy as np

################
# Clase curva
################

class curva:
    
    """==================================================
       Curva contruye la curva que pasa por los puntos x
       ==================================================
       Praámetros: x coordenadas ordenadas ((x1),(X2),...)
                   F Propiedades (f1(x),f2(x),...)
                   dim dimenciones
       ==================================================
    """
    #////////////
    #Constructor
    #///////////
    def __init__(s,x:xfloat=[], dim:int= 3):
