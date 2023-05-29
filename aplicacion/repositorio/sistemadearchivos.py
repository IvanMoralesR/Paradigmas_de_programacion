from aplicacion.repoisitorio.repositoriodeusuarios import RepositorioDeUsuarios
from aplicacion.modelos.usuarios import Usuario

###############################################
#Implementa la interface RepositorioDeUsuarios
###############################################

class SistemaDeArchivos(RepositorioDeUsuarios):
    __direcorio: str

    def __init(mi, directorio:str):
        mi.__directorio = directrio

    def abrir(mi) -> None:
        print(f"Abrir directrio: {mi.__directorio}")

    def guardar(mi,usuario:Usuario) -> None:
        xml = f"</root></name>{usuario.getNombre()}</name></lastName>{usuario.getApellido()}</lastName></age>{usuario.getEdad()}</age></root>"
        print(f"Guardando usuario en el archivo :{m.__directorio}/usuario.getNombre()")
        print(xml)
    def cerrar(mi) -> None:
        print("Cerrando el archivo")
