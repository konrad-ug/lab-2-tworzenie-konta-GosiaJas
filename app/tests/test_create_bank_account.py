import unittest

from ..Konto import Konto
from ..Konto import KontoFirmowe

class TestCreateBankAccount(unittest.TestCase):

    def test_tworzenie_konta(self):
        pierwsze_konto = Konto("Dariusz", "Januszewski", "94110912342", "PROM_123")
        self.assertEqual(pierwsze_konto.imie, "Dariusz", "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, "Januszewski", "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 50, "Saldo nie jest równe 50!")
        self.assertEqual(pierwsze_konto.pesel, "94110912342", "Pesel nie został zapisany!") #f2
        self.assertEqual(len(pierwsze_konto.pesel), 11, "Niepoprawny pesel") #f3

    def test2_tworzenie_konta(self):
        drugie_konto = Konto("Ania", "Janek", "03211783450", "PROM_123")
        self.assertEqual(drugie_konto.imie, "Ania", "Imie nie zostało zapisane!")
        self.assertEqual(drugie_konto.nazwisko, "Janek", "Nazwisko nie zostało zapisane!")
        self.assertEqual(drugie_konto.saldo, 50, "Saldo nie jest równe 50!")
        self.assertEqual(drugie_konto.pesel, "03211783450", "Pesel nie został zapisany!")  # f2
        self.assertEqual(len(drugie_konto.pesel), 11, "Niepoprawny pesel")  # f3

    def test3_tworzenie_konta(self):
        trzecie_konto = Konto("Franek", "Kowal", "53110912342", "PROM_123")
        self.assertEqual(trzecie_konto.imie, "Franek", "Imie nie zostało zapisane!")
        self.assertEqual(trzecie_konto.nazwisko, "Kowal", "Nazwisko nie zostało zapisane!")
        self.assertEqual(trzecie_konto.saldo, 0, "Saldo nie jest zerowe!")
        self.assertEqual(trzecie_konto.pesel, "53110912342", "Pesel nie został zapisany!") #f2
        self.assertEqual(len(trzecie_konto.pesel), 11, "Niepoprawny pesel") #f3

    def test4_tworzenie_konta(self):
        czwarte_konto = Konto("Dariusz", "Januszewski", "94110912342")
        self.assertEqual(czwarte_konto.imie, "Dariusz", "Imie nie zostało zapisane!")
        self.assertEqual(czwarte_konto.nazwisko, "Januszewski", "Nazwisko nie zostało zapisane!")
        self.assertEqual(czwarte_konto.saldo, 0, "Saldo nie jest zerowe!")
        self.assertEqual(czwarte_konto.pesel, "94110912342", "Pesel nie został zapisany!")  # f2
        self.assertEqual(len(czwarte_konto.pesel), 11, "Niepoprawny pesel")  # f3

    def test5_tworzenie_konta(self):
        piate_konto = Konto("Dariusz", "Januszewski", "94110912342", "xyz")
        self.assertEqual(piate_konto.imie, "Dariusz", "Imie nie zostało zapisane!")
        self.assertEqual(piate_konto.nazwisko, "Januszewski", "Nazwisko nie zostało zapisane!")
        self.assertEqual(piate_konto.saldo, 0, "Saldo nie jest zerowe!")
        self.assertEqual(piate_konto.pesel, "94110912342", "Pesel nie został zapisany!")  # f2
        self.assertEqual(len(piate_konto.pesel), 11, "Niepoprawny pesel")  # f3

    def test6_tworzenie_konta(self):
        szoste_konto = Konto("Joanna", "Mazur", "01321760021", "xyz")
        self.assertEqual(szoste_konto.imie, "Joanna", "Imie nie zostało zapisane!")
        self.assertEqual(szoste_konto.nazwisko, "Mazur", "Nazwisko nie zostało zapisane!")
        self.assertEqual(szoste_konto.saldo, 0, "Saldo nie jest zerowe!")
        self.assertEqual(szoste_konto.pesel, "01321760021", "Pesel nie został zapisany!")  # f2
        self.assertEqual(len(szoste_konto.pesel), 11, "Niepoprawny pesel")  # f3

    def test7_tworzenie_konta(self):
        siodme_konto = Konto("Joanna", "Mazur", "01321760021", "PROM_pro")
        self.assertEqual(siodme_konto.imie, "Joanna", "Imie nie zostało zapisane!")
        self.assertEqual(siodme_konto.nazwisko, "Mazur", "Nazwisko nie zostało zapisane!")
        self.assertEqual(siodme_konto.saldo, 50, "Saldo nie jest równe 50!")
        self.assertEqual(siodme_konto.pesel, "01321760021", "Pesel nie został zapisany!")  # f2
        self.assertEqual(len(siodme_konto.pesel), 11, "Niepoprawny pesel")  # f3

    def test8_tworzenie_konta(self):
        osme_konto = Konto("Joanna", "Mazur", "01321760021")
        self.assertEqual(osme_konto.imie, "Joanna", "Imie nie zostało zapisane!")
        self.assertEqual(osme_konto.nazwisko, "Mazur", "Nazwisko nie zostało zapisane!")
        self.assertEqual(osme_konto.saldo, 0, "Saldo nie jest zerowe!")
        self.assertEqual(osme_konto.pesel, "01321760021", "Pesel nie został zapisany!")  # f2
        self.assertEqual(len(osme_konto.pesel), 11, "Niepoprawny pesel")  # f3

    def test9_tworzenie_konta(self):
        dziewiate_konto = Konto("Joanna", "Mazur", "01321760021", "PROM_123456789")
        self.assertEqual(dziewiate_konto.imie, "Joanna", "Imie nie zostało zapisane!")
        self.assertEqual(dziewiate_konto.nazwisko, "Mazur", "Nazwisko nie zostało zapisane!")
        self.assertEqual(dziewiate_konto.saldo, 0, "Saldo nie jest zerowe!")
        self.assertEqual(dziewiate_konto.pesel, "01321760021", "Pesel nie został zapisany!")  # f2
        self.assertEqual(len(dziewiate_konto.pesel), 11, "Niepoprawny pesel")  # f3

    def test10_tworzenie_konta(self):
        dziewiate_konto = Konto("Adam", "Małysz", "77120356421", "PROM_123")
        self.assertEqual(dziewiate_konto.imie, "Adam", "Imie nie zostało zapisane!")
        self.assertEqual(dziewiate_konto.nazwisko, "Małysz", "Nazwisko nie zostało zapisane!")
        self.assertEqual(dziewiate_konto.saldo, 50, "Saldo nie jest rowne 50!")
        self.assertEqual(dziewiate_konto.pesel, "77120356421", "Pesel nie został zapisany!")  # f2
        self.assertEqual(len(dziewiate_konto.pesel), 11, "Niepoprawny pesel")  # f3

class TestsPrzelewy(unittest.TestCase):

    def testPrzelewWychodzacy_wystarczajaceSrodki(self):
        konto = Konto("Dariusz", "Januszewski", "94110912342")
        przelew = 100
        konto.saldo = 500
        konto.przelewWychodzacy(przelew)
        self.assertEqual(konto.saldo, 500 - przelew, "Nie udalo sie wykonac przelewu")

    def testPrzelewWychodzacy_niewystarczajaceSrodki(self):
        konto = Konto("Dariusz", "Januszewski", "94110912342")
        przelew = 400
        konto.saldo = 200
        konto.przelewWychodzacy(przelew)
        self.assertEqual(konto.saldo, 200, "Udalo sie wykonac przelew")

    def testPrzelewWchodzacy(self):
        konto = Konto("Dariusz", "Januszewski", "94110912342")
        przelew = 100
        konto.saldo = 200
        konto.przelewWchodzacy(przelew)
        self.assertEqual(konto.saldo, 200 + przelew, "Nie udalo sie odebrac przelewu")

    def testKilkaPrzelewów(self):
        konto = Konto("Dariusz", "Januszewski", "94110912342")
        konto.saldo = 400
        konto.przelewWchodzacy(300)
        konto.przelewWychodzacy(200)
        konto.przelewWychodzacy(200)
        konto.przelewWchodzacy(100)
        self.assertEqual(konto.saldo,400 + 300 - 200 - 200 + 100, "Nie udalo sie wykonac serii przelewów")

class TestsKontoFirmowe(unittest.TestCase):
    def testPoprawnyNIP(self):
        konto = KontoFirmowe("firma", "1234567890")
        self.assertEqual(len(konto.NIP), 10, "Niepoprawna długość NIP")

    def testZaDlugiNIP(self):
        konto = KontoFirmowe("firma", "123456789101112")
        self.assertEqual(konto.NIP, "Niepoprawny NIP", "Bład!")

    def testZaKrotkiNIP(self):
        konto = KontoFirmowe("firma", "12345")
        self.assertEqual(konto.NIP, "Niepoprawny NIP", "Błąd!")

class TestsPrzelewyEkspresowe(unittest.TestCase):
    def testEkspresowyWychodzacy_kontoZwykle_wystarczajaceSrodki(self):
        konto = Konto("Dariusz", "Januszewski", "94110912342")
        konto.saldo = 500
        konto.ekspresowyWychodzacy(300)
        self.assertEqual(konto.saldo, 500 - 300 - 1, "Nie udało się wykonać przelewu ekspresowego")

    def testEkspresowyWychodzacy_kontoZwykle_niewystarczajaceSrodki(self):
        konto = Konto("Dariusz", "Januszewski", "94110912342")
        konto.saldo = 500
        konto.ekspresowyWychodzacy(800)
        self.assertEqual(konto.saldo, 500, "Blad!")

    def testEkspresowyWychodzacy_kontoZwykle_przelewWszystkichSrodkow(self):
        konto = Konto("Dariusz", "Januszewski", "94110912342")
        konto.saldo = 500
        konto.ekspresowyWychodzacy(500)
        self.assertEqual(konto.saldo, 500 - 500 - 1, "Nieudało się wykonać przelewu ekspresowego")

    def testEkspresowyWychodzacy_kontoFirmowe_wystarczajaceSrodki(self):
        konto = KontoFirmowe("firma", "1234567890")
        konto.saldo = 500
        konto.ekspresowyWychodzacy(300)
        self.assertEqual(konto.saldo, 500 - 300 - 5, "Nie udało się wykonać przelewu ekspresowego")

    def testEkspresowyWychodzacy_kontoFirmowe_niewystarczajaceSrodki(self):
        konto = KontoFirmowe("firma", "1234567890")
        konto.saldo = 500
        konto.ekspresowyWychodzacy(800)
        self.assertEqual(konto.saldo, 500, "Blad!")

    def testEkspresowyWychodzacy_kontoFirmowe_przelewWszystkichSrodkow(self):
        konto = KontoFirmowe("firma", "1234567890")
        konto.saldo = 500
        konto.ekspresowyWychodzacy(500)
        self.assertEqual(konto.saldo, 500 - 500 - 5, "Nieudało się wykonać przelewu ekspresowego")

class TestHistoria(unittest.TestCase):
    def testHistoria_KontoZwykle(self):
        konto = Konto("Dariusz", "Januszewski", "94110912342")
        konto.przelewWchodzacy(300)
        konto.przelewWchodzacy(500)
        konto.przelewWychodzacy(200)
        konto.przelewWchodzacy(50)
        konto.przelewWychodzacy(120)
        konto.ekspresowyWychodzacy(320)
        konto.przelewWchodzacy(80)
        self.assertEqual(konto.historia, [300,500,-200,50,-120, -320, -1, 80], "Błąd w historii")

    def testHistoria_KontoFirmowe(self):
        konto = KontoFirmowe("firma", "1234567890")
        konto.przelewWchodzacy(300)
        konto.przelewWchodzacy(500)
        konto.przelewWychodzacy(200)
        konto.przelewWchodzacy(50)
        konto.przelewWychodzacy(120)
        konto.ekspresowyWychodzacy(320)
        konto.przelewWchodzacy(80)
        self.assertEqual(konto.historia, [300,500,-200,50,-120,-320, -5,80], " Błąd w historii")

class TestZaciaganieKredytu(unittest.TestCase):
    def testKredytUdzielony(self):
        konto = Konto("Dariusz", "Januszewski", "94110912342")
        konto.historia = [400, -300, 400, -50, 120, 300, 20]
        konto.zaciagnijKredyt(400)
        self.assertEqual(konto.zaciagnijKredyt(400), True, "Nie przyznano kredytu")

    def testKredytNieudzielony_ZaKrotkaHistoria(self):
        konto = Konto("Dariusz", "Januszewski", "94110912342")
        konto.historia = [300, 400, 20]
        konto.zaciagnijKredyt(400)
        self.assertEqual(konto.zaciagnijKredyt(400), False, "Błąd")
    
    def testKredytNieudzielony_OstatnieZaksiegowanieWyplata(self):
        konto = Konto("Dariusz", "Januszewski", "94110912342")
        konto.historia = [300, 400, -20, 100, -60, 200, -55]
        konto.zaciagnijKredyt(400)
        self.assertEqual(konto.zaciagnijKredyt(400), False, "Błąd")

    def testKredytNieudzielony_KredytWiekszyNizSumaOstatnichTransakci(self):
        konto = Konto("Dariusz", "Januszewski", "94110912342")
        konto.historia = [300, 400, 20, -300, -50, 100, 55, 400]
        konto.zaciagnijKredyt(400)
        self.assertEqual(konto.zaciagnijKredyt(400), False, "Błąd")


        # refractor i zadanie 13 