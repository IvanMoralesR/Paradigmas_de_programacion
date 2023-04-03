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
