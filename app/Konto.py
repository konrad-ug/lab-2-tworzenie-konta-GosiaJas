class Konto:

    def __init__(self, imie, nazwisko, pesel, kod = None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.saldo = 0
        self.pesel = pesel

        self.historia = []

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
            self.historia.append(-przelewWychodzacy)

    def przelewWchodzacy(self, przelewWchodzacy):
        self.saldo += przelewWchodzacy
        self.historia.append(przelewWchodzacy)

    def ekspresowyWychodzacy(self, kwotaEkspresowego):
        if (self.saldo >= kwotaEkspresowego):
            self.saldo -= kwotaEkspresowego
            self.saldo -= 1
            self.historia.append(-kwotaEkspresowego)
            self.historia.append(-1)

    def zaciagnijKredyt(self,kwotaKredytu):
        if(len(self.historia) < 5):
            return False
        elif(self.historia[-1] > 0 and self.historia[-2] > 0 and self.historia[-3] > 0 and sum(self.historia[-5:-1]) > kwotaKredytu):
            self.saldo += kwotaKredytu
            return True

        else:
            return False
                

class KontoFirmowe(Konto):
    
    def __init__(self, nazwa, NIP):
        self.nazwa = nazwa
        self.saldo = 0
        self.historia=[]
        if (len(NIP) != 10):
            self.NIP = "Niepoprawny NIP"
        else:
            self.NIP = NIP

    def ekspresowyWychodzacy(self, kwotaEkspresowego):
        if (self.saldo >= kwotaEkspresowego):
            self.saldo -= kwotaEkspresowego
            self.saldo -= 5
            self.historia.append(-kwotaEkspresowego)
            self.historia.append(-5)




