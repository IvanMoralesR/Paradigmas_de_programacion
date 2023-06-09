from aplicacion.modelos.usuario import Usuario
from aplicacion.repositorio.repositoriodeusuarios import RepositorioDeUsuarios

#########################
#Clase storemanage
#NO TIENE VARIABLES!!!
#########################
class ManejoDeInscripciones:
   
    ##################################################################
    # Decorador staticmethod
    # El objeto solo tiene la funcion inscribir usuario
    # ENVUELVE LA FUNCION SIN LLAMAR VARIABLES LOCALES
    # el objeto ManejoDeIndcripciones es la interface intercambiable
    ###################################################################

    @staticmethod
    def inscribirUsuario(usuario: Usuario, repositorioDeUsuarios: RepositorioDeUsuarios)->None:
        print("----->Guardando usuario...... \n")
        repositorioDeUsuarios.abrir()
        repositorioDeUsuarios.guardar(usuario)
        repositorioDeUsuarios.cerrar()
