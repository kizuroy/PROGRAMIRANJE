from collections import defaultdict


def vsebovanost(krogi):
    vsebuje = defaultdict(list)
    notranji = set()

    for krog0 in krogi:
        for krog1 in krogi:
            x0, y0, r0 = krog0
            x1, y1, r1 = krog1
            if r0 > r1 and (x1 - x0) ** 2 + (y1 - y0) ** 2 < r0 ** 2:
                vsebuje[krog0].append(krog1)
                notranji.add(krog1)

    return vsebuje, notranji


def letala(krogi):
    vsebuje, notranji = vsebovanost(krogi)
    letala = set()
    for krog, vkrogu in vsebuje.items():
        if krog in notranji or len(vkrogu) == 1:
            continue
        for vkrog in vkrogu:
            if vkrog in vsebuje:
                break
        else:
            letala.add(krog)
    return letala



def najvec_oken(krogi):
    vsebuje, _, = vsebovanost(krogi)
    vsa_letala = letala(krogi)
    if not vsa_letala:
        return None
    
    naj_oken = max(len(vsebuje[krog]) for krog in vsa_letala)
    naj_letala = [krog for krog in vsa_letala if len(vsebuje[krog]) == naj_oken]
    
    if len(naj_letala) != 1:
        return None
    return naj_letala[0][:2]


def stevilo_oken(krog, hierarhija):
    if krog not in hierarhija:
        return 1
    return sum(stevilo_oken(podkrog, hierarhija) for podkrog in hierarhija[krog])
    
        

def pari(krogi, razdalje):
    krogi = set(krogi)
    pari = []
    for r, par in razdalje:
        if par <= krogi:
           pari.append(par)
           krogi -= par
    return pari



def prepisi_koordinate(vhodna, izhodna):
    podatki = open(vhodna).read().strip()
    open(izhodna, "wt").write("\n".join(
        " ".join(f"{int(podatki[i:i+3]):3}"
                 for i in range(vrsta, vrsta + 9, 3))
        for vrsta in range(0, len(podatki), 9)))




class Strelec:
    def __init__(self):
        self.odaljeno = set()
    
    def dodeli(self, krog):
        self.dodeljeno.add(krog)
    
    def strel(self, x, y):
        prej = self.preostalih()
        self.dodeljeno = {(x0, y0, r0) for x0, y0, r0 in self.dodeljeno
                          if (x - x0) ** 2 + (y - y0) ** 2 > r0 ** 2}
        return self.preostalih() != prej

    def preostalih(self):
        return len(self.dodeljeno)



import unittest

class Test(unittest.TestCase):
    def test_najvec_oken(self):
        krogi = [
            (164.4, 136.8, 50.8),
            (59.2, 182.8, 50.8),
            (282.8, 71.5, 45.6),
            (391, 229.4, 58.4),
            (259.9, 186, 47.6),
            (428, 89, 63.2),
            (88.6, 44.3, 37.5),
            (371.6, 233.6, 10.6),
            (408.7, 210.5, 8.9),
            (398.1, 95.5, 13),
            (449.5, 99.6, 13.6),
            (455.4, 66.5, 12.4),
            (139.6, 138, 10.6),
            (185, 138, 10.6),
            (69.8, 46.5, 10.6),
            (267.4, 51.7, 17.2),
            (225.8, 187.3, 7.5),
            (242.8, 187.3, 7.5),
            (259.8, 187.3, 7.5),
            (276.7, 187.3, 7.5),
            (293.7, 187.3, 7.5),
            (267.4, 51.7, 10.6),
            (99.6, 43.1, 17.2),
            (99.6, 43.1, 10.6),
            (150.3, 245.5, 50.8),
            (144.3, 243.6, 38.8),
            (127.3, 245.5, 7.5),
            (161.3, 245.5, 7.5)]

        # Letalo s 5 krogi
        self.assertEqual((259.9, 186), najvec_oken(krogi))

        # Odstranimo tega, največ jih ima oni s tremi
        krogi.remove((259.9, 186, 47.6))
        self.assertEqual((428, 89), najvec_oken(krogi))

        # Odstranimo onega s tremi krogi
        krogi.remove((428, 89, 63.2))
        self.assertIsNone(najvec_oken(krogi))

        # Nazaj onega s tremi, dodamo še enega s tremi
        krogi.append((428, 89, 63.2))

        krogi.append((1000, 1000, 100))
        krogi.append((1010, 1010, 10))
        krogi.append((1020, 1020, 10))
        krogi.append((1030, 1030, 10))
        self.assertIsNone(najvec_oken(krogi))

        krogi.append((2000, 2000, 100))
        krogi.append((2010, 2010, 10))
        krogi.append((2020, 2020, 10))
        krogi.append((2030, 2030, 10))
        self.assertIsNone(najvec_oken(krogi))

        # Vrnemo onega s tremi
        krogi.append((259.9, 186, 47.6))
        self.assertEqual((259.9, 186), najvec_oken(krogi))

    def test_stevilo_oken(self):
        noter = {(0, 0, 10): [(5, 0, 5), (-5, 0, 5)],
                 (-5, 0, 5): [(-8, 0, 2), (-2, 0, 2)],
                 (-2, 0, 2): [(-2, 0, 1)]}
        self.assertEqual(3, stevilo_oken((0, 0, 10), noter))
        self.assertEqual(2, stevilo_oken((-5, 0, 5), noter))
        self.assertEqual(1, stevilo_oken((5, 0, 5), noter))

    def test_pari(self):
        from math import sqrt

        # Imamo takšne kroge
        krogi = [(2, 11, 1), (3.5, 8.5, 0.5), (4, 4, 1), (9, 9, 2), (12.5, 12.5, 0.5), (13, 4, 3)]

        # Izračunamo urejen seznam parov, predstavljenih s trojkami
        # (razdalja, {(x0, y0), (x1, y1)})
        razdalje = sorted(
            (sqrt((x0 - x1) ** 2 + (y0 - y1) ** 2) - r0 - r1, {(x0, y0), (x1, y1)})
            for x0, y0, r0 in krogi for x1, y1, r1 in krogi
            if (x0, y0, r0) < (x1, y1, r1)
        )
        # Pripravimo seznam središč krogov
        sredisca = [krog[:2] for krog in krogi]

        # Funkcija prejme središča (brez polmerov!) in urejen seznam razdalij
        self.assertEqual([{(9, 9), (13, 4)}, {(2, 11), (3.5, 8.5)}, {(4, 4), (12.5, 12.5)}],
                         pari(sredisca, razdalje))
        
        krogi = [(2, 11, 1), (3.5, 8.5, 0.5), (4, 4, 1), (9, 9, 2), (12.5, 12.5, 0.5), (13, 4, 3), (100, 100, 2)]
        razdalje = sorted(
            (sqrt((x0 - x1) ** 2 + (y0 - y1) ** 2) - r0 - r1, {(x0, y0), (x1, y1)})
            for x0, y0, r0 in krogi for x1, y1, r1 in krogi
            if (x0, y0, r0) < (x1, y1, r1)
        )
        sredisca = [krog[:2] for krog in krogi]

        self.assertEqual([{(9, 9), (13, 4)}, {(2, 11), (3.5, 8.5)}, {(4, 4), (12.5, 12.5)}],
                         pari(sredisca, razdalje))



    def test_prepisi_koordinate(self):
        open("krogi.txt", "wt").write("150023038512418012001000123123011005")
        prepisi_koordinate("krogi.txt", "rezultat.txt")
        self.assertEqual("""
150  23  38
512 418  12
  1   0 123
123  11   5""".strip(), open("rezultat.txt").read().strip())

    def test_strelec(self):
        s = Strelec()

        self.assertEqual(0, s.preostalih())

        s.dodeli((9, 9, 3))
        self.assertEqual(1, s.preostalih())
        s.strel(11.8, 11.8)
        self.assertEqual(1, s.preostalih())

        s.strel(11, 11)
        self.assertEqual(0, s.preostalih())

        s.dodeli((9, 9, 3))
        s.dodeli((4, 4, 1))
        self.assertEqual(2, s.preostalih())

        s.dodeli((13, 4, 3))
        s.dodeli((16, 4, 3))
        s.dodeli((14, 4, 1))
        self.assertEqual(5, s.preostalih())

        s.strel(4.5, 4.5)
        self.assertEqual(4, s.preostalih())

        s.strel(14, 4)
        self.assertEqual(1, s.preostalih())


if __name__ == "__main__":
    unittest.main()