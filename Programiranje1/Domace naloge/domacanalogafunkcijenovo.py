import unittest


# 1. Funkcija prejme ovire v obliki seznama trojk (x0, x1, y) in vrne število ovir.

def stevilo_ovir(ovire):
    return len(ovire)


# 2. Funkcija vrne skupno dolžino vseh ovir.

def dolzina_ovir(ovire):
    dolzina = 0

    for od, do, _ in ovire:
        racun = do - od + 1
        dolzina = dolzina + racun

    return dolzina


# 3. Funkcija vrne širino kolesarke steze, se pravi najbolj desno koordinato v seznamu ovir.

def sirina(ovire):
    sirinaovir = None

    for _, x1, _ in ovire:
        if sirinaovir is None or x1 > sirinaovir:
            sirinaovir = x1

    return sirinaovir


# 4. Funkcija prejme vrstico v obliki niza, sestavljenega iz znakov # in . ter vrne seznam parov
#    (x0, x1) (ogrevalni del domače naloge prejšnjega tedna).

def pretvori_vrstico(vrstica):
    vrstica = "." + vrstica + "."
    spremembe = []

    for i in range(len(vrstica)):
        if vrstica[i] != vrstica[i - 1]:
            spremembe.append(i)

    bloki = []

    for zac, kon in zip(spremembe[::2], spremembe[1::2]):
        bloki.append((zac, kon - 1))

    return bloki


# 5. Funkcija prejme seznam, kakršnega vrača prejšnja funkcija in neko število y.
#    Vrniti mora seznam, v katerem je vsakemu paru dodan y.
#    Klic dodaj_vrstico([(3, 4), (6, 8), (11, 11)], 3) vrne [(3, 4, 3), (6, 8, 3), (11, 11, 3)].

def dodaj_vrstico(bloki, y):
    nova = []

    for vrstice in bloki:
        listvrstice = list(vrstice)

        listvrstice.append(y)
        nova.append(tuple(listvrstice))

    return nova


# 6. Funkcija dobi zemljevid v obliki seznama nizov in vrne seznam ovir (obvezna domača naloga prejšnjega tedna).
#    Funkcija mora uporabiti prejšnji dve funkciji - testi bodo to preverili tako,
#    da bodo začasno zamenjali tvojo funkcijo z neko drugo,
#    ki vrača napačne številke in preverili, ali so številke res "pravilno napačne".

def pretvori_zemljevid(zemljevid):
    lokacija = []

    for vrstica, ovire in enumerate(zemljevid):

        lokacije = dodaj_vrstico(pretvori_vrstico(ovire), vrstica + 1)
        for elementi in lokacije:
            lokacija.append(elementi)

    return lokacija


# 7. Funkcija prejme seznam ovir (v obliki trojk) in vrne vrstico, v kateri bi kolesar, ki se vozi po stolpcu x,
#    naletel na oviro (naloga izpred dveh tednov). Če v stolpcu ni ovir, naj vrne None.

def globina(ovire, x):
    ymin = None

    for x0, x1, yn in ovire:
        if x0 <= x <= x1 and (ymin is None or yn < ymin):
            ymin = yn

    return ymin


# 8. Funkcija vrne stolpec, v katerem kolesar pride najdlje in vrstico, do katere pride. Možno je tudi,
#    da v kakem stolpcu ni ovire; v tem primeru vrne koordinato tega stolpca in None.

def naj_stolpec(ovire):
    sirinapoti = sirina(ovire)
    naj_y = naj_x = 0

    for x in range(1, sirinapoti + 1):
        ymin = None

        for x0, x1, yn in ovire:
            if x0 <= x <= x1 and (ymin is None or yn < ymin):
                ymin = yn

        if ymin is None or ymin > naj_y:
            naj_y = ymin
            naj_x = x

            if ymin is None:
                break

    return naj_x, naj_y


# 9. Funkcija vrne seznam, katerega elementa so False oz. True glede na to, ali stolpec vsebuje kako oviro ali ne.
#     Če je širina poti 5 in sta drugi in zadnji stolpec brez ovir, vrne [False, True, False, False, True].

def senca(ovire):
    sirinapoti = sirina(ovire)
    tabelapreverjanj = []

    for x in range(1, sirinapoti + 1):
        ymin = None
        for x0, x1, yn in ovire:
            if x0 <= x <= x1 and (ymin is None or yn < ymin):
                ymin = yn

        if ymin is None:
            tabelapreverjanj.append(True)
        else:
            tabelapreverjanj.append(False)

    return tabelapreverjanj


ovire1 = [(1, 3, 6), (2, 4, 3), (4, 6, 7),
          (3, 4, 9), (6, 9, 5), (9, 10, 2), (9, 10, 8)]

ovire2 = [(1, 3, 6), (2, 4, 3), (4, 6, 7),
          (3, 4, 9), (9, 10, 2), (9, 10, 8)]

ovire3 = [(1, 3, 6), (2, 4, 3),
          (3, 4, 9), (9, 10, 2), (9, 10, 8)]


class Test(unittest.TestCase):
    def test_stevilo_ovir(self):
        self.assertEqual(7, stevilo_ovir(ovire1))
        self.assertEqual(6, stevilo_ovir(ovire2))
        self.assertEqual(0, stevilo_ovir([]))

    def test_dolzina_ovir(self):
        self.assertEqual(19, dolzina_ovir(ovire1))
        self.assertEqual(15, dolzina_ovir(ovire2))
        self.assertEqual(0, dolzina_ovir([]))

    def test_sirina(self):
        self.assertEqual(10, sirina(ovire1))
        self.assertEqual(9, sirina(ovire1[:-2]))
        self.assertEqual(6, sirina(ovire1[:-3]))
        self.assertEqual(3, sirina(ovire1[:1]))

    def test_pretvori_vrstico(self):
        self.assertEqual([(3, 5)], pretvori_vrstico("..###."))
        self.assertEqual([(3, 5), (7, 7)], pretvori_vrstico("..###.#."))
        self.assertEqual([(1, 2), (5, 7), (9, 9)], pretvori_vrstico("##..###.#."))
        self.assertEqual([(1, 1), (4, 6), (8, 8)], pretvori_vrstico("#..###.#."))
        self.assertEqual([(1, 1), (4, 6), (8, 8)], pretvori_vrstico("#..###.#"))
        self.assertEqual([], pretvori_vrstico("..."))
        self.assertEqual([], pretvori_vrstico(".."))
        self.assertEqual([], pretvori_vrstico("."))

    def test_dodaj_vrstico(self):
        self.assertEqual([(3, 4, 3), (6, 8, 3), (11, 11, 3)], dodaj_vrstico([(3, 4), (6, 8), (11, 11)], 3))

    def test_pretvori_zemljevid(self):
        zemljevid = [
            "......",
            "..##..",
            ".##.#.",
            "...###",
            "###.##",
        ]
        self.assertEqual([(3, 4, 2), (2, 3, 3), (5, 5, 3), (4, 6, 4), (1, 3, 5), (5, 6, 5)],
                         pretvori_zemljevid(zemljevid))

        global pretvori_vrstico
        pretvori = pretvori_vrstico
        try:
            def pretvori_vrstico(vrstica):
                return [(i, i) for i, c in enumerate(vrstica) if c == "#"]

            self.assertEqual([(2, 2, 2), (3, 3, 2), (1, 1, 3), (2, 2, 3), (4, 4, 3), (3, 3, 4), (4, 4, 4),
                              (5, 5, 4), (0, 0, 5), (1, 1, 5), (2, 2, 5), (4, 4, 5), (5, 5, 5)],
                             pretvori_zemljevid(zemljevid),
                             "Funkcija pretvori_zemljevid naj kar lepo uporabi pretvori_vrstico")
        finally:
            pretvori_vrstico = pretvori

        global dodaj_vrstico
        dodaj = dodaj_vrstico
        try:
            def dodaj_vrstico(ovire, vrstica):
                return [(*o, 2 * vrstica) for o in ovire]

            self.assertEqual([(3, 4, 4), (2, 3, 6), (5, 5, 6), (4, 6, 8), (1, 3, 10), (5, 6, 10)],
                             pretvori_zemljevid(zemljevid),
                             "Funkcija pretvori_zemljevid naj kar lepo uporabi dodaj_vrstico")
        finally:
            dodaj_vrstico = dodaj

    def test_globina(self):
        self.assertEqual(3, globina(ovire1, 3))
        self.assertEqual(5, globina(ovire1, 6))
        self.assertEqual(7, globina(ovire2, 6))
        self.assertIsNone(globina(ovire3, 6))

    def test_naj_stolpec(self):
        self.assertEqual((5, 7), naj_stolpec(ovire1))
        self.assertEqual((7, None), naj_stolpec(ovire2))
        self.assertEqual((5, None), naj_stolpec(ovire3))

    def test_senca(self):
        self.assertEqual([False] * 10, senca(ovire1))
        self.assertEqual([False, False, False, False, False, False, True, True, False, False], senca(ovire2))
        self.assertEqual([False, False, False, False, True, True, True, True, False, False], senca(ovire3))
        self.assertEqual([False] * 6, senca(ovire2[:-3]))
        self.assertEqual([False] * 3, senca(ovire3[:1]))


if __name__ == "__main__":
    unittest.main()
