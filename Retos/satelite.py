# satelite.py

# Simulación de desintegración orbital de un satélite
def simular_satelite():
    print("Simulación de desintegración orbital de un satélite")

    # Entradas del usuario
    altitud_actual = float(input("Ingrese la altitud inicial del satélite (km): "))
    coef_arrastre = float(input("Ingrese el coeficiente de arrastre inicial (por ejemplo, 0.01): "))
    altitud_minima = float(input("Ingrese la altitud mínima de seguridad (km): "))

    orbita = 0 #contador para llevar registros de las orbitas completadas
    umbral_estabilidad = 0.01  # km, pérdida mínima para considerar que se estabilizó

    while True:
        altitud_perdida = coef_arrastre * altitud_actual
        altitud_actual -= altitud_perdida
        coef_arrastre += 0.0001
        orbita += 1

        print(f"Órbita {orbita}: Altitud = {altitud_actual:.2f} km, Pérdida = {altitud_perdida:.4f} km")

        if altitud_actual <= altitud_minima:
            print(f"\nEl satélite ha reingresado en la atmósfera terrestre tras {orbita} órbitas.")
            break

        if altitud_perdida < umbral_estabilidad:
            print(f"\nEl satélite se ha estabilizado en una órbita a {altitud_actual:.2f} km después de {orbita} órbitas.")
            break
