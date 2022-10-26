import unittest

from ..Konto import Konto

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