import random

# --- strucktura objektu wezla # ------------------------------
class Wezel:
    def __init__(self, data):
        self.lewy = None
        self.prawy = None
        self.elem = data

# --- wstawianie pojedyczej wartosci do drzewa # --------------
    def wstaw(self, data):
        if self.elem:
            if data < self.elem:
                if self.lewy is None:
                    self.lewy = Wezel(data)
                else:
                    self.lewy.wstaw(data)
            elif data > self.elem:
                if self.prawy is None:
                    self.prawy = Wezel(data)
                else:
                    self.prawy.wstaw(data)
        else:
            self.elem = data

# --- przeszukiwanie drzewa v1.1 # ----------------------------
    def szukaj_w_dzrewie(self, szukana):
        element = self
        znaleziony = False
        while element != None :
            print(element.elem)
            if szukana == element.elem:
                print('znaleziono')
                znaleziony = True
                break
            elif szukana < element.elem:
                element = element.lewy
            else:
                element = element.prawy
        return znaleziony

# --- Wyswietlanie drzewa rosnaco #----------------------------
    def PokazDrzewo(self):
        if self.lewy:
            self.lewy.PokazDrzewo()
        if self.prawy:
            self.prawy.PokazDrzewo()
        print(self.elem, end=' '),

# --- generuj drzewo po wartosciach losowych # ----------------
    def GenerujDL(self, min, max, n):
        for i in random.sample(range(min, max), n):
            self.wstaw(i)

# --- szukanie drzewa v1.0 # ----------------------------------
def SzukajN(drzewo, x):
    while drzewo != None:
        if x == drzewo.elem:
            print('znaleziony')
            return drzewo.elem
        if x < drzewo.elem:
            drzewo = drzewo.lewy
            print('2 - tu jestem')
        else:
            jest = True
            print("znaleziony")
    return drzewo



root = Wezel(12)
root.GenerujDL(1, 200, 100)
root.PokazDrzewo()
print()
# print(root.findval(7))
# print(root.findval(14))
print(root.szukaj_w_dzrewie((188)))