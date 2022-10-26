import unittest

from ..Konto import Konto

class TestCreateBankAccount(unittest.TestCase):

    def f3(self):
        pierwsze_konto = Konto("Dariusz", "Januszewski", "12345678910", "PROM_23")
        self.assertEqual(pierwsze_konto.imie, "Dariusz", "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, "Januszewski", "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")
        self.assertEqual(pierwsze_konto.pesel, "12345678910", "Pesel nie został zapisany") #f2
        self.assertEqual(len(pierwsze_konto.pesel), 11, "Niepoprawny pesel") #f3


