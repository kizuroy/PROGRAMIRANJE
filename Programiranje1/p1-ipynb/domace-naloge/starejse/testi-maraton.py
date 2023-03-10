import unittest
class TestMaraton(unittest.TestCase):
    def test_v_sekunde(self):
        self.assertEqual(v_sekunde("00:00:00"), 0)
        self.assertEqual(v_sekunde("00:00:01"), 1)
        self.assertEqual(v_sekunde("00:00:02"), 2)
        self.assertEqual(v_sekunde("00:01:00"), 60)
        self.assertEqual(v_sekunde("00:02:00"), 120)
        self.assertEqual(v_sekunde("02:00:00"), 7200)
        self.assertEqual(v_sekunde("02:02:02"), 7322)
        self.assertEqual(v_sekunde("1:03:46"), 3826)
        self.assertEqual(v_sekunde("01:03:46"), 3826)
        self.assertEqual(v_sekunde("01:3:46"), 3826)
        self.assertEqual(v_sekunde("01:30:6"), 5406)
        self.assertEqual(v_sekunde("01:2:15"), 3735)

    def test_iz_sekund(self):
        self.assertEqual(iz_sekund(0), "0:0:0")
        self.assertEqual(iz_sekund(1), "0:0:1")
        self.assertEqual(iz_sekund(60), "0:1:0")
        self.assertEqual(iz_sekund(61), "0:1:1")
        self.assertEqual(iz_sekund(62), "0:1:2")
        self.assertEqual(iz_sekund(122), "0:2:2")
        self.assertEqual(iz_sekund(3600), "1:0:0")
        self.assertEqual(iz_sekund(3666), "1:1:6")


    def test_podatki(self):
        self.assertEqual(podatki("1\t14895\tROMAN SONJA\t1979\tSLO\t0:16:39\t0:33:32"),
                         ("ROMAN SONJA", 1979, 999, 2012))
        self.assertEqual(podatki("1\t14895\tROMAN B. SONJA\t1979\tSLO\t0:16:39\t0:33:32"),
                         ("ROMAN B. SONJA", 1979, 999, 2012))

    def test_razlika(self):
        self.assertEqual(pospesek("1\t14895\tROMAN SONJA\t1979\tSLO\t0:16:10\t0:32:20"), 1)
        self.assertEqual(pospesek("1\t14895\tROMAN SONJA\t1979\tSLO\t0:16:10\t0:48:30"), 2)
        self.assertEqual(pospesek("1\t14895\tROMAN SONJA\t1979\tSLO\t0:16:10\t0:24:15"), 0.5)

    @property
    def realdata(self):
        return open("10z.txt", encoding="utf-8")

    def test_naj_razlika(self):
        self.assertEqual(naj_pospesek(self.realdata), "GRUDEN SONJA")

    def test_vsi_pospeseni(self):
        self.assertEqual(
            vsi_pospeseni(self.realdata, 0.85),
            ['GRUDEN SONJA', 'DEBELJAK MOJCA', 'MESTNIK LARA', 'BALANT ZDENKA', 'HOSTA ANJA'])
        self.assertEqual(vsi_pospeseni(self.realdata, 0.8), ['GRUDEN SONJA'])

    def test_leta(self):
        self.assertEqual(
            leta(self.realdata),
            [1937, 1938, 1942, 1943] + list(range(1946, 2004))+ [2005, 2006])

    def test_tekaci_leta(self):
        self.assertEqual(tekaci_leta(self.realdata, 1948), 'JAGER JO??ICA, KO??EVAR MILA in RUPAR ALENKA')
        self.assertEqual(tekaci_leta(self.realdata, 1947), "BOLE MARIJA")
        self.assertEqual(tekaci_leta(self.realdata, 1945), "")

    def test_najboljsi_po_letih(self):
        self.assertEqual(
            najboljsi_po_letih(self.realdata),
            [(1937, 'MCNALLY ETHEL'), (1938, 'PUHAR MIRA'),
             (1942, 'LOUHI REJEC LEENA'), (1943, 'GOLOB IVANA'),
             (1946, '??U??TER??I?? DUNJA'), (1947, 'BOLE MARIJA'),
             (1948, 'JAGER JO??ICA'), (1949, '??NIDAR??I?? JO??ICA'),
             (1950, 'KRMAVNAR dAMJANA'), (1951, 'GOMIVNIK VIDA'),
             (1952, 'STRA??EK DRAGICA'), (1953, 'RINK MARJETA'),
             (1954, 'DOLENEC IRENA'), (1955, 'JERAJ MARIJA'),
             (1956, 'VRTA??NIK BOKAL EDA'), (1957, 'HERMAN EMILIJA'),
             (1958, 'HIR??MAN ALENKA'), (1959, 'P??AKER MARIJA'),
             (1960, 'MO??IVNIK ??KEDELJ BARBKA'), (1961, 'PERAK LUCIJA'),
             (1962, 'NAHTIGAL BRIGITA'), (1963, 'RUPNIK SONJA'),
             (1964, 'OBR?? TEA'), (1965, 'BERKOPEC MARTA'),
             (1966, 'SELJAK BERNARDA'), (1967, '??RNILOGAR VESNA'),
             (1968, 'RUPNIK ANDREJA'), (1969, '??TEVANEC MARIJA'),
             (1970, 'AH??IN MATEJKA'), (1971, '??GAJNER MAJDA'),
             (1972, 'HELENA VALAS'), (1973, 'Pirc Alenka'),
             (1974, 'RADIVO MANICA'), (1975, 'CONRADI MARJETKA'),
             (1976, 'VESEL HELENA'), (1977, 'STRUNA NINA'),
             (1978, 'PRAPROTNIK ZALA'), (1979, 'ROMAN SONJA'),
             (1980, 'BRODNIK NIKA'), (1981, 'LEMUT KLEMENTINA'),
             (1982, 'PAVLI?? MARY'), (1983, 'MU??I?? RADEJ NINA'),
             (1984, 'FAJDIGA ANJA'), (1985, 'PLANOV??EK ANA'),
             (1986, '??UNI?? KATJA'), (1987, 'MIKLAV??IN MAJA'),
             (1988, 'BER??I?? KATJA'), (1989, 'KOPA?? POLONA'),
             (1990, 'MU??I?? MATEJA'), (1991, 'VIDMAR SARA'),
             (1992, 'MEJA?? ANJA'), (1993, 'KOZJEK TINA'),
             (1994, 'MI??MA?? MARU??A'), (1995, '??GAJNER JERNEJA'),
             (1996, 'VAN DE VOORDE MAGDALENA'), (1997, 'GUZELJ BLATNIK LAURA'),
             (1998, 'LE??NJAK ANA'), (1999, '??ESNIK TINA'),
             (2000, 'STAUBER LAURA'), (2001, 'MIHEVC LARA'),
             (2002, 'MALI KLARA'), (2003, 'FERJAN??I?? MA??A'),
             (2005, 'SLAPNIK A??A'), (2006, 'MEGLI?? AJ??A')])

if __name__ == "__main__":
    unittest.main()
