import unittest

from ..Konto import Konto
from ..Konto import KontoFirmowe

from parameterized import parameterized

class TestsKredytyRefaktor_KontoZwykle(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "94110912342"
    
    def setUp(self):
        self.konto = Konto(self.imie, self.nazwisko, self.pesel)

    @parameterized.expand([
        ([100, 100, 100, 600, 100], 500, True),
        ([400, -300, 400, -50, 120, 300, 20], 400, True),
        ([300, 400, 20], 100, False),
        ([300, 400, -20, 100, -60, 200, -55], 400, False),
        ([300, 400, 20, -300, -50, 100, 55, 400], 600, False) 
    ])

    def testZaciaganieKredytu_KontoZwykle(self, historia, wnioskowanaKwota, wynikWniosku):
        self.konto.historia = historia
        czyPrzyznany =self.konto.zaciagnijKredyt(wnioskowanaKwota)
        self.assertEqual(czyPrzyznany, wynikWniosku, "Błąd")

class TestsKredytyRefaktor_KontoFirmowe(unittest.TestCase):
    nazwa = "firma"
    nip = "1234567890"
    
    def setUp(self):
        self.konto = KontoFirmowe(self.nazwa, self.nip)

    @parameterized.expand([
        ([100, 1000, 800, -1775, 600, 1000], 500, True),
        ([400, 600, 500, 300, 1000], 400, False),
        ([3000, -1775, 4000, 2000], 3000, True),
        ([1775, 800, -1775, 3000, 200], 4000, False),
    ])

    def testZaciaganieKredytu_KontoFirmowe(self, historia, wnioskowanaKwota, wynikWniosku):
        self.konto.historia = historia
        czyPrzyznany =self.konto.zaciagnijKredyt(wnioskowanaKwota)
        self.assertEqual(czyPrzyznany, wynikWniosku, "Błąd")