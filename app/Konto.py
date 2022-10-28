class Konto:
    def __init__(self, imie, nazwisko, pesel, kod = None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.saldo = 0
        self.pesel = pesel
        if(kod == None):
            self.kod = None
        else:
            if(kod[0:5] == "PROM_" and len(kod) == 8):
                # self.saldo = 50
                # f5
                if(int(pesel[0:2]) > 60 or int(pesel[2]) == 2 or int(pesel[2]) == 3):
                    self.saldo = 50
