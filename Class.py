class Pies:

    gatunek = "Pies domowy"

    def __init__(self, rasa, imie, wiek):
        print("Leci INIT")
        self.rasa = rasa
        self.imie = imie
        self.wiek = wiek

    def szczekaj(self):
        print(self.imie + " szczeka: Hau hau!")

    def zaprezentuj_psa(self):
        print("Rasa to " + self.rasa)
        print("Imie to " + self.imie)
        print("Wiek to " + str(self.wiek))


reksio = Pies("Kundele", "Reksio", 2)
azor = Pies("Kundele", "Azor", 3)
reksio.zaprezentuj_psa()
reksio.szczekaj()
