


class Persona:

    def __init__(self, id, nombre, apellido, correo, contraseña):
        self._id = id
        self._nombre = nombre
        self._apellido = apellido
        self._correo = correo
        self._contraseña = contraseña

    #Getters and setters

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
    def id(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def id(self, apellido):
        self._apellido = apellido

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def id(self, correo):
        self._correo = correo

    @property
    def contraseña(self):
        return self._contraseña

    @contraseña.setter
    def id(self, contraseña):
        self._contraseña = contraseña

    def registrar(self):
        self._id = input("Indique el Id: ")
        self._nombre = input("Indique el nombre: ")
        self._apellido = input("Indique el apellido: ")
        self._correo = input("Indique el correo: ")
        self._contraseña = input("Indique la contraseña: ")

    def ver_registro(self):
        print(f"Id:{self._id} Nombre: {self._nombre} Apellido: {self._apellido} Correo: {self._correo}")



