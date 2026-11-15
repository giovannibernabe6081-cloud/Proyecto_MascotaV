# ==============================================================================
# MAIN - AVANCE 3 FINAL
# ==============================================================================
from modelos import MascotaVirtual, MascotaEntrenada, Truco

# --- Instanciación ---
catty = MascotaVirtual("Catty", "Gato", 1, "Negro")
aslan = MascotaEntrenada("Aslan", "Perro", 3, "Café", "Agilidad")
blue = MascotaEntrenada("Blue", "Perro", 5, "Blanco", "Búsqueda")

# --- 1. Encapsulamiento (getters/setters con validación) ---
print("=== PRUEBA 1: ENCAPSULAMIENTO ===")
catty.hambre = 80          # Valor válido: el setter lo acepta
print(f"Hambre de Catty: {catty.hambre}")
catty.hambre = 150         # Valor inválido: el setter lo rechaza
print(f"Hambre de Catty (sin cambios): {catty.hambre}")

# --- 2. Herencia (MascotaEntrenada usa métodos de MascotaVirtual) ---
print("\n=== PRUEBA 2: HERENCIA ===")
aslan.alimentar()
aslan.jugar()

# --- 3. Composición (MascotaEntrenada tiene objetos Truco) ---
print("\n=== PRUEBA 3: COMPOSICIÓN ===")
aslan.entrenar_truco("Dar la pata", 2)
aslan.entrenar_truco("Rodar", 3)
aslan.mostrar_truco("Dar la pata")   # Delegación: invoca Truco.ejecutar() a través de la mascota
aslan.mostrar_truco("Saltar aro")    # Truco que aún no conoce

truco_suelto = Truco("Sentarse", 1)  # El componente también funciona de forma independiente
print(f"\nTruco independiente: {truco_suelto.ejecutar('Cualquier mascota')}")

# --- 4. Polimorfismo (mismo método, comportamiento distinto) ---
print("\n=== PRUEBA 4: POLIMORFISMO ===")
for mascota in [catty, aslan, blue]:
    mascota.ver_estado()   # La versión ejecutada depende del tipo real del objeto
