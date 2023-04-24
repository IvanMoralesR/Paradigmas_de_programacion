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

#Reportar llve y valor
for k in capitals:
    print("Key= "+ k + ", Value= " + capitals[k])

#Nuevo dato para el diccionario
capitals["México"]="CDMX"
print(capitals)

#Borrar dato del diccionario

del capitals ["México"]
print(capitals)

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
miprimeralista=[]
print(miprimeralista)

##################
#Llenado de lista#
##################

miprimeralista=[1,"Javier",1.34,"Bosco","Angel",True]
print(miprimeralista)

######################################
#list: hacaer ina lista              #
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
#Quitar numeroscon indice i#
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
