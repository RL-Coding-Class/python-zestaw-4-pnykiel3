from abc import ABC, abstractmethod

class Pojazd(ABC):
    def __init__(self, model: str, rok: int):
        self._model = model
        self._rok = rok
        self._predkosc = 0

    @property
    def predkosc(self) -> float:
        return self._predkosc

    @predkosc.setter
    def predkosc(self, v: float):
        if v < 0:
            raise ValueError("Prędkość nie może być ujemna!")
        self._predkosc = v

    @predkosc.deleter
    def predkosc(self):
        self._predkosc = 0

class Samochod(Pojazd):
    def __init__(self, model: str, rok: int, liczba_drzwi: int):
        super().__init__(model, rok)
        self.liczba_drzwi = liczba_drzwi

class Autobus(Pojazd):
    def __init__(self, model: str, rok: int, liczba_miejsc: int):
        super().__init__(model, rok)
        self.liczba_miejsc = liczba_miejsc

class FabrykaPojazdow(ABC):
    def __init__(self, nazwa: str):
        self._nazwa = nazwa
        self._liczba_wyprodukowanych = 0

    @property
    def nazwa (self) -> str:
        return self._nazwa

    @classmethod
    def utworz_fabryke(cls, typ: str, nazwa: str):
        if typ == 'autobus':
            return FabrykaAutobusow(nazwa)
        elif typ == 'samochod':
            return FabrykaSamochodow(nazwa)
        else:
            raise ValueError("Nie umiem zrobic takiej fabryki")

    @abstractmethod
    def stworz_pojazd(self, model: str, rok: int) -> Pojazd:
        pass

    @staticmethod
    def sprawdz_rok(rok: int) -> bool:
        return 2024 >= rok >= 1900

    def ile_wyprodukowano(self) -> int:
        return self._liczba_wyprodukowanych

    def _zwieksz_licznik(self):
        self._liczba_wyprodukowanych += 1

class FabrykaSamochodow(FabrykaPojazdow):
    def stworz_pojazd(self, model: str, rok: int, liczba_drzwi: int = 4) -> Samochod:

        if self.sprawdz_rok(rok):
            pojazd = Samochod(model, rok, liczba_drzwi)
            self._zwieksz_licznik()
            return pojazd
        raise ValueError("Nieprawidłowy rok produkcji!")

class FabrykaAutobusow(FabrykaPojazdow):
    def stworz_pojazd(self, model: str, rok: int, liczba_miejsc: int = 50) -> Autobus:
        if self.sprawdz_rok(rok):
            pojazd = Autobus(model, rok, liczba_miejsc)
            self._zwieksz_licznik()
            return pojazd
        raise ValueError("Nieprawidłowy rok produkcji!")


def main():
    # Utworz fabryki pojazdow (samochodow i autobusow)
    fabryka_samochodow = FabrykaPojazdow.utworz_fabryke('samochod', "Fabryka Samochodów Warszawa")
    fabryka_autobusow = FabrykaPojazdow.utworz_fabryke('autobus', "Fabryka Autobusów Kraków")

    # Utworzone fabryki - demonstracja @property nazwa
    print(f"Nazwa fabryki: {fabryka_samochodow.nazwa}")
    print(f"Nazwa fabryki: {fabryka_autobusow.nazwa}")

    # Utworz pojazdy
    samochod = fabryka_samochodow.stworz_pojazd("Fiat", 2023, liczba_drzwi=5)
    autobus = fabryka_autobusow.stworz_pojazd("Solaris", 2023, liczba_miejsc=60)

    # Demonstracja dzialania gettera, settera i deletera
    samochod.predkosc = 50  # uzycie setter
    print(f"Prędkość samochodu: {samochod.predkosc}")  # uzycie getter
    del samochod.predkosc  # uzycie deleter
    print(f"Prędkość po reset: {samochod.predkosc}")

    # Pokazanie ile pojazdow wyprodukowano
    print(f"Wyprodukowano samochodów: {fabryka_samochodow.ile_wyprodukowano()}")
    print(f"Wyprodukowano autobusów: {fabryka_autobusow.ile_wyprodukowano()}")

if __name__ == "__main__":
    main()
