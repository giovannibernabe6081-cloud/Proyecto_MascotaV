# ==============================================================================
# SISTEMA DE GESTIÓN DE MASCOTAS VIRTUALES - AVANCE 3 FINAL
# Módulo de modelos: contiene todas las clases del sistema.
#   - Encapsulamiento (Avance 2): atributos privados con getters/setters.
#   - Herencia y Polimorfismo (Avance 2): MascotaEntrenada hereda de MascotaVirtual.
#   - Composición (Avance 3): MascotaEntrenada "tiene-un(a)" lista de objetos Truco.
# ==============================================================================


# --- CLASE AUXILIAR PARA COMPOSICIÓN ---
class Truco:
    """Componente independiente: representa un truco que una mascota puede aprender."""

    def __init__(self, nombre: str, dificultad: int = 1):
        self.nombre = nombre
        self.__dificultad = 1  # Atributo privado (rango 1 a 5)
        self.dificultad = dificultad  # Pasa por el setter para validar

    @property
    def dificultad(self) -> int:
        return self.__dificultad

    @dificultad.setter
    def dificultad(self, nuevo_valor: int):
        if 1 <= nuevo_valor <= 5:
            self.__dificultad = nuevo_valor
        else:
            print(f"[ERROR] Dificultad inválida ({nuevo_valor}). Debe estar entre 1 y 5.")

    def ejecutar(self, nombre_mascota: str) -> str:
        return f"{nombre_mascota} ejecuta el truco '{self.nombre}' (dificultad {self.dificultad}/5)."

    def __str__(self) -> str:
        return f"{self.nombre} (dificultad {self.dificultad}/5)"


# --- CLASE BASE ---
class MascotaVirtual:
    # Aplicación de Encapsulamiento
    def __init__(self, nombre: str, especie: str, edad: int, color: str):
        self.nombre = nombre
        self.especie = especie
        self._edad = max(0, edad)  # Atributo protegido (int): asegura que no sea negativo
        self.color = color

        # Atributos privados
        self.__hambre = 50    # Rango: 0 (Sin hambre) a 100 (Muy hambriento)
        self.__energia = 100  # Rango: 0 (Agotado) a 100 (Lleno de energía)

    @property
    def hambre(self) -> int:
        return self.__hambre

    @hambre.setter
    def hambre(self, nuevo_valor: int):
        # Validación para garantizar que el valor se mantenga entre 0 y 100
        if 0 <= nuevo_valor <= 100:
            self.__hambre = nuevo_valor
        else:
            print(f"[ERROR] Valor inválido para hambre ({nuevo_valor}). Debe estar entre 0 y 100.")

    @property
    def energia(self) -> int:
        return self.__energia

    @energia.setter
    def energia(self, nuevo_valor: int):
        # Validación de rango para la energía
        if 0 <= nuevo_valor <= 100:
            self.__energia = nuevo_valor
        else:
            print(f"[ERROR] Valor inválido para energía ({nuevo_valor}). Debe estar entre 0 y 100.")

    # --- MÉTODOS OPERATIVOS DE LA CLASE BASE ---

    def alimentar(self):
        print(f"Alimentando a {self.nombre}...")
        self.hambre = max(0, self.hambre - 30)
        print(f"-> Nivel de hambre actual de {self.nombre}: {self.hambre}/100")

    def jugar(self):
        if self.energia < 20:
            print(f"\n¡{self.nombre} está demasiado cansado/a para jugar! Necesita dormir.")
            return

        print(f"\nJugando con {self.nombre}...")
        self.hambre = min(100, self.hambre + 20)
        self.energia = max(0, self.energia - 30)
        print(f"-> {self.nombre} jugó alegremente. Energía: {self.energia}/100 | Hambre: {self.hambre}/100")

    def dormir(self):
        print(f"\n{self.nombre} está durmiendo profundamente...")
        self.energia = 100
        print(f"-> Energía de {self.nombre} restaurada al 100%.")

    def ver_estado(self):
        print(f"\n--- Estado de {self.nombre} ({self.especie}) ---")
        print(f"Edad: {self._edad} meses")  # El texto "meses" se añade sólo para visualizar
        print(f"Color: {self.color}")
        print(f"Hambre: {self.hambre}/100")
        print(f"Energía: {self.energia}/100")
        print("-----------------------------------")


# --- SUBCLASE (Herencia + Composición) ---
class MascotaEntrenada(MascotaVirtual):
    def __init__(self, nombre: str, especie: str, edad: int, color: str, especialidad: str, nivel_inicial: int = 1):
        super().__init__(nombre, especie, edad, color)

        self.especialidad = especialidad
        self._nivel_entrenamiento = nivel_inicial
        self.trucos_aprendidos = []  # COMPOSICIÓN: la mascota "tiene" una lista de objetos Truco

    def entrenar_truco(self, nombre_truco: str, dificultad: int = 1):
        if self.energia < 25:
            print(f"\n{self.nombre} no tiene suficiente energía ({self.energia}/100) para entrenar.")
            return

        nuevo_truco = Truco(nombre_truco, dificultad)  # Se crea el objeto componente
        self.trucos_aprendidos.append(nuevo_truco)
        self._nivel_entrenamiento += 1
        self.energia = max(0, self.energia - 25)
        self.hambre = min(100, self.hambre + 15)
        print(f"\n¡{self.nombre} ha aprendido el truco '{nuevo_truco.nombre}'!")
        print(f"-> Nuevo nivel de entrenamiento: {self._nivel_entrenamiento}")

    def mostrar_truco(self, nombre_truco: str):
        # DELEGACIÓN: la mascota pide al objeto Truco que se ejecute
        for truco in self.trucos_aprendidos:
            if truco.nombre == nombre_truco:
                print(f"\n{truco.ejecutar(self.nombre)}")
                return
        print(f"\n{self.nombre} todavía no conoce el truco '{nombre_truco}'.")

    # Sobrescritura de métodos (Polimorfismo)
    def ver_estado(self):
        super().ver_estado()
        trucos = ", ".join(str(t) for t in self.trucos_aprendidos) if self.trucos_aprendidos else "Ninguno"
        print(f"Especialidad: {self.especialidad}")
        print(f"Nivel de Entrenamiento: {self._nivel_entrenamiento}")
        print(f"Trucos Aprendidos: {trucos}")
        print("===================================")
