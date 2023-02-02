import random
import risar

# Ovire se shranjujejo v seznam
ovire = []

# Določi širino ovire med 30 in 80
sirina = random.randint(30, 80)

# Določi položaj ovire, ne sme pa štrleti čez
polozaj = random.randint(0, risar.maxX - sirina)

while True:
    # Premakni vse ovire navzdol
    for ovira in ovire:
        ovira.setPos(ovira.x(), ovira.y() + 1)

    # Dodaj novo oviro z verjetnostjo 2%
    if len(ovire) < 20 and random.random() < 0.02:
        # Določi širino ovire med 30 in 80
        sirina = random.randint(30, 80)

        # Določi položaj ovire, ne sme pa štrleti čez
        polozaj = random.randint(0, risar.maxX - sirina)
        
        # Nariši oviro
        ovira = risar.pravokotnik(polozaj, 0, sirina, 25, risar.barva(0, 0, 0))

        # Dodaj oviro v seznam
        ovire.append(ovira)

    # Odstrani ovire, ki niso več vidne
    for ovira in ovire:
        if ovira.y() > risar.maxY:
            risar.odstrani(ovira)
            ovire.remove(ovira)

    # Čakaj 0.002 sekunde
    risar.cakaj(0.002)
