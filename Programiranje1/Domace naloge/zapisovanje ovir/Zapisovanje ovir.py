import os
import warnings
from random import randint
from datetime import datetime
import unittest


















def zapisi_ovire(ime_datoteke, ovire):
    with open(ime_datoteke, 'w') as datoteka:
        for vrstica, ovire_vrstice in ovire.items():
            datoteka.write(f"{vrstica:03d}: {' '.join([f'{zacetek:>3}-{konec:<4}' for zacetek, konec in ovire_vrstice])}\n")



















class TestZapis(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)

        self.ovire = {4: [(5, 6), (9, 11)],
                      5: [(9, 11), (19, 20), (30, 34)],
                      13: [(5, 8), (9, 11), (17, 19), (22, 25), (90, 100)]}

        self.ovire2 = self.ovire | {randint(100, 200): [(1, 2)]}
        with open("ovire.txt", "wt") as f:
            lf = "\n"
            f.write("\n\n".join(fr"{y}{lf}{lf.join(fr'{x0}{lf}{x1}' for x0, x1 in xs)}" for y, xs in self.ovire2.items()))

    def test_01_obvezna_zapisi_ovire(self):
        ime_datoteke = f"ovire{datetime.now().strftime('%m-%d-%H-%M-%S')}.txt"
        zapisi_ovire(ime_datoteke, self.ovire)
        with open(ime_datoteke) as f:
            self.assertEqual("""
004:   5-6      9-11
005:   9-11    19-20    30-34
013:   5-8      9-11    17-19    22-25    90-100
""".strip("\n"), "\n".join(map(str.rstrip, f)))

        self.ovire[101] = self.ovire[5]
        zapisi_ovire(ime_datoteke, self.ovire)
        with open(ime_datoteke) as f:
            self.assertEqual("""
004:   5-6      9-11
005:   9-11    19-20    30-34
013:   5-8      9-11    17-19    22-25    90-100
101:   9-11    19-20    30-34
""".strip("\n"), "\n".join(map(str.rstrip, f)))

        os.remove(ime_datoteke)

    def test_02_dodatna_preberi_ovire(self):
        self.assertEqual(preberi_ovire("ovire.txt"), self.ovire2)


if __name__ == "__main__":
    unittest.main()