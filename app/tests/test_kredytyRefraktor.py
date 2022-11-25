import unittest

from ..Konto import Konto
from ..Konto import KontoFirmowe

from parameterized import parameterized

class TestsKredytyRefaktor(unittest.TestCase):
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

    def testZaciaganieKredytu(self, historia, wnioskowanaKwota, wynikWniosku):
        self.konto.historia = historia
        czyPrzyznany =self.konto.zaciagnijKredyt(wnioskowanaKwota)
        self.assertEqual(czyPrzyznany, wynikWniosku, "Błąd")