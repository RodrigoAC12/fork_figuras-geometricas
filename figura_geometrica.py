"""Módulo para calcular áreas de figuras geométricas.

Este módulo proporciona clases para calcular el área de diferentes figuras geométricas
como rectángulos, triángulos y círculos, implementando una interfaz abstracta común.
"""

from abc import ABC, abstractmethod


class FiguraGeometrica(ABC):
    """Clase abstracta que define la interfaz para figuras geométricas."""

    @abstractmethod
    def calcular_area(self):
        """Calcula el área de la figura."""

    @abstractmethod
    def describir(self):
        """Devuelve una descripción de la figura."""
        return "Figura geométrica"


class Rectangulo(FiguraGeometrica):
    """Clase que representa un rectángulo."""

    def __init__(self, base, altura):
        """Inicializa el rectángulo con base y altura."""
        self.base = base
        self.altura = altura

    def calcular_area(self):
        """Calcula el área del rectángulo."""
        return self.base * self.altura

    def describir(self):
        """Devuelve una descripción del rectángulo."""
        return f"Rectángulo de base {self.base} y altura {self.altura}"


class Triangulo(FiguraGeometrica):
    """Clase que representa un triángulo."""

    def __init__(self, base, altura):
        """Inicializa el triángulo con base y altura."""
        self.base = base
        self.altura = altura

    def calcular_area(self):
        """Calcula el área del triángulo."""
        return (self.base * self.altura) / 2

    def describir(self):
        """Devuelve una descripción del triángulo."""
        return f"Triángulo de base {self.base} y altura {self.altura}"


class Circulo(FiguraGeometrica):
    """Clase que representa un círculo."""

    def __init__(self, radio):
        """Inicializa el círculo con radio."""
        self.pi = 3.14159
        self.radio = radio

    def calcular_area(self):
        """Calcula el área del círculo."""
        return self.pi * (self.radio ** 2)

    def describir(self):
        """Devuelve una descripción del círculo."""
        return f"Círculo de radio {self.radio}"


# Variables globales
BASE_RECTANGULO = 10
ALTURA_RECTANGULO = 5
BASE_TRIANGULO = 7
ALTURA_TRIANGULO = 4
RADIO_CIRCULO = 3

if __name__ == "__main__":
    figuras = [
        Rectangulo(BASE_RECTANGULO, ALTURA_RECTANGULO),
        Triangulo(BASE_TRIANGULO, ALTURA_TRIANGULO),
        Circulo(RADIO_CIRCULO),
    ]

    for figura in figuras:
        print(f"{figura.describir()} - Área: {figura.calcular_area()}")
