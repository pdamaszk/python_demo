class Wezel():
    def __init__(self, dane=None):
        self.elem = dane
        self.lewy = None
        self.prawy = None

class DrzewoBin():
    def __init__(self):
        self.korzen = Wezel()

    def dodaj(self, dane):
        if self.korzen.elem == None:
            self.korzen.elem = dane
        else:
            def dodaj_do_wierzcholka(dane, wierzcholek):
                if dane < wierzcholek.elem:
                    if wierzcholek.lewy == None:
                        wierzcholek.lewy = Wezel(dane)
                    else:
                        dodaj_do_wierzcholka(dane, wierzcholek.lewy)
                if dane > wierzcholek.elem:
                    if wierzcholek.prawy == None:
                       wierzcholek.prawy = Wezel(dane)
                    else:
                        dodaj_do_wierzcholka(dane, wierzcholek.prawy)

            dodaj_do_wierzcholka(dane, self.korzen)

    def wyswietl(self):
        wynik = ''
        def przechodzenie_wzdluzne(wynik, wierzcholek):
            if wierzcholek:
                if wierzcholek.elem:
                    wynik += (str(wierzcholek.elem) + '-')
                    wynik = przechodzenie_wzdluzne(wynik, wierzcholek.lewy)
                    wynik = przechodzenie_wzdluzne(wynik, wierzcholek.prawy)
            return wynik
        def przechodzenie_poprzeczne(wynik, wierzcholek):
            if wierzcholek:
                if wierzcholek.elem:
                    wynik = przechodzenie_poprzeczne(wynik, wierzcholek.lewy)
                    wynik += (str(wierzcholek.elem) + '-')
                    wynik = przechodzenie_poprzeczne(wynik, wierzcholek.prawy)
            return wynik
        def przechodzenie_wsteczne(wynik, wierzcholek):
            if wierzcholek:
                if wierzcholek.elem:
                    wynik = przechodzenie_wsteczne(wynik, wierzcholek.lewy)
                    wynik = przechodzenie_wsteczne(wynik, wierzcholek.prawy)
                    wynik += (str(wierzcholek.elem) + '-')
            return wynik
        print(przechodzenie_wzdluzne(wynik, self.korzen))
        print(przechodzenie_poprzeczne(wynik, self.korzen))
        print(przechodzenie_wsteczne(wynik, self.korzen))

drzewo_bin = DrzewoBin()
drzewo_bin.dodaj(3)
drzewo_bin.dodaj(2)
drzewo_bin.dodaj(1)
drzewo_bin.dodaj(8)
drzewo_bin.dodaj(7)
drzewo_bin.dodaj(99)

drzewo_bin.wyswietl()