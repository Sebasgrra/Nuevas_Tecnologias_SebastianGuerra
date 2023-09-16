isOn = int(input("Ingrese 1 para Inicialziar el servicio: "))

menu = """
1. Registro
2. Opcion2
3. Opcion3
"""
while isOn != 0:
    opc = int(input(menu))
    if opc == 1:
        print("----SISTEMA DE RESGITRO ACTIVADO----")
        name = input("Escriba su nombre: ")
        lastname = input("Escriba sus apellidos: ")
        age = input("Escriba su edad: ")
        emailaddress = input("Escriba su nuevo correo: ")
        password = input("Escriba su contraseña: ")
        print("----REGISTRO HECHO----")
    elif opc ==2:
        loginuser = input("Escriba su correo actual: ")
        loginpassword = input("Escriba su contraseña actual: ")
        captcha = int(input("How much is 9.5 + 90.5? "))
        if (emailaddress == loginuser or password == loginpassword) and captcha == 100:
             print("----SESIÓN INICIADA----")
        else:
              print("----CORREO, CONTRASEÑA O CAPTCHAT INCORRECTA----")
    elif opc == 3:
        print("Salir")
        isOn = 0
    else:
        print("Ingrese una opcion valida")