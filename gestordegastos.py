def main():
    while True:
        try:
            saldo_inicial = float(input("Ingrese el monto inicial (positivo): "))
            if saldo_inicial > 0:
                break
            else:
                print("El monto debe ser positivo.")
        except ValueError:
            print("Entrada inválida. Intente de nuevo.")

    total_gastado = 0.0

    while True:
        porcentaje_gastado = (total_gastado / saldo_inicial) * 100 if saldo_inicial > 0 else 0
        print("\n================ DATOS DE LA CUENTA ================")
        print(f"Saldo actual: ${saldo_inicial - total_gastado:.2f}")
        print(f"Total gastado: ${total_gastado:.2f}")
        print(f"Porcentaje gastado: {porcentaje_gastado:.2f}%")
        print("====================================================")
        print("1. Ingresar dinero")
        print("2. Ingresar un gasto")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            try:
                monto = float(input("Ingrese el monto a agregar: "))
                if monto > 0:
                    saldo_inicial += monto
                else:
                    print("El monto debe ser positivo.")
            except ValueError:
                print("Entrada inválida.")
        elif opcion == '2':
            try:
                gasto = float(input("Ingrese el monto del gasto: "))
                if 0 < gasto <= (saldo_inicial - total_gastado):
                    total_gastado += gasto
                else:
                    print("Monto inválido o insuficiente.")
            except ValueError:
                print("Entrada inválida.")
        elif opcion == '3':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida.")
main()