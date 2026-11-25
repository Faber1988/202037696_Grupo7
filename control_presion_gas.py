presion = 0.0

for lectura in range(10):
    if presion >= 6.0:
        print("CRÍTICO: Ruptura inminente. Abortar.")
        break
    elif presion < 2.0:
        print("Acción: inyectar_gas -> Inyectando presión a la red")
        presion += 0.5
    elif presion >= 2.0 and presion <= 4.5:
        print("Acción: flujo_normal -> Flujo nominal estabilizado")
        presion += 0.1
    else:
        print("Acción: abrir_escape -> Purga de emergencia abierta")
        presion -= 0.8

    print(f"Lectura {lectura}: presión = {presion:.2f} Bar")

