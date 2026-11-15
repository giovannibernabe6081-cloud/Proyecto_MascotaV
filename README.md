# Proyecto_MascotaV
# Sistema de Gestión de Mascotas Virtuales - Avance 2

Este proyecto amplía el sistema de mascotas virtuales aplicando conceptos avanzados de Programación Orientada a Objetos en Python Encapsulamiento, Herencia, Polimorfismo y Modelado UML.

## Características

- Encapsulamiento Atributos privados (`__hambre`, `__energia`) protegidos con Getters y Setters `@property` que validan rangos de 0 a 100.
- Herencia Subclase `MascotaEntrenada` que extiende a `MascotaVirtual` reutilizando atributos con `super()` y añadiendo nuevos atributos propios (`especialidad`, `trucos_aprendidos`).
- Polimorfismo Sobrescritura (`override`) del método `ver_estado()` en la subclase para mostrar información extendida.

---

## Diagrama UML

```mermaid
classDiagram
    class Truco {
        +nombre: str
        -__dificultad: int
        +dificultad: int
        +ejecutar(nombre_mascota) str
    }
    class MascotaVirtual {
        +nombre: str
        +especie: str
        #_edad: int
        +color: str
        -__hambre: int
        -__energia: int
        +hambre: int
        +energia: int
        +alimentar()
        +jugar()
        +dormir()
        +ver_estado()
    }
    class MascotaEntrenada {
        +especialidad: str
        #_nivel_entrenamiento: int
        +trucos_aprendidos: list~Truco~
        +entrenar_truco(nombre_truco, dificultad)
        +mostrar_truco(nombre_truco)
        +ver_estado()
    }
    MascotaVirtual <|-- MascotaEntrenada : herencia
    MascotaEntrenada "1" *-- "0..*" Truco : composición
```
