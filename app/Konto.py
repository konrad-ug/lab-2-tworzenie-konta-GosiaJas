class Konto:
    def __init__(self, imie, nazwisko, pesel, kod):
        self.imie = imie
        self.nazwisko = nazwisko
        self.saldo = 0
        self.pesel = pesel
        if(kod == None):
            self.kod = None
        else:
            if(kod[0] == "P" and kod[1] == "R" and kod[2] == "O" and kod[3] == "M" and kod[4] == "_" and len(kod) == 8):
                self.saldo = 50
