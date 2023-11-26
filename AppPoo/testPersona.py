
#from Persona import Persona
from Persona import Persona

Persona1 = Persona(id=None,
                   nombre=None,
                   apellido=None,
                   correo=None,
                   contraseña=None)

Persona1.id = "1"

print(Persona1.id)

Persona1.registrar()
Persona1.ver_registro()