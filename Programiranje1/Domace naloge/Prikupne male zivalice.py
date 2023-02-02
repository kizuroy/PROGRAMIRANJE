ovire = [(1, 1, 3), (1, 5, 6), (1, 8, 8), (1, 10, 10),
         (2, 5, 6), (2, 13, 16),
         (4, 9, 11), (4, 13, 14),
         (5, 1, 3), (5, 15, 17),
         (6, 5, 6), (6, 8, 9),
         (7, 12, 13),
         (8, 10, 10),
         (9, 1, 2), (9, 14, 16),
         (10, 4, 4), (10, 12, 12),
         (11, 17, 17),
         (12, 13, 15),
         (13, 1, 5), (13, 7, 11), (13, 17, 17),
         (14, 16, 16),
         (15, 3, 4), (15, 10, 11),
         (16, 15, 15),
         (17, 2, 3), (17, 5, 9), (17, 11, 13), (17, 16, 16)]



def mozen_skok(x, y, ovira):
  y1, x0, x1 = ovira
  return abs(y - y1) <= 2 and (x0 <= x + 1 <= x1 or abs(y - y1) == 1 and x0 <= x + 2 <= x1 or abs(y - y1) == 0 and x0 <= x + 2 <= x1)


def mozne_ovire(x, y):
  return [ovira for ovira in ovire if mozen_skok(x, y, ovira)]


def obstaja_pot(ovira):
    y, x0, x1 = ovira
    print(mozne_ovire(x1,y))

    if len(mozne_ovire(x1, y)) == 0:
        konec = (y, 18, 18)
        if mozen_skok(x1, y, (konec)):
            return True
        else:
            False
    
    
    

    









import unittest


class TestObvezna(unittest.TestCase):
    def test_01_mozen_skok(self):
        for yk, xs in [(8, ((13, 16), (14, 16), (15, 16), (16, 16),
                            (13, 17), (14, 17), (15, 17), (16, 17), (16, 18), (16, 19),
                            (14, 18), (15, 18), (16, 18), (16, 19), (16, 20),
                            (15, 16), (15, 17), (15, 18), (15, 19),
                            (16, 16), (16, 17), (16, 18), (16, 19))),
                       (9, ((13, 16), (14, 16), (15, 16), (16, 16),
                            (13, 17), (14, 17), (15, 17), (16, 17), (16, 18), (16, 19),
                            (14, 18), (15, 18), (16, 18), (17, 19), (17, 20), (17, 21),
                            (15, 16), (15, 17), (15, 18), (15, 19),
                            (16, 16), (16, 17), (16, 18), (16, 19),
                            (17, 17), (17, 18), (17, 18))),
                       (10, ((17, 17), (17, 18), (17, 19), (17, 20))),
                      ]:
            for y in (yk, 20 - yk):
                for x0, x1 in xs:
                    self.assertTrue(mozen_skok(15, 10, (y, x0, x1)),
                                    f"Skok z (15, 10) na ({y}, {x0}, {x1}) je možen, funkcija pa pravi, da ni.")

        for yk, xs in [(7, ((13, 16), (14, 16), (15, 16), (16, 16),
                            (13, 17), (14, 17), (15, 17), (16, 17), (16, 18), (16, 19),
                            (14, 18), (15, 18), (16, 18), (16, 19), (16, 20),
                            (15, 16), (15, 17), (15, 18), (15, 19),
                            (16, 16), (16, 17), (16, 18), (16, 19))),
                       (8, ((17, 17), (17, 18), (17, 19), (17, 20), (17, 21))),
                       (9, ((13, 15), (14, 15), (15, 15),
                            (18, 18), (18, 19), (18, 20))),
                       (10, ((18, 18), (18, 19), (18, 20))),
                      ]:
            for y in (yk, 20 - yk):
                for x0, x1 in xs:
                    self.assertFalse(mozen_skok(15, 10, (y, x0, x1)),
                                    f"Skok z (15, 10) na ({y}, {x0}, {x1}) ni možen, funkcija pa pravi, da je.")

    def test_02_mozne_ovire(self):
        self.assertEqual({(13, 7, 11), (17, 5, 9), (15, 10, 11)}, set(mozne_ovire(8, 15)))
        self.assertEqual({(4, 13, 14), (7, 12, 13)}, set(mozne_ovire(12, 6)))
        self.assertEqual({(5, 1, 3)}, set(mozne_ovire(2, 7)))
        self.assertEqual({(5, 1, 3)}, set(mozne_ovire(2, 6)))
        self.assertEqual({(13, 17, 17), (11, 17, 17)}, set(mozne_ovire(16, 12)))
        self.assertEqual(set(), set(mozne_ovire(6, 3)))

    def test_03_obstaja_pot(self):
        self.assertTrue(obstaja_pot((2, 13, 16)))
        self.assertTrue(obstaja_pot((4, 13, 14)))
        self.assertTrue(obstaja_pot((6, 8, 9)))
        self.assertTrue(obstaja_pot((5, 1, 3)))

        self.assertTrue(obstaja_pot((13, 1, 5)))

        self.assertTrue(obstaja_pot((17, 2, 3)))

        self.assertFalse(obstaja_pot((1, 1, 3)))
        self.assertFalse(obstaja_pot((0, 1, 2)))


# class TestDodatna(unittest.TestCase):
#     def test_01_stevilo_poti(self):
#         self.assertEqual(2, stevilo_poti((4, 13, 14)))
#         self.assertEqual(4, stevilo_poti((5, 1, 3)))
#         self.assertEqual(4, stevilo_poti((13, 1, 5)))
#         self.assertEqual(0, stevilo_poti((9, 1, 2)))
#         self.assertEqual(16, stevilo_poti((17, 2, 3)))


if __name__ == "__main__":
    unittest.main()