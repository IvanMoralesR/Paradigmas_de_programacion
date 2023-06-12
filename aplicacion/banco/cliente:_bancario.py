#######################
#Clase ClienteBancario
#######################
class ClienteBancario:
    __nombres: str= None
    __apellidos: str= None
    __edad: int= 0
    __balanceDeCuenta:float = 0.0

    def __init__(self, nombres:str, apellidos:str, edad:int=0, balanceDeCuenta:float=0.0):
        self.__validarEdad(edad)
        self.__validarCantidad(balanceDeCuenta)
        self.nombres = nombres
        self.apellidos = apellidos
        self.__edad = edad
        self.balanceDeCuenta

    def getNombreCompleto(self) -> str:
        return self.nombres + " " + self.apellidos

    def __mandarEmail(sel, titulo:str, texto:str) -> None:
        print("mandar email: "+ titulo + " con texto: " + texto)
    def __enviarBalanceAlBanco(self, cantidad: float) -> None:
        print("Enviando cantidad: " + str(cantidad)+ "al banco...")

    ############################################
    # Metodo privado con dos giones bajos
    # SI la eda es n¿menor a 18 genera un error
    ############################################
    def __validarEdad(self, edad:int) -> None:
        if edad < 18:
            raise Exception ("Es menor de edad")
    def imprimirInfo(self) -> str:
        return "Nombre: " + self.getNombreCompleto() + ", Edad: " + str(self.__edad) + "Balance: " + str(.__balanceDeCueta)

    #####################################################
    # Método privado que checa so el balance es negativo 
    # y genera un error
    #####################################################
    def __validarCantidad(self, balanceDeCuenta:float) -> None:
        if balanceDeCuenta < 0:
            raise Exception("El balance de la cuenta no puede ser negativo")

    def guardarDinero(self, cantidad:float) -> None:
        self.__balanceDeCuenta = self.__balanceDeCuenta + cantidad
        señf.__mandarEmail("---- guardando depósito ----", " se recibieron")


