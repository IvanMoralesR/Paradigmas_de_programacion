from aplicacion.banco.cliente_bancario import ClienteBancario

##############################################
# try; intenta (correr las instrucciones)
# except: atrapar el error en una variable e
# e se puede convertir a string
##############################################

##########################################
# Error por sacar más dinero de que tiene
##########################################
try:
    cliente = ClienteBancario("Jaime Andrade", "Hernández Sanchéz", 28. 0.0)
    cliente.guardarDinero(300)
    print(cliente,imprimirInfo())
    cliente.retirarDinero(400)
    print(cliente,imprimiInfo())
#############################################
# Exepcion es el objeto más general de error
#############################################

try:
    print(cliente.__nombres)
except Exception as ex:
    print("Error: "+ str(ex))

#################
# Forma correcta
#################
print(cliente.nombres)

