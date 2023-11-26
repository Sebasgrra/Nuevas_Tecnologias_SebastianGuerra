class Persona:

    def __init__(self, id, nombre, apellido, correo, contraseña):
        self._id = id
        self._nombre = nombre
        self._apellido = apellido
        self._correo = correo
        self._contraseña = contraseña

    #vamos a generar los getter and setter
    #GET
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, correo):
        self._correo = correo

    @property
    def contraseña(self):
        return self._contraseña

    @contraseña.setter
    def contraseña(self, contraseña):
        self._contraseña = contraseña

        #Vamos a generar los metodos
        # para registrar los usuarios e imprimir el registro

    def registrar_usuario(self):
        id = input(f"Ingrese el id del usuario")
        nombre = input("Ingrese el nombre del usuario")
        apellido = input("ingrese el apellido del usuario")
        correo = input("ingrese el correo del usuario")
        contraseña = input("Ingrese la contraseña")

    def imprimir_registro(self):
        print(f"id:{self._id} Nombre: {self._nombre} Apellido: {self._apellido} Correo: {self._correo}")

