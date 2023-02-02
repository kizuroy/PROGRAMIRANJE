import unittest
import ast
from itertools import chain


def stevilo_ovir(ovire):
    return len(ovire)


def dolzina_ovir(ovire):
    return sum(x1 - x0 + 1 for x0, x1, _ in ovire)


def sirina(ovire):
    return max(x1 for _, x1, _ in ovire)


def pretvori_vrstico(vrstica):
    vrstica = "." + vrstica + "."
    bloki = []
    for i, znak in enumerate(vrstica):
        if znak == "#":
            if vrstica[i - 1] == ".":
                zacetek = i
            if vrstica[i + 1] == ".":
                bloki.append((zacetek, i))
    return bloki

# def pretvori_vrstico(vrstica):
#     return [(i, i + 1) for i, j in enumerate("." + vrstica + ".", 1) if j == "#" and ("." + vrstica + ".")[i - 2] == "." and ("." + vrstica + ".")[i] == "."]


# def indeksi(s, subs):
#     return [i for i in range(len(s)) if s.find(subs, i) == i]
def indeksi(s, subs):
    return [i for i in range(len(s)) if s[i:i + len(subs)] == subs]



def dodaj_vrstico(bloki, y):
    return [(x0, x1, y) for x0, x1 in bloki]


# def pretvori_zemljevid(zemljevid):
#     ovire = []
#     for y, vrstica in enumerate(zemljevid, start = 1):
#         ovire += dodaj_vrstico(pretvori_vrstico(vrstica), y)
#     return ovire
def pretvori_zemljevid(zemljevid):
    return list(chain.from_iterable(
        [dodaj_vrstico(pretvori_vrstico(vrstica), y) for y, vrstica in enumerate(zemljevid, start = 1)]))


def globina(ovire, x):
    return min([y for x0, x1, y in ovire if x0 <= x <= x1], default = None)


def naj_stolpec(ovire):
    naj_y = 0
    for x in range(1, sirina(ovire) + 1):
        g = globina(ovire, x)
        if g == None:
            return x, None
        if g > naj_y:
            naj_y = g
            naj_x = x
    return naj_x, naj_y

# def naj_stolpec(ovire):
#     return min([(x, y) for x, y in enumerate(senca(ovire), start = 1) if y], key = lambda x: x[1], default = 1)


def senca(ovire):
    return [globina(ovire, x) is None for x in range(1, sirina(ovire) + 1)]


ovire1 = [(1, 3, 6), (2, 4, 3), (4, 6, 7),
          (3, 4, 9), (6, 9, 5), (9, 10, 2), (9, 10, 8)]

ovire2 = [(1, 3, 6), (2, 4, 3), (4, 6, 7),
          (3, 4, 9), (9, 10, 2), (9, 10, 8)]

ovire3 = [(1, 3, 6), (2, 4, 3),
          (3, 4, 9), (9, 10, 2), (9, 10, 8)]


class TestOneLineMixin:
    functions = {
        elm.name: elm
        for elm in ast.parse(open(__file__, "r", encoding = "utf-8").read()).body
        if isinstance(elm, ast.FunctionDef)}

    def assert_is_one_line(self, func):
        body = self.functions[func.__code__.co_name].body
        self.assertEqual(len(body), 1, "\nFunkcija ni dolga le eno vrstico")
        self.assertIsInstance(body[0], ast.Return, "\nFunkcija naj bi vsebovala le return")

    def test_nedovoljene_funkcije(self):
        dovoljene_funkcije = {
            "stevilo_ovir", "dolzina_ovir", "sirina", "pretvori_vrstico", "dodaj_vrstico",
            "pretvori_zemljevid", "globina", "naj_stolpec", "senca", "indeksi"}
        for func in self.functions:
            self.assertIn(func, dovoljene_funkcije, f"\nFunkcija {func} ni dovoljena.")


class Test01Obvezna(unittest.TestCase, TestOneLineMixin):
    def test_01_stevilo_ovir(self):
        self.assertEqual(7, stevilo_ovir(ovire1))
        self.assertEqual(6, stevilo_ovir(ovire2))
        self.assertEqual(0, stevilo_ovir([]))

        self.assert_is_one_line(stevilo_ovir)

    def test_02_dolzina_ovir(self):
        self.assertEqual(19, dolzina_ovir(ovire1))
        self.assertEqual(15, dolzina_ovir(ovire2))
        self.assertEqual(0, dolzina_ovir([]))

        self.assert_is_one_line(dolzina_ovir)

    def test_03_sirina(self):
        self.assertEqual(10, sirina(ovire1))
        self.assertEqual(9, sirina(ovire1[:-2]))
        self.assertEqual(6, sirina(ovire1[:-3]))
        self.assertEqual(3, sirina(ovire1[:1]))

        self.assert_is_one_line(sirina)

    def test_04_dodaj_vrstico(self):
        self.assertEqual([(3, 4, 3), (6, 8, 3), (11, 11, 3)], dodaj_vrstico([(3, 4), (6, 8), (11, 11)], 3))

        self.assert_is_one_line(dodaj_vrstico)

    def test_05_globina(self):
        self.assertEqual(3, globina(ovire1, 3))
        self.assertEqual(5, globina(ovire1, 6))
        self.assertEqual(7, globina(ovire2, 6))
        self.assertIsNone(globina(ovire3, 6))

        self.assert_is_one_line(globina)

    def test_06_senca(self):
        self.assertEqual([False] * 10, senca(ovire1))
        self.assertEqual([False, False, False, False, False, False, True, True, False, False], senca(ovire2))
        self.assertEqual([False, False, False, False, True, True, True, True, False, False], senca(ovire3))
        self.assertEqual([False] * 6, senca(ovire2[:-3]))
        self.assertEqual([False] * 3, senca(ovire3[:1]))

        self.assert_is_one_line(senca)


class Test02Dodatna(unittest.TestCase, TestOneLineMixin):
    def test_01_indeksi(self):
        self.assertEqual([3, 10, 15, 17], indeksi("prepelica peče pepelko", "pe"))
        self.assertEqual([0, 2, 8, 16], indeksi("pepelka peče prepelico", "pe"))
        self.assertEqual([0, 2], indeksi("peperutka", "pe"))
        self.assertEqual([0], indeksi("peperutka", "pepe"))
        self.assertEqual([8], indeksi("peperutka", "a"))
        self.assertEqual([0, 3, 10, 15, 17], indeksi("prepelica peče pepelko", "p"))
        self.assertEqual([], indeksi("prepelica peče pepelko", "m"))

        self.assert_is_one_line(indeksi)

    def test_02_pretvori_vrstico(self):
        self.assertEqual([(3, 5)], pretvori_vrstico("..###."))
        self.assertEqual([(3, 5), (7, 7)], pretvori_vrstico("..###.#."))
        self.assertEqual([(1, 2), (5, 7), (9, 9)], pretvori_vrstico("##..###.#."))
        self.assertEqual([(1, 1), (4, 6), (8, 8)], pretvori_vrstico("#..###.#."))
        self.assertEqual([(1, 1), (4, 6), (8, 8)], pretvori_vrstico("#..###.#"))
        self.assertEqual([], pretvori_vrstico("..."))
        self.assertEqual([], pretvori_vrstico(".."))
        self.assertEqual([], pretvori_vrstico("."))

        self.assert_is_one_line(pretvori_vrstico)


class Test03Ekstra(unittest.TestCase, TestOneLineMixin):
    def test_01_pretvori_zemljevid(self):
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

        self.assert_is_one_line(pretvori_zemljevid)

    def test_02_naj_stolpec(self):
        self.assertEqual((5, 7), naj_stolpec(ovire1))
        self.assertEqual((7, None), naj_stolpec(ovire2))
        self.assertEqual((5, None), naj_stolpec(ovire3))

        self.assert_is_one_line(naj_stolpec)


if __name__ == "__main__":
    unittest.main()
