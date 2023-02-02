from operator import itemgetter


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

    iskanje_dodatna = int(input('Vstavite zeljeno startno pozicijo:'))

    start = 6

    razdaljay = []
    dodatna_naloga_rezultat = []

    ovire.sort(key=itemgetter(2))

    # 1. del naloge 'iskanje dolzino y osi kjer se bo kolesar zabil
    for i in ovire:
        if i[0] <= start <= i[1]:
            razdaljay.append(i[2])
            if len(razdaljay) == 1:
                break

    # 2. del naloge
    for d in ovire:
        if d[0] <= iskanje_dodatna <= d[1]:
            dodatna_naloga_rezultat.append(d[1])
            dodatna_naloga_rezultat.append(d[2])

            if len(dodatna_naloga_rezultat) == 2:
                break

    print('Prekolesarli ste', int(razdaljay[0]), 'polj preden ste si polomili noge!!!')
    print('Nevem kaj se dogaja???', int(dodatna_naloga_rezultat[0]), int(dodatna_naloga_rezultat[1]), 'Ali je to prau?')

kolesar()
