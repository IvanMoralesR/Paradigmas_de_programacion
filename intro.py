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
#Continuar instrucción en varios renglones#
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
#Funciones#
############

def say_hello(name):
    print("Hello", name)
    print("Welcome to Python Tutorials")

say_hello("Ivan UwU")

#(^-^)(^-^)(^-^)(^-^)(^-^)(^-^)(^-^)(^-^)(^-^)(^-^)(^-^)(^-^)(^-^)(^-^)(^-^)(^-^)(^-^)(^-^)(^-^)(^-^)(^-^)(^-^)(^-^)(^-^)(^-^)(^-^)(^-^)(^-^)(^-^)

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
#La notación científica de flotantes utilizando e o E#
######################################################

y= 12.2E-09  #1.2 x 10^{-9}
print(y)

#########################################################
#la función float() convierte strings y enteros a floats#
#########################################################
y = float("14.3")
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

#(^-^)(^-^)(^-^)(^-^)(^-^)(^-^)(^-^)(^-^)(^-^)(^-^)(^-^)(^-^)(^-^)(^-^)(^-^)(^-^)(^-^)(^-^)(^-^)(^-^)(^-^)(^-^)(^-^)(^-^)(^-^)(^-^)(^-^)(^-^)(^-^)

####################
#Conjunto de python#
####################
even_nums={2,4,6,8,10} #conjunto de números pares
print (even_nums)

# El bool boe parte del conjunto
emp={1,'Steve', 10.5,True} #conjunto de diferentes objetos
print(emp)
nums={1,2,3,4,4,5,5}
print(nums)

################################
#Convertir secuencia a conjunto#
#No lo genera en orden         #
################################

s= set('hello') #set convierte en conjunto
print(s)
s= set((1,3,2,4,5)) #tupla a conjunto (Lo escribe con orden pue)
print(s)

################################################
#De diccionario a conjunto: conjuntos de llaves#
################################################

d={1:'One',2:'Two'}
s= set(d)
print(s)

s.add(100) #add agraga un elemento al conjunto
print(s)

s.remove(100)
print(s)

s1={1,2,3,4,5}
s2={4,5,6,1,8}

su = s1|s2 #Unón
print(su)

si=s1&s2 #interseccion
print(si)

sr= s1-s2 #diferencia de conjuntos
print(sr)

sp=s2-s1
print(sp)

ss=s1^s2 #diferencia simétrica

print(ss)

#####################
#Uso de diccionarios#
#####################

capitals={"USA":"Washinton D.C","France":"Paris","India":"New Dehli"}
print (capitals)

#############
#llave:valor#
#############
#diccionario vacio

d= {}

#Llave entera, valor string
numNamaes={1:"One",2:"Two",3:"Three"}

#Llave real, valor string
decNames={1.5:"One and a Half",2.5:"Two and a Half", 3.5:"Three and a Half"}

#Llave tupla, valor string
items={("Parker","Reynolds","Camlin"):"pen",("LG","Whirpool","Samsung"):"Refrigerator"}

# Llave string, valor int
romanNums= {'I':1, 'II':2, 'III':3, 'VI':4, 'V':5}
print(romanNums)
print(romanNums["I"]) #improme una definicion especifica :3

print(capitals.get("India")) #imprime su definicion en el dicionario
print(capitals.get("india")) #no imprime nada porque no esta en el diccionario

#Reportar llave y valor
for k in capitals:
    print("Key= "+ k + ", Value= " + capitals[k])

#Nuevo dato para el diccionario
capitals["México"]="CDMX"
print(capitals)

#Borrar dato del diccionario

del capitals ["México"]
print(capitals)

#Borrar todo el diccionario
del capitals

#Reportar llaves
print(romanNums.keys()) #muestra las laves wiiiiii

#Reporta valores
print(romanNums.values()) #muestra las definiciones UwU

#Juicio de llave (Está o no está la llave en el diccionario)
print("I" in romanNums)
print("X" in romanNums)
print("XX" in romanNums)

#############################################
#Listas                                     #
#Las listas pueden ser de objetos diferentes#
#############################################
miprimeralista=[] #lista vacia
print(miprimeralista)

##################
#Llenado de lista#
##################

miprimeralista=[1,"Javier",1.34,"Bosco","Angel",True]
print(miprimeralista)

######################################
#list: hacaer una lista              #
#range(i,j); secuencia de i hasta j-1#
######################################
nums= list(range(1,61)) #lista con rango

for i in nums:
    print(i)

######################################
#Incluir elementos nuevos a una lista#
######################################

nums.append(61)
nums.append(62)
nums.append(63)
nums.append(61)
print(nums)

##############################
#Quitar elementos de la lista#
##############################

nums.remove(61)
print(nums)

############################
#Quitar numeros con indice i#
############################

i=61
del nums[i]
print(nums)

##############
#Borrar lista#
##############

del nums

##############
#Sumar Listas#
##############
L1= [1,2,3]
L2= [4,5,6]
print(L1+L2) #junta las listas

################
#Llenado a mano#
################

Potencial=[]
for i in range(0,1000):
    Potencial.append(float(i))
print(Potencial[100])

################################
#Generar una tupla con la lista#
################################

Potencial= tuple(Potencial)
print(Potencial[100])

#(^-^)(^-^)(^-^)(^-^)(^-^)(^-^)(^-^)(^-^)(^-^)(^-^)(^-^)(^-^)(^-^)(^-^)(^-^)(^-^)(^-^)(^-^)(^-^)(^-^)(^-^)(^-^)(^-^)(^-^)(^-^)(^-^)(^-^)(^-^)(^-^)

##############
#Condiconales#
##############
precio=50
#////////////////
#Si esto...
#///////////////
if precio < 50:
    print("El precion es menor que 50")

#////////////////////////////////
#Su no... si esto otro...
#////////////////////////////////
elif precio > 50:
    print("El precio es mayor a 50")
#///////////////////////////
#Si nada de lo anterior...
#///////////////////////////
else:
    print("El precio es 50")

precio= 50
cantidad= 5
total= precio*cantidad
########################
#Condicionales anidados#
########################

if total > 100:
    if total > 500:
        print("Total es mayoe que 500")
    else:
        if total < 500 and total > 400: #dos condiciones con el and \(^_^)/
            print("Total es menor que 500 pero menor 400")
        elif total < 500 and total > 300:
            print("Total entre 300 y 500")
        else:
            print("Total entre 100 y 300")

#////////////////////////////////////
#condicionales de igualdad son ==
#////////////////////////////////////
elif total == 100:
    print("Total es 100")
else:
    print("Total menor que 100")

############################################
#Contar mientras la condición sea verdadera#
############################################

num=0
while num < 5:
    num = num + 1
    print('num = ', num)

num=0
while num < 5:
    num+= 1 #le agrega 1 y lo guarda en num
    print('num = ', num)
    if num == 3:
        break    #break para el ciclo

num=0
while num < 5:
    num+= 1
    if num == 3:
        continue   #Evitae lo que sigue, contunuar con las iteraciones
    print('num = ', num)

###################
#Bucle sobre lista#
###################

nums = [10,20,30,40,50]
for i in nums:
    print (i)

####################
#Bucle sobre string#
####################

for char in 'Hello':
    print(char)

############################
#Bucle sobre un diccionario#
#items = Elementos         #
############################

numNames = {1:'One', 2:'Two', 3:'Three'}
for pair in numNames.items():
    print(pair)

#########################
#Bucle sobre diccionario#
#key = llave            #
#value = valor          #
#########################
for k,v in numNames.items():
    print ("key = ", k, ", value = ", v)

#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

#/|\/|\/|\/|\
#Funciones/|\
#/|\/|\/|\/|\

#################
#Primera función#
#################

def saludo():
    #//////////////////////////////////////////////////////////////////////////
    #Documentación rapida de la función (lo que lleva o mas bien lo que hace)
    #/////////////////////////////////////////////////////////////////////////
    """Esta función saluda"""
    print('¡Holi! ¿como estan?')

#/////////////////////
#Llamado de la función
#/////////////////////

saludo()

#//////////////////////////////
#Se ejecuta pero no se asigna 
#////////////////////////////// 

salida=saludo()

#/////////////////
#Esto no funciona
#////////////////
print(salida)

#######################
#Mostrar documentación#
#######################
#help(saludo)

#######################
#Función con argumento#
#######################
def salu2(nombre): #nombre es algo así como la variable en una función
    '''Está función te saluda por tu nombre'''
    print("buenas",nombre,"!")
salu2("Julian")  #evaluamos la función en Julian
salu2("Ermenejildo")

###################################
#Ahorrar trabjo al intérprete     #
#nombre:str la variable es un str #
###################################
def saludos(nombre:str):
     '''Está función te saluda por tu nombre  estrictamente'''
     print("Buenas",nombre,"!")

saludos("Ermenejildo")
a=123
print(type(a))
saludos(a) #supongo que el inerprete hace su magia y convierte el str a int porque si jala

###############################
#Funcion con muchos argumentos#
###############################

def saludos_multiples(nombre1, nombre2, nombre3):
    """Esta funcion saluda a 3 personas al mismo tiempo"""
    print("Hola ",nombre1,nombre2,"y ",nombre3)

saludos_multiples("Hugo","Paco","Luis")

############################################
#Función con cualquier numero de argumentos#
############################################

def muchos_saludos(*nombre):
    """Esta funcion saluda a todos los que quieras"""
    i=0

    #/////////////////////////////////
    #end= es para ponerlo de corrido
    #/////////////////////////////////
    print("Hols", end="")
    while len(nombre) > i:
        #Ultimo nombre
        if(i==len(nombre)-1):
            print(nombre[i])
        else:


            #cualquier otro nombre
            print(nombre[i], end=", ")
        i+=1

muchos_saludos("Chencho", "Mencho", "Sancho", "Pancho", "Juancho",)

def greet( firstname,lastname):
    print('Hello',firstname," ", lastname)

################################################
#Llamar a la función con argumentos en desorden#
################################################

greet(lastname='Zapata', firstname='Steve') #Se pueden especificar las variable en desorden

########################################
#Función con argumentos desconocidos **#
########################################

def greet(**persona):
    #/////////////////////////////////////////////////////////////
    #Persona tiene las características de first name y lastname
    #////////////////////////////////////////////////////////////
    print('Hello', persona['firstname'], persona['lastname'])

greet(firstname= 'Steve', lastname= 'Jobs')
greet(lastname= 'Jobs', firstname= 'Steve')
greet(firstname= 'Steve', lastname= 'Jobs', age= 55) #sepueden agragar más parametros de los necesarios

#################################
#Función con valores por defecto#
#################################

def greet(name= 'Guest'):
    print('Hello', name)

greet() #Utiliza el valor por defecto
greet('Steve')

#######################
#Función con resultado#
#######################

def suma(a,b):
    return a+b

#################################
#Progamación funcional          #
#Se puden finciónes en funciónes#
#################################

total=suma(5, suma(5,10))
print(total)

################################################
#Cálculo lamda                                 #
#nombre de la función= lamabda variable : función#
################################################

x_al_cuadrado = lambda x : x*x

a1 = x_al_cuadrado(5)
print(a1)

############################
#Lambda de varias variables#
############################

suma = lambda x1, x2, x3: x1+x2+x3
print(suma(99,98,97))

sumas = lambda *x: x[0]+x[1]+x[2]+x[3]
print(sumas(100,200,300,400))

#########################################
#Uso de una función anónima             #
#El argumento va afuera entre parentesis#
#########################################

print((lambda x: x*x)(6)) #funcion anónima sin nombre pues

##############################
#Funcipon con variable global#
#Evite el exceso             #
##############################

name= 'Steve'
def greet():
    global name #para utilizar una variable global(que viene afuera del bloque)
    name='Bill'
    print('Hello',name)

greet()

#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/

################################
#Algoritmo 1                   #
################################
#Serie exponencial             #
#Factorización de x            #
#Negativos con funcion inversa #
################################
n=200
x=-100.0
flag= False
if x<0:
    x= -x
s=1.0

for i in range(n,0,-1):
    s*= x/float(i)
    s+= 1.0
if flag == True:
    s= 1/s
print(s)

