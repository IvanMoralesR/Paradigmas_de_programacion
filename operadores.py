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
