##################################
#pROGRAMACION oRIENTADA A OBJETOS#
##################################

################################
#Una clase para un objeto vacio#
#No está tan vacia, necesita   #
#la palabra pass=pasar         #
################################

class ObjetoVacio:
    pass

#########################
#nada es un objeto vacio#
#########################

nada= ObjetoVacio()
print(type(nada))

#######################
#Poderosa clase Llanta#
#######################

class Llanta:
    cuenta=0 #variable cuenta es de toda la clase
    ###################################
    #Función condtructora de identidad#
    #__init__ es una función reservada#
    #comienza con un mismo: self      #
    #pero puede ser otro nombre (mi)  #
    #parámetros de entrada= default   #
    ###################################

    def __init__(mi,radio=50,ancho=30,presión=1.5): #valores default
        #variable de la estructura completa llanta
        Llanta.cuenta +=1
        #variables exclusivas de cada objeto
        mi.radio=radio
        mi.ancho=ancho
        mi.presión=presión

########################
#Objetos (instanciados)#
########################

llanta1= Llanta(50,30,1.5)
llanta2= Llanta(presión=1.2)
llanta3= Llanta(40,30,1.6)

###################################
#Objeto que contiene otros objetos#
###################################

class Coche:
    def __init__ (mi,ll1,ll2,ll3,ll4):
        mi.llanta1=ll1
        mi.llanta2=ll2
        mi.llanta3=ll3
        mi.llanta4=ll4

tsurito= Coche(llanta1,llanta2,llanta3,llanta4)

print("Total de llantas: ", Llanta.cuenta) #variable global de la clase
print("Presión de la llanta 4= ", llanta4.presión)
print("Radio de la llanra 4= ", llanta4.radio)
print("Radio llanta 30", llanta3.radio)
print("Presión de llanta1 del tsurito",tsurito.llanata1.presión)
