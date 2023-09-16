saldo = 0
acumIngresos = 0
acumEgresos = 0

isOn = int(input("Ingrese 1 para Inicialziar el servicio: "))

while isOn != 0:
    opc = int(input("1. Ingreso:\n2. Egresos:\n3. Salir\n"))
    if opc == 1:
        ingreso = int(input("Registre el Ingreso\n"))
        saldo = saldo + ingreso 
        print(f"Su saldo es: ${saldo}")
        acumIngresos += 1
        print(acumIngresos)
    elif opc ==2:
        egreso = int(input("Registre su monto a Retirar: "))
        saldo = saldo - egreso 
        if saldo < 0:
            print("Saldo Insuficiente")
            saldo = saldo + ingreso
            print(saldo)
        
        else:
            print(f"Su saldo es: ${saldo}")
        acumEgresos += 1
        print(acumEgresos)
    elif opc == 3:
        print("Salir")
        isOn = 0
    else:
        print("Ingrese una opcion valida")
        

#RegistreIngresos = float(input("Consigne su dinero: "))
#print("Su dinero Consignado es" +RegistreIngresos)