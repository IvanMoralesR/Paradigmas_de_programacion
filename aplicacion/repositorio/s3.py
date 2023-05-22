
from aplicacion.repositorio.repositoriodeusuarios import RepositorioDeUsuarios
from aplicaion.modelos.usuario import Usuario

#####################################
#S3 es hijo de RepositorioDeUsuarios
#####################################
class S3(RepositorioDeUsuarios):
    __clientId:  str
    __secretKey: str
    __bucket: str

    def __init__(mi, clientId: str, secretKey: str, bucket: str):
        mi.__clientId = clientId
        mi.__secretKey = secretKey
        mi.__bucket = bucket

    def abrir(mi) -> None:
        print(f"Estableciendo conexión a AWS S3 {mi.__clientId}:{mi.secretKey}")
        
    def guardar(mi, usuario:Usuario) -> None:
        userData = {"nombre": usuario.getNombre(),
                  "apellido": usuario.getApellido(),
                  "edad": usuario.getEdad() }
        print(f"Guardar usuario de la bandeja:{mi.__bucket}: {userData}")

    def cerrar(mi) -> None:
        print("Cerrando conexion AWS S3")
