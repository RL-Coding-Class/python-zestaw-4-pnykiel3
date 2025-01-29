from multipledispatch import dispatch
import math

class Figura(object):
    def __init__(self):
        print("Figura init")

class Prostokat(Figura):
    def __init__(self, x: int, y: int):
        super().__init__()
        self.x = x
        self.y = y

class Kwadrat(Prostokat):
    def __init__(self, x: int):
        super().__init__(x, x)

class Kolo(Figura):
    def __init__(self, r: float):
        super().__init__()
        self.r = r

# Funkcje pole
@dispatch(Figura)
def pole(instance: Figura):
    print("Pole: Figura")
    return 0

@dispatch(Prostokat)
def pole(instance: Prostokat):
    print("Pole: Prostokąt")
    return instance.x * instance.y

@dispatch(Prostokat, int, int)
def pole(instance: Prostokat, x: int, y: int):
    print(f"Pole: Prostokąt zmiana wymiarów na {x}x{y}")
    instance.x = x
    instance.y = y
    return instance.x * instance.y

@dispatch(Kwadrat)
def pole(instance: Kwadrat):
    print("Pole: Kwadrat")
    return instance.x ** 2

@dispatch(Kwadrat, int)
def pole(instance: Kwadrat, x: int):
    instance.x = x
    print(f"Pole: Kwadrat zmiana boku; x = {x}")
    return instance.x ** 2

@dispatch(Kolo)
def pole(instance: Kolo):
    print("Pole: Koło")
    return math.pi * instance.r ** 2

@dispatch(Kolo, float)
def pole(instance: Kolo, r: float):
    instance.r = r
    print(f"Pole: Koło zmiana promienia; r = {r})")
    return math.pi * instance.r ** 2

# Polimorfizm w czasie wykonywania
def polaPowierzchni(listaFigur):
    for i in listaFigur:
        print(f"Pole obiektu: {pole(i)}")

if __name__ == "__main__":
    # Tworzenie obiektów
    print("=== Tworzenie obiektów ===")
    a, b, c, d = Figura(), Prostokat(2, 4), Kwadrat(2), Kolo(3)

    # Wywołania funkcji pole
    print("\n=== Wywołania funkcji pole ===")
    print(f"Pole prostokąta (2x4): {pole(b)}")
    print(f"Pole kwadratu (bok=2): {pole(c)}")
    print(f"Pole koła (r=3): {pole(d)}")

    # Zmiana wymiarów za pomocą funkcji pole
    print("\n=== Zmiana wymiarów ===")
    print(f"Pole prostokąta po zmianie na 5x6: {pole(b, 5, 6)}")
    print(f"Pole kwadratu po zmianie boku na 7: {pole(c, 7)}")
    print(f"Pole koła po zmianie promienia na 4: {pole(d, 4.0)}")

    # Polimorfizm
    print("\n=== Polimorfizm w czasie wykonywania ===")
    polaPowierzchni([a, b, c, d])
