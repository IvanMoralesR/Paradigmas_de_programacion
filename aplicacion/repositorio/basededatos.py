
from aplicacion.repositorio.repositoriodeusuarios import RepositorioDeUsuarios
from aplicaion.repositrio.modelos.usuario import Usuario

####################################################
# Para llenar la interface hay que heredar la clase
####################################################

class BaseDeDAtos(RepositorioDeUsuarios):
    __host: str
    __user: str
    __password: str

    def __init__(mi, host:str, user:str, password:str):
        mi.__host = host
        mi.__user = user
        mi.__password = password

    def abrir(mi ->) None:
        print(f"Abriendo la conexíon a la base de datos: {mi.__host}:{mi.__user}@{mi.password}")
    
    def guardar (mi, usuario:Usuario)-> None:
        useElements = { "nombre": usuario.getNombre(),
                        "apellido":usuario.getApellido(),
                        "edad": usuario.getEdad() }
        print(f"Guardando el usuario en la base de datos {usuario.getNombre()}\n")
        print(f"INSERTAR DATAOS DEL UDUARIO('{userElements['nombre']}','{useElements['aplellido']}',{userEelements['edad']})")

    def cerrar(mi) -> None:
        print("Cerrando conexion ")

#Estoy cansado, con hambre, dolor de espalda y anciedad, ayuda...


