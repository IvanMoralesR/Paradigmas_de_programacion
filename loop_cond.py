
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
    #end= es para pinerlo de corrido
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

#####################################
#Función con argumentos desconocidos#
#####################################

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
