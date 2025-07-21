def cargar_historial():
try:
with open("movimientos.txt", 'r') as f:
return [line.strip() for line in f]
except FileNotFoundError:
return []
def guardar_historial(movimientos):
with open("movimientos.txt", 'w') as f:
for movimiento in movimientos:
f.write(f"{movimiento}\n")
def mostrar_menu(saldo_actual, total_gastado, saldo_inicial):
porcentaje = (total_gastado / saldo_inicial) * 100 if saldo_inicial > 0
else 0
print("\n=== DATOS DE LA CUENTA ===")
print(f"Saldo actual: ${saldo_actual:.2f}")
print(f"Total gastado: ${total_gastado:.2f}")
print(f"Porcentaje gastado: {porcentaje:.2f}%")
print("\n1. Ingresar dinero")
print("2. Gastar dinero")
print("3. Ver historial")
print("4. Salir")
return input("Seleccione una opción: ")
def ingresar_dinero(saldo_actual, movimientos):
try:
monto = float(input("Monto a ingresar: "))
if monto > 0:
saldo_actual += monto
movimientos.append(f"Ingreso: +${monto:.2f}")
print("¡Ingreso registrado!")
else:
print("El monto debe ser positivo.")
except ValueError:
print("Error: Ingrese un número válido.")
return saldo_actual
def gastar_dinero(saldo_actual, total_gastado, movimientos):
try:
monto = float(input("Monto a gastar: "))
if 0 < monto <= saldo_actual:
saldo_actual -= monto
total_gastado += monto
movimientos.append(f"Gasto: -${monto:.2f}")
print("¡Gasto registrado!")
else:
print(f"Error: Monto inválido. Saldo disponible:
${saldo_actual:.2f}")
except ValueError:
print("Error: Ingrese un número válido.")
return saldo_actual, total_gastado
def ver_historial(movimientos):
print("\n=== HISTORIAL ===")
if not movimientos:
print("No hay movimientos registrados.")
else:
for i, mov in enumerate(movimientos, 1):
print(f"{i}. {mov}")
input("\nPresione Enter para continuar...")
# Programa principal
movimientos = cargar_historial()
saldo_actual = 0.0
total_gastado = 0.0
# Si no hay movimientos, pedir saldo inicial
if not movimientos:
while True:
try:
saldo_inicial = float(input("Ingrese su saldo inicial: $"))
if saldo_inicial > 0:
saldo_actual = saldo_inicial
movimientos.append(f"Saldo inicial: +${saldo_inicial:.2f}")
break
else:
print("El saldo debe ser positivo.")
except ValueError:
print("Error: Ingrese un número válido.")
else:
# Calcular saldo actual y total gastado desde movimientos
saldo_inicial = 0
for mov in movimientos:
if "Ingreso: +" in mov:
saldo_actual += float(mov.split("+$")[1])
elif "Gasto: -" in mov:
monto = float(mov.split("-$")[1])
saldo_actual -= monto
total_gastado += monto
elif "Saldo inicial: +" in mov:
saldo_actual = float(mov.split("+$")[1])
saldo_inicial = saldo_actual + total_gastado
# Bucle principal
while True:
opcion = mostrar_menu(saldo_actual, total_gastado, saldo_inicial)
if opcion == '1':
saldo_actual = ingresar_dinero(saldo_actual, movimientos)
elif opcion == '2':
saldo_actual, total_gastado = gastar_dinero(saldo_actual,
total_gastado, movimientos)
elif opcion == '3':
ver_historial(movimientos)
elif opcion == '4':
guardar_historial(movimientos)
print("\nSesión guardada. ¡Hasta luego!")
break
else:
print("Opción no válida. Intente nuevamente.")