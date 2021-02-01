#classe persona: nome, cognome, sesso, data nascita
#classe studente : nome, cognome, sesso, data di nascita, matricola,
#classe docente: nome, cognome, sesso, data di nascita, matricola, email

class Persona:


    def __init__(self, nome, cognome, sesso, data_nascita):
        self.nome = nome
        self.cognome = cognome
        self.sesso = sesso
        self.data_nascita = data_nascita

    def stampadettagli(self):
        print(self.nome + " " + self.cognome + " " + self.sesso + " " + self.data_nascita)



class Studente(Persona):
    matricola = ""
    def __init__(self, nome, cognome, sesso, data_nascita, matricola):
        super().__init__(nome, cognome, sesso, data_nascita)
        self.matricola = matricola

    def stampadettagli(self):
        print("Studente: ")
        print(self.nome + " " + self.cognome + " " + self.sesso + " " + self.data_nascita + " " + self.matricola)


class Docente(Persona):

    def __init__(self, nome, cognome, sesso, data_nascita, email):
        super().__init__(nome, cognome, sesso, data_nascita)
        self.email = email

    def stampadettagli(self):
        print("Docente: ")
        print(self.nome + " " + self.cognome + " " + self.sesso + " " + self.data_nascita + " " + self.email)

d = Docente("Andrea", "Basti", "M", "22/04/1994", "esempio@gmail.com")
d.stampadettagli() #serve per richiamare la stampa. Senza questo codice una volta mandato in esecuzione il software non stampa i dettagli

s = Studente("Alberto", "Baldi", "M", "01/02/1974", " 0000907071")
s.stampadettagli() #serve per richiamare la stampa. Senza questo codice una volta mandato in esecuzione il software non stampa i dettagli
