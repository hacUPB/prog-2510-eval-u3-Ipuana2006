import random
print("\n" + "-" * 50)
print(" ¡BIENVENIDO/A AL SISTEMA DE FASTFAST AIRLINES! ")
print("-" * 50 + "\n")

# 1. Información del usuario
while True:
    print("Seleccione su título:")
    print("1. Señor.")
    print("2. Señora.")
    opcion = input("Ingrese 1 o 2: ").strip()

    if opcion == "1":
        titulo = "Señor"
        break
    elif opcion == "2":
        titulo = "Señora"
        break
    else:
        print("Opción no válida. Por favor ingrese 1 o 2.")


nombre = input("Ingrese su nombre: ").strip().capitalize()
apellido = input("Ingrese su apellido: ").strip().capitalize()

print(f"\n{titulo} {nombre} {apellido}, ¡Bienvenido/a a bordo de FastFast Airlines!")

# 2. Selección de vuelo
ciudades  = ['Medellín','Bogotá','Cartagena']
# Mostrar opciones disponibles
print("Ciudades disponibles:")
for ciudad in ciudades:
    print(f"- {ciudad}")

# Obtener origen válido
while True:
    origen = input("Ingrese ciudad de origen: ").strip().title()
    if origen in ciudades:
        break
    else:
        print("Ciudad no válida. Por favor, elija entre Medellín, Bogotá o Cartagena.")

# Obtener destino válido y diferente del origen
while True:
    destino = input("Ingrese ciudad de destino: ").strip().title()
    if destino not in ciudades:
        print("Ciudad no válida. Por favor, elija entre Medellín, Bogotá o Cartagena.")
    elif destino == origen:
        print("El destino no puede ser igual al origen. Intente de nuevo.")
    else:
        break


# Resultado
print(f"\nOrigen seleccionado: {origen}")
print(f"Destino seleccionado: {destino}\n")

distancias = {
    ("Medellín", "Bogotá"): 240,
    ("Bogotá", "Medellín"): 240,
    ("Medellín", "Cartagena"): 461,
    ("Cartagena", "Medellín"): 461,
    ("Bogotá", "Cartagena"): 657,
    ("Cartagena", "Bogotá"): 657
}


# Días válidos de la semana
dias_semana = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]

# Solicitar día de la semana
while True:
    dia_semana = input("Ingrese el día de la semana que desea viajar: ").strip().lower()
    if dia_semana in dias_semana:
        break
    else:
        print("Día no válido. Intente de nuevo.")

# Solicitar día del mes
while True:
    try:
        dia_mes = int(input("Ingrese el día del mes (1 a 30): "))
        if 1 <= dia_mes <= 30:
            break
        else:
            print("Número fuera de rango. Ingrese un número entre 1 y 30.")
    except ValueError:
        print("Por favor, ingrese un número válido.")

# Determinar la distancia
distancia = distancias.get((origen, destino), 0)

# Determinar si es día de semana o fin de semana
if dia_semana in ["lunes", "martes", "miércoles", "jueves"]:
    if distancia < 400:
        precio = 79900
    else:
        precio = 156900
else:  # viernes, sábado, domingo
    if distancia < 400:
        precio = 119900
    else:
        precio = 213000

# Mostrar resultado
print(f"\nVuelo {origen} → {destino}")
print(f"Fecha: {dia_semana.title()} {dia_mes}")
print(f"Precio del boleto: ${precio:,}\n")


#3 Preguntar preferencia de asiento
print("\nPreferencia de asiento:")
print("1. Pasillo")
print("2. Ventana")
print("3. Sin preferencia")

while True:
    preferencia = input("Elija una opción (1, 2 o 3): ").strip()
    if preferencia == "1":
        letra_asiento = "C"
        break
    elif preferencia == "2":
        letra_asiento = "A"
    elif preferencia == "3":
        letra_asiento = "B"
        break
    else:
        print("Opción no válida. Intente de nuevo.")

# Número aleatorio de asiento entre 1 y 29
numero_asiento = random.randint(1, 29)
asiento = f"{numero_asiento}{letra_asiento}"

# 4. Salida
print("\n--- Confirmación de Reserva ---")
print(f"Pasajero: {titulo} {nombre} {apellido}")
print(f"Ruta: {origen} -> {destino}")
print(f"Fecha: {dia_semana.capitalize()}, día {dia_mes}")
print(f"Precio del boleto: ${precio:,}")
print(f"Asiento asignado: {asiento}")
print("------------------------------")

