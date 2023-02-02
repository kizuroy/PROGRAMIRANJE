import unittest


def po_vrstah(vrt):
    return [sum(i) for i in vrt]


def najboljsi(vrt):
    return [max(i) for i in vrt]


def diagonala(vrt):
    return sum(vrt[i][i] for i in range(min(len(vrt), len(vrt[0]))))


def je_palindromen(vrt):
    return all(vrsta == vrsta[::-1] for vrsta in vrt)


def preberi_vrt(ime_dat):
    return [[int(x) for x in vrsta.split(",")] for vrsta in open(ime_dat)]


def palindromne(vrt):
    return [vrsta for vrsta in vrt if vrsta == vrsta[::-1]]


def prastevilski(vrt):
    return [[x if prastevilo(x) else 0 for x in vrsta] for vrsta in vrt]


def povsod_0(vrt):
    return all(any(x == 0 for x in vrsta) for vrsta in vrt)


def vedno_vec_ali_manj(vrt):
    return all(sum(x) <= sum(y) for x, y in zip(vrt, vrt[1:])) or \
           all(sum(x) >= sum(y) for x, y in zip(vrt, vrt[1:]))


def prastevilo(n):
    return all(n % i != 0 for i in range(2, n))


class TestStatistika(unittest.TestCase):
    vrt = [[1, 3, 3, 8, 5, 4, 2, 1, 5, 6],
           [2, 4, 3, 3, 6, 8, 1, 3, 5, 6],
           [4, 5, 6, 4, 7, 4, 3, 6, 4, 7],
           [2, 8, 7, 0, 0, 7, 4, 7, 8, 0],
           [2, 3, 4, 7, 0, 8, 7, 6, 3, 8],
           [3, 7, 9, 0, 8, 5, 3, 2, 3, 4],
           [1, 5, 7, 7, 6, 4, 2, 3, 5, 6],
           [0, 6, 3, 3, 6, 8, 0, 6, 7, 7],
           [0, 1, 3, 2, 8, 0, 0, 0, 0, 0],
           [3, 1, 0, 3, 6, 7, 0, 5, 3, 1],
           [1, 3, 5, 7, 0, 8, 6, 5, 3, 1],
           [3, 6, 3, 1, 3, 5, 8, 7, 5, 1],
           [4, 3, 6, 0, 0, 8, 4, 7, 5, 3],
           [3, 5, 6, 8, 6, 3, 1, 3, 5, 2]]

    vrt2 = [[1, 2, 4, 2, 2, 3, 1, 0, 0, 3, 1, 3, 4, 3],
            [3, 4, 5, 8, 3, 7, 5, 6, 1, 1, 3, 6, 3, 5],
            [3, 3, 6, 7, 4, 9, 7, 3, 3, 0, 5, 3, 6, 6],
            [8, 3, 4, 0, 7, 0, 7, 3, 2, 3, 7, 1, 0, 8],
            [5, 6, 7, 0, 0, 8, 6, 6, 8, 6, 0, 3, 0, 6],
            [4, 8, 4, 7, 8, 5, 4, 8, 0, 7, 8, 5, 8, 3],
            [2, 1, 3, 4, 7, 3, 2, 0, 0, 0, 6, 8, 4, 1],
            [1, 3, 6, 7, 6, 2, 3, 6, 0, 5, 5, 7, 7, 3],
            [5, 5, 4, 8, 3, 3, 5, 7, 0, 3, 3, 5, 5, 5],
            [6, 6, 7, 0, 8, 4, 6, 7, 0, 1, 1, 1, 3, 2]]

    vrt0 = [[42]]
    vrt_x = [[1, 2, 3, 5, 4]]
    vrt_y = [[1], [2], [3], [5], [4]]

    vrt_pal = [[3, 6, 7, 6, 3],
               [5, 5, 5, 5, 5],
               [5, 1, 1, 1, 5],
               [2, 3, 4, 3, 2]]

    vrt_pat = [[3, 6, 7, 6, 3],
               [5, 5, 5, 5, 5],
               [5, 1, 1, 9, 5],
               [2, 3, 4, 3, 2],
               [2, 3, 4, 3, 0]]

    vrt_pov0 = [[0, 6, 7, 6, 3],
                [5, 5, 5, 0, 5],
                [5, 0, 1, 9, 5],
                [2, 3, 4, 3, 0]]

    def test_po_vrstah(self):
        self.assertEqual(
            po_vrstah(self.vrt),
            [38, 41, 50, 43, 48, 44, 46, 46, 14, 29, 39, 42, 40, 42])
        self.assertEqual(
            po_vrstah(self.vrt2), [29, 60, 65, 53, 61, 79, 41, 61, 61, 52])
        self.assertEqual(po_vrstah(self.vrt0), [42])
        self.assertEqual(po_vrstah(self.vrt_x), [15])
        self.assertEqual(po_vrstah(self.vrt_y), [x[0] for x in self.vrt_y])

    def test_najboljsi(self):
        self.assertEqual(
            najboljsi(self.vrt), [8, 8, 7, 8, 8, 9, 7, 8, 8, 7, 8, 8, 8, 8])
        self.assertEqual(
            najboljsi(self.vrt2), [4, 8, 9, 8, 8, 8, 8, 7, 8, 8])
        self.assertEqual(najboljsi(self.vrt0), [42])
        self.assertEqual(najboljsi(self.vrt_x), [5])
        self.assertEqual(najboljsi(self.vrt_y), [x[0] for x in self.vrt_y])

    def test_diagonala(self):
        self.assertEqual(diagonala(self.vrt), 25)
        self.assertEqual(diagonala(self.vrt2), 25)
        self.assertEqual(diagonala(self.vrt0), 42)
        self.assertEqual(diagonala(self.vrt_x), 1)
        self.assertEqual(diagonala(self.vrt_y), 1)

    def test_je_palindromen(self):
        self.assertFalse(je_palindromen(self.vrt))
        self.assertFalse(je_palindromen(self.vrt2))
        self.assertTrue(je_palindromen(self.vrt0))
        self.assertFalse(je_palindromen(self.vrt_x))
        self.assertTrue(je_palindromen(self.vrt_y))
        self.assertTrue(je_palindromen(self.vrt_pal))
        self.assertFalse(je_palindromen(self.vrt_pat))

    def test_palindromne(self):
        self.assertEqual(palindromne(self.vrt), [])
        self.assertEqual(palindromne(self.vrt2), [])
        self.assertEqual(palindromne(self.vrt0), [[42]])
        self.assertEqual(palindromne(self.vrt_x), [])
        self.assertEqual(palindromne(self.vrt_y), self.vrt_y)
        self.assertEqual(palindromne(self.vrt_pal), self.vrt_pal)
        self.assertEqual(
            palindromne(self.vrt_pat),
            [[3, 6, 7, 6, 3], [5, 5, 5, 5, 5], [2, 3, 4, 3, 2]])

    def test_preberi_vrt(self):
        self.assertEqual(preberi_vrt("vrt.txt"), self.vrt)
        self.assertEqual(preberi_vrt("vrt0.txt"), self.vrt0)
        self.assertEqual(preberi_vrt("vrt_x.txt"), self.vrt_x)
        self.assertEqual(preberi_vrt("vrt_y.txt"), self.vrt_y)

    def test_prastevilski(self):
        self.assertEqual(prastevilski(self.vrt),
                         [[1, 3, 3, 0, 5, 0, 2, 1, 5, 0],
                          [2, 0, 3, 3, 0, 0, 1, 3, 5, 0],
                          [0, 5, 0, 0, 7, 0, 3, 0, 0, 7],
                          [2, 0, 7, 0, 0, 7, 0, 7, 0, 0],
                          [2, 3, 0, 7, 0, 0, 7, 0, 3, 0],
                          [3, 7, 0, 0, 0, 5, 3, 2, 3, 0],
                          [1, 5, 7, 7, 0, 0, 2, 3, 5, 0],
                          [0, 0, 3, 3, 0, 0, 0, 0, 7, 7],
                          [0, 1, 3, 2, 0, 0, 0, 0, 0, 0],
                          [3, 1, 0, 3, 0, 7, 0, 5, 3, 1],
                          [1, 3, 5, 7, 0, 0, 0, 5, 3, 1],
                          [3, 0, 3, 1, 3, 5, 0, 7, 5, 1],
                          [0, 3, 0, 0, 0, 0, 0, 7, 5, 3],
                          [3, 5, 0, 0, 0, 3, 1, 3, 5, 2]])

        self.assertEqual(self.vrt,
                         [[1, 3, 3, 8, 5, 4, 2, 1, 5, 6],
                          [2, 4, 3, 3, 6, 8, 1, 3, 5, 6],
                          [4, 5, 6, 4, 7, 4, 3, 6, 4, 7],
                          [2, 8, 7, 0, 0, 7, 4, 7, 8, 0],
                          [2, 3, 4, 7, 0, 8, 7, 6, 3, 8],
                          [3, 7, 9, 0, 8, 5, 3, 2, 3, 4],
                          [1, 5, 7, 7, 6, 4, 2, 3, 5, 6],
                          [0, 6, 3, 3, 6, 8, 0, 6, 7, 7],
                          [0, 1, 3, 2, 8, 0, 0, 0, 0, 0],
                          [3, 1, 0, 3, 6, 7, 0, 5, 3, 1],
                          [1, 3, 5, 7, 0, 8, 6, 5, 3, 1],
                          [3, 6, 3, 1, 3, 5, 8, 7, 5, 1],
                          [4, 3, 6, 0, 0, 8, 4, 7, 5, 3],
                          [3, 5, 6, 8, 6, 3, 1, 3, 5, 2]],
                         "Kremplje stran od vrta, ki ga dobite kot argument!")

        self.assertEqual(prastevilski([[42]]), [[0]])
        self.assertEqual(prastevilski([[43]]), [[43]])
        self.assertEqual(prastevilski(self.vrt_x), [[1, 2, 3, 5, 0]])
        self.assertEqual(prastevilski(self.vrt_y), [[1], [2], [3], [5], [0]])

    def test_vrazevernikus(self):
        self.assertEqual(vrazevernikus(self.vrt), 263)
        self.assertEqual(vrazevernikus(self.vrt0), 42)
        self.assertEqual(vrazevernikus(self.vrt_x), 4)
        self.assertEqual(vrazevernikus(self.vrt_y), 4)
        self.assertEqual(vrazevernikus(self.vrt_pal), 16)

    def test_povsod_0(self):
        self.assertFalse(povsod_0(self.vrt))
        self.assertFalse(povsod_0(self.vrt2))
        self.assertFalse(povsod_0(self.vrt0))
        self.assertFalse(povsod_0(self.vrt_x))
        self.assertFalse(povsod_0(self.vrt_y))
        self.assertFalse(povsod_0(self.vrt_pal))
        self.assertFalse(povsod_0(self.vrt_pat))
        self.assertTrue(povsod_0(self.vrt_pov0))
        self.assertTrue(povsod_0([[0]]))
        self.assertTrue(povsod_0([[0] * 5]))
        self.assertTrue(povsod_0([[0]] * 5))

    def test_vedno_vec(self):
        self.assertFalse(vedno_vec(self.vrt))
        self.assertTrue(vedno_vec(sorted(self.vrt, key = sum)))
        self.assertFalse(vedno_vec(self.vrt2))
        self.assertTrue(vedno_vec(sorted(self.vrt2, key = sum)))
        self.assertTrue(vedno_vec(self.vrt0))
        self.assertTrue(vedno_vec(self.vrt_x))
        self.assertFalse(vedno_vec(self.vrt_y))
        self.assertTrue(vedno_vec(sorted(self.vrt_y, key = sum)))
        self.assertFalse(vedno_vec(self.vrt_pal))
        self.assertTrue(vedno_vec(sorted(self.vrt_pal, key = sum)))
        self.assertFalse(vedno_vec(self.vrt_pat))
        self.assertTrue(vedno_vec(sorted(self.vrt_pat, key = sum)))
        self.assertTrue(vedno_vec([[0]] * 5))

    def test_vedno_vec_ali_manj(self):
        self.assertFalse(vedno_vec_ali_manj(self.vrt))
        self.assertTrue(vedno_vec_ali_manj(sorted(self.vrt, key = sum)))
        self.assertTrue(vedno_vec_ali_manj(sorted(self.vrt, key = sum, reverse = True)))
        self.assertFalse(vedno_vec_ali_manj(self.vrt2))
        self.assertTrue(vedno_vec_ali_manj(sorted(self.vrt2, key = sum)))
        self.assertTrue(vedno_vec_ali_manj(sorted(self.vrt2, key = sum, reverse = True)))
        self.assertTrue(vedno_vec_ali_manj(self.vrt0))
        self.assertTrue(vedno_vec_ali_manj(self.vrt_x))
        self.assertFalse(vedno_vec_ali_manj(self.vrt_y))
        self.assertTrue(vedno_vec_ali_manj(sorted(self.vrt_y, key = sum)))
        self.assertTrue(vedno_vec_ali_manj(sorted(self.vrt_y, key = sum, reverse = True)))
        self.assertTrue(vedno_vec_ali_manj(sorted(self.vrt_pal, key = sum)))
        self.assertTrue(vedno_vec_ali_manj(sorted(self.vrt_pal, key = sum, reverse = True)))
        self.assertTrue(vedno_vec_ali_manj(sorted(self.vrt_pat, key = sum)))
        self.assertTrue(vedno_vec_ali_manj(sorted(self.vrt_pat, key = sum, reverse = True)))
        self.assertTrue(povsod_0([[0]] * 5))
