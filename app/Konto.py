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
    def przelewWychodzacy(self, przelewWychodzacy):
        if(self.saldo >= przelewWychodzacy):
            self.saldo -= przelewWychodzacy

    def przelewWchodzacy(self, przelewWchodzacy):
        self.saldo += przelewWchodzacy

    def ekspresowyWychodzacy(self, kwotaEkspresowego):
        if (self.saldo >= kwotaEkspresowego):
            self.saldo -= kwotaEkspresowego
            self.saldo -= 1

class KontoFirmowe(Konto):
    def __init__(self, nazwa, NIP):
        self.nazwa = nazwa
        if (len(NIP) != 10):
            self.NIP = "Niepoprawny NIP"
        else:
            self.NIP = NIP

    def ekspresowyWychodzacy(self, kwotaEkspresowego):
        if (self.saldo >= kwotaEkspresowego):
            self.saldo -= kwotaEkspresowego
            self.saldo -= 5




