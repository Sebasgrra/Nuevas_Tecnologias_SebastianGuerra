from Persona import Persona

class Empleado(Persona):
    def __init__(self,id,nombre, apellido, correo, contraseña, cargo,salario):
        super().__init__(id,nombre,apellido,correo,contraseña)
        self._cargo = cargo
        self._salario = salario

    @property
    def cargo(self):
        return self._cargo

    @cargo.setter
    def cargo(self,cargo):
        self._cargo = cargo

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self,salario):
        self._salario = salario

    def registrar(self):
        super().registrar()
        self._cargo = input("Ingrese el cargo: ")
        self._salario = float(input("Ingrese el salario: "))

    def ver_registro(self):
        super().ver_registro()
        print(f"Cargo: {self._cargo} salario: {self.salario}")

    def iniciar_sesion(self):
        correo_reg=input("Ingrese el correo registrado: ")
        contras_reg=input("ingrese la contraseña registrada: ")

        if correo_reg == self._correo and contras_reg == self._contraseña:
            print(f"Bienvenido {self.nombre}")
            return True
        else:
            print("Validad tus credenciales")
            return False

    def iniciar_negocio_Empleado(self, iniciar_sesion, ver_registro):
        init = iniciar_sesion()

        while init==True:
            print("1: Ver datos usuario 2: hacer otra cosa 3: salir")
            opcion=int(input("Seleccione una opcion: "))

            if opcion==1:
                print("Ver datos usuarios")
                ver_registro()
            elif opcion==2:
                print("Hacer cosa")
            elif opcion==3:
                print("Salir")
                init = False
            else:
                print("Seleciione una opcion correcta: ")
