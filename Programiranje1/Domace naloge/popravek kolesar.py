import numpy as np

def kolesar():
    ovire = [
        (1, 3, 6),
        (2, 4, 3),
        (4, 6, 7),
        (3, 4, 9),
        (6, 9, 5),
        (9, 10, 2),
        (9, 10, 8)
    ]
    # 1. zacetna naloga
    yline = []

    start = 6
    konec = 0

    for x1, x2, y in ovire:
        if x1 <= start <= x2:
            yline.append(y)
            yline.sort()
    konec = yline[0]
    print(konec)

    # 2. Dodatna naloga
    sirina_steze = 0
    for x1, x2, y in ovire:
        for xx1, xx2, yy in ovire:
            if x2 < xx2:
                sirina_steze = xx2
    print('Kolesarskia steza je siroka', sirina_steze, 'polj.')
    i = 0

kolesar()
