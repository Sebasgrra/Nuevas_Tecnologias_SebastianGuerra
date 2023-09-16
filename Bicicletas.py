isOn = int(input("Ingrese 1 para Inicialziar el servicio: "))

menu = """
1. Registro
2. Iniciar Sesión
3. Ver Usuarios Registrados
4. Asignar Bicicleta
5. Salir
"""
usuarios = []

while isOn != 0:
    opc = int(input(menu))
    if opc == 1:
        print("----SISTEMA DE REGISTRO ACTIVADO----")
        name = input("Escriba su nombre: ")
        lastname = input("Escriba sus apellidos: ")
        age = input("Escriba su edad: ")
        emailaddress = input("Escriba su nuevo correo: ")
        password = input("Escriba su contraseña: ")
        cardnumber = int(input("Dijite el numero de su tarjeta: "))
        usuario = [name, lastname, age, emailaddress, password, cardnumber]
        usuarios.append(usuario)
        print("----REGISTRO HECHO----")
    elif opc == 2:
        loginuser = input("Escriba su correo actual: ")
        loginpassword = input("Escriba su contraseña actual: ")
        captcha = int(input("How much is 9.5 + 90.5? "))
        for usuario in usuarios:
            if (usuario[3] == loginuser or usuario[4] == loginpassword) and captcha == 100:
                print("----SESIÓN INICIADA----")
                break
        else:
            print("----CORREO, CONTRASEÑA O CAPTCHA INCORRECTA----")
    elif opc == 3:
        print("Lista de Usuarios Registrados:")
        for index, usuario in enumerate(usuarios, start=1):
            print(f"Usuario {index}:")
            print(f"Nombre: {usuario[0]}")
            print(f"Apellidos: {usuario[1]}")
            print(f"Edad: {usuario[2]}")
            print(f"Correo: {usuario[3]}")
            print(f"Número de tarjeta: {usuario[5]}")
    elif opc == 4:
        card_number = int(input("Ingrese el número de tarjeta del usuario al que desea asignar una bicicleta: "))
        found = False
        for usuario in usuarios:
            if usuario[5] == card_number:
                found = True
                origen = input("Ingrese el origen de la bicicleta: ")
                destino = input("Ingrese el destino de la bicicleta: ")
                print(f"Bicicleta asignada al usuario {usuario[0]}: Origen: {origen}, Destino: {destino}")
                break
        if not found:
            print("Usuario no encontrado. No se puede asignar la bicicleta.")
    elif opc == 5:
        print("Saliendo del programa...")
        isOn = 0
    else:
        print("Ingrese una opción válida")
