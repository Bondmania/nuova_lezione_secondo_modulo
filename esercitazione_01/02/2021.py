# animale
# mammifero
# cane
# gatto

class Animale():
    nome = ""
    colore = ""
    sesso = ""
    def __init__(self):
        self.nome = nome
        self.colore = colore
        self.sesso = sesso

nome = "micio"
colore = "rosso"
sesso = "maschio"

    def stampa(self):
        print(self.nome + " " + self.colore)


class Mammifero(Animale):
    grandezza = ""
    provenienza = ""

    def __init__(self, nome, colore, grandezza, provenienza):
        super.__init__(nome, colore)
        self.grandezza = grandezza
        self.provenienza = provenienza



class Cane(Mammifero):
    razza = ""
    pass

class Gatto(Mammifero):
    caratteristica = ""
    pass

