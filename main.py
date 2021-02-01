class Persona:
    nome = ""
    cognome = ""
    sesso = ""

Persona.nome = "Alberto"
personaQualsiasi = Persona()
personaQualsiasi.nome = "Marco"
Persona.nome = "Franco"
print(personaQualsiasi.nome)
altrapersona = Persona()
print(altrapersona.nome)


class Persona:
    counter = 0
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome

        self.counter = self.counter + 1

        def stampa(self):
            print(self.nome + " " + self.cognome)

print(Persona.counter)
p = Persona("Alberto", "Baldi")
p.stampa()

p = Persona("Alberto", "Baldi")


#come faccio che la classe abbia lo stesso schema di un altra
#ereditarietà
#come si fa

class Utente(Persona):
    matricola = ""
    pass



class Admin(Utente):
    permessi = []

admin = Admin()
admin.stampa()