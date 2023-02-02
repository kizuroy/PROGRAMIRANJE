import unittest


def vrstica(s):
    konec = []
    s, stevila = s.split(':')
    stevila = stevila.replace('-', ',').strip().split(', ')

    for kaj in stevila:
        novastevila = kaj + ',' + s
        novastevila = novastevila.split(',')

        novastevila = map(int, novastevila)
        konec.append(tuple(novastevila))

    return konec


def preberi(s):
    tabela = []

    for i in s.splitlines():
        tabela.extend(vrstica(i))

    return tabela


def intervali(xs):
    nova = []
    for i in xs:
        a = str(i).replace(', ', '-').strip('(').strip(')')
        nova.append(a)
    return nova


def zapisi_vrstico(y, xs):
    y = str(y) + ':'
    a = ''

    for i in xs:
        dodajanje = str(i)
        dodajanje = dodajanje.replace(',', '-').replace(' ', '').strip('()') + ','
        a += dodajanje
    zdruzenje = y + ' ' + a.strip(',').replace(',', ', ')

    return zdruzenje


class Obvezna(unittest.TestCase):
    def test_vrstica(self):
        self.assertEqual([(1, 3, 4), (5, 11, 4), (15, 33, 4)], vrstica("4: 1-3, 5-11, 15-33"))
        self.assertEqual([(989, 1300, 1234)], vrstica("1234: 989-1300"))

    def test_preberi(self):
        self.assertEqual([(5, 6, 4),
                          (90, 100, 13), (5, 8, 13), (9, 11, 13),
                          (9, 11, 5), (19, 20, 5), (30, 34, 5),
                          (9, 11, 4),
                          (22, 25, 13), (17, 19, 13)], preberi(
            """4: 5-6
13: 90-100, 5-8, 9-11
5: 9-11, 19-20, 30-34
4: 9-11
13:  22-25, 17-19
"""))

    def test_intervali(self):
        self.assertEqual(["6-10", "12-16", "20-22", "98-102"], intervali([(6, 10), (12, 16), (20, 22), (98, 102)]))

    def test_zapisi_vrstico(self):
        self.assertEqual("5: 6-10, 12-16", zapisi_vrstico(5, [(6, 10), (12, 16)]).rstrip("\n"))
        self.assertEqual("8: 6-10, 12-16, 20-22, 98-102",
                         zapisi_vrstico(8, [(6, 10), (12, 16), (20, 22), (98, 102)]).rstrip("\n"))
        self.assertEqual("8: 6-10, 12-16, 20-22, 98-102",
                         zapisi_vrstico(8, [(6, 10), (12, 16), (20, 22), (98, 102)]).rstrip("\n"))


class Dodatna(unittest.TestCase):
    def test_zapisi(self):
        ovire = [(5, 6, 4),
                 (90, 100, 13), (5, 8, 13), (9, 11, 13),
                 (9, 11, 5), (19, 20, 5), (30, 34, 5),
                 (9, 11, 4),
                 (22, 25, 13), (17, 19, 13)]
        kopija_ovir = ovire.copy()
        self.assertEqual("""4: 5-6, 9-11
5: 9-11, 19-20, 30-34
13: 5-8, 9-11, 17-19, 22-25, 90-100""", zapisi(ovire).rstrip("\n"))
        self.assertEqual(ovire, kopija_ovir)


if __name__ == "__main__":
    unittest.main()
