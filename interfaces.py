########################################################
#Del directorio aplicacion, 
#  el subdirectorio repositorio, 
#    el archivo basededatos.py: traer elobjeto BaseDeDatos
########################################################

from aplicacion.repositorio.basededatos import BaseDeDatos

############################################
#Del directorio aplicaion, 
#  el subdirectorio repositorio, 
#     el archivo s3.py: trae objeto S3.py
############################################
from aplicacion.repositorio.s3 import S3

##########################################################################
#Del directorio aplicacion,
#  el sundirectorio repositorio
#     el archivo sistemade archivos.py: trar el objeto SistemaDeArchivos
##########################################################################

from aplicacion.repositorio.sistemadearchivos import SistemaDeArchivos
#############################################
#Del directorio aplicacion,
#  del subdirectorio modelos
#    el archivo usuario.py: traer Usuaruio
##############################################

from aplicacion.modelos.usuario import Usuario

####################################################################################
#Del directorio aplicaion,
#  del subdirectorio negocios,
#    el archivo manejodeaplicaiones.py: trear el obejeto ManejoDeinscripciones
####################################################################################
from aplicacion.negocios.manejodeinscripciones import ManejoDeInscripciones

##########################
#Crear el objeto Usuario
##########################
usuario= Usuario("Roberto","Jimenez",18)

####################
#Crear el objeto s3
####################
repositorioS3= S3("321321321","sdf324223","MiCubeta")

#############################################################
#Inerface inscribirUsuario del objeto ManejoDeInscripciones
#############################################################
ManejoDeInscripciones.inscribirUsuario(usuario,repositorioS3)
print("\n")

######################################
#Crear el objeto sistema dedearchivos
######################################

repositorioSistemaDeArchivos = SistemaDeArchivos("/home/users")

###############################################################
#Interface inscribirUsuario del objeto ManejoDeInscripciones
###############################################################
ManejoDeInscripciones.incribirUsuario(usuario,repositorioBaseDeDatos)
print("\n")

