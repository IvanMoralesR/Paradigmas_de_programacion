'''
COMENTARIO ACA LARGO, PARA ESO SIRVEN
lAS 3 COMILLAS
'''
#####################
#OPERACIONES BASICAS#
#####################
print (2+3) #print imprime
print (2*3)
print (2/3)
print (2**10) #n**m n elevado a la m potencia
print(2**0.5) #raíz cuadrada
print(10%2) #modulo o residuo
print(10%0.1) #exclusivo de python

##########################################
#Para saber el tipo de objeto se usa type#
##########################################
t=0
print(type(t)) #entero
t=3.6
print(type(t))
t=True
print(type(t))

######################
# Mensaje en pantalla#
######################
print("Este es un comando de python","Este es otro",t) #comas separan weas de python
print('id:','1')
print('First Name')
print('Last Name','Jobs')
print('vamos a sumar esto'+' con esto otro')

###########################################
#Continuar instrucción en variod renglones#
###########################################
if 100>99 and \
        200<= 300 and\
        True!=False:
            print('Hello World')

#######################################
#Comandos diferentes en la misma liena#
#######################################
print("Hola "); print ("tu!!!") # se considera mala practica

##############################################
#Usando préntesis redondos cuadrados o llaves#
#se puede escribir en varios renglones       #
##############################################

list = [1, 2, 3, 4,
        5, 7, 8, 9,
        10, 11,12]

matriz = [[1,2,3,4],[5,6,7,8,],[9,10,11,12] ]

print(list)
print(matriz)

##############################################################
#Indentación escrita para procesos dependientes de : (puntos)#
##############################################################

if 10>5:
    print("diez es mayor que cinco")
    print("otra indentación")
for i in list:
    print (i)
    print("ok")
if 10>5:
    print("verdadero")
elif 5>3: # comienza segundo condicioneal
    print ("esto no se impriomirá")
else: ("aquí nunca llega")

############
#Funcoiones#
############

def say_hello(name):
    print("Hello", name)
    print("Welcome to Python Tutorials")

say_hello("Julian")

####################################################
#Input permite obtener datps del usuario en promter#
####################################################

nombre = input("Dame tu nombre")
print("hola como estas")

########################################
#Los enteros son de presición ilimitada#
########################################

y = 50000000000000000000000000
print(y)

#################################################################
#Se pueden delimitar los números cpn guión bajo pero no con coma#
#################################################################

y = 50_000_000
print(y)

#####################################################
#La funcion int() cambia strings y floats a  enteros#
#####################################################
numero=int(input("dame tu edad: "))
type(numero)

######################################################
#La notación científica fr flotantes utilizando e o E#
######################################################

y= 12.2E-09  #1.2 x 10^{-9}
print(y)

####################################################
#Los complejos se escriben con ña raíz fr menos uno#
#j siempre con in numero com prefijo               #
#no acepta la jota suelta  la jota viene ser la i  #
####################################################
z=1+1j
print(z)
# suma +
# resta -
#división /
# modulo %
# exponete **
# // funcion piso
# Funciones para tranformar números int() float() complex()
# operacones abs () round() pow()

print (round(3.14159,4)) #el coma 4 es que quiero redondear a 4 dijitos

#########################
#Strings de varias línas#
#########################

Parrafo= """Día 1392 me tienen encadenado a un ecritorio,
me obligan a aprender python, tengo hambre, ayuda"""
print(Parrafo)

###############################################
#La función len() obtiene el tamaño del string#
###############################################

n=len(Parrafo)
print(n)

#############################################################
#Las letras en un string ocupan lugares como en un arreglo  #
#(tambien de atrás para adelantr comenzando en -1 el último)#
#############################################################
palabra= "hola"
print (palabra[0])
print (palabra[-4])



