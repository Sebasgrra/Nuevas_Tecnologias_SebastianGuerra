from Persona import Persona


class Empleado(Persona):
    def __init__(self, id, nombre, apellido, correo, contraseña, cargo, salario, tipo_contrato):
        super().__init__(id,nombre,apellido,correo,contraseña)
        self._cargo = cargo
        self._salario = salario
        self._tipo_contatro = tipo_contrato

    @property
    def cargo(self):
        return self._cargo

    @cargo.setter
    def cargo(self, cargo):
        self._cargo = cargo

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, salario):
        self._salario = salario

    @property
    def tipo_contrato(self):
        return self._tipo_contrato

    @tipo_contrato.setter
    def tipo_contrato(self, contrato):
        self._tipo_contrato = contrato

    #Vamos a sobre escribir los metodos
    def registrar_usuario(self):
        self.id = input(f"Ingrese el id del usuario")
        self.nombre = input("Ingrese el nombre del usuario")
        self.apellido = input("Ingrese el apellido del usuario")
        self.correo = input("Ingrese el correo del usuario")
        self.contraseña = input("Ingrese la contraseña")
        self.cargo = input("Ingrese el cargo del empleado")
        self.salario = float(input("Ingrese salario del empleado"))
        self.tipo_contrato = input("Indique el tipo del salario")

    def imprimir_registro(self):
        super().imprimir_registro()
        print(f"Cargo: {self._cargo} salario: {self._salario} Tipo de contrato: {self._tipo_contrato}")



















    def iniciar_sesion(self):
        correo_reg = input("Ingrese el correo registrado: ")
        contras_reg = input("ingrese la contraseña registrada: ")

        if correo_reg == self._correo and contras_reg == self._contraseña:
            print(f"Bienvenido {self.nombre}")
            return True
        else:
            print("Validad tus credenciales")
            return False

    def iniciar_negocio_Empleado(self, iniciar_sesion, ver_registro):
        init = iniciar_sesion()

        while init == True:
            print("1: Ver datos usuario 2: hacer otra cosa 3: salir")
            opcion = int(input("Seleccione una opcion: "))

            if opcion == 1:
                print("Ver datos usuarios")
                ver_registro()
            elif opcion == 2:
                print("Hacer cosa")
            elif opcion == 3:
                print("Salir")
                init = False
            else:
                print("Seleciione una opcion correcta: ")
