from Empleado import Empleado

empleado1 = Empleado(id=None,
                   nombre=None,
                   apellido=None,
                   correo=None,
                   contraseña=None,
                   cargo = None,
                   salario = None)

empleado1.registrar()
empleado1.iniciar_negocio_Empleado(empleado1.iniciar_sesion, empleado1.ver_registro)
