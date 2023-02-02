from cgi import print_environ_usage
import enum
from itertools import count
import numpy as np
#   Naloge 28.10.2022
#   A-javost nizov
#   Napiši program, ki mu uporabnik vpiše niz in pove, koliko črk a je v njem.
#vnos = input('Vnesi neki:')
niz = "kako si danes"
stevec = 0
for a in niz:
    if a == "a":
        stevec += 1
print(stevec)
print()
#   Uporaba count
print(niz.count("a"))
print()
print('2. naloga:')

#   Najmanjši pozitivec
#   Napiši program, ki v danem seznamu števil (lahko ga zapišete kar na začetek programa,
#   npr. l = [5, 4, -7, 2, 12, -3, -4, 11, 7]) poišče in izpiše najmanjše pozitivno število v njem.
#   Za gornji seznam tako izpiše 2.

l = [5, 4, -7, 2, 12, -3, -4, 11, 7]
najmansi = float("inf")
for iskanje in l:
    if iskanje > 0:
        if iskanje < najmansi:
            najmansi = iskanje
print('Resitev:',najmansi)

#   Izboljsava:
for iskanje in l:
    if 0 < iskanje < najmansi:
        najmansi = iskanje

# Izboljsava 2: (List conprehation)
print('Izboljsava 2:',min([st for st in l if st > 0]))
print()
print()

#   Najtežji ven!
print('Naloga 3.')
teze = [66, 72, 84, 68, 96, 73, 80]

#   Boljsa resitev:
teze.remove(max(teze))
print(teze)
print()

#   Iskanje povprecne teze:
print('Naloga 3.1:')
teze_skupaj = 0
for st in teze:
    teze_skupaj = st + teze_skupaj
print('1. Poprecna teza brez najdebelejsega je:', teze_skupaj / len(teze))

#   2. resitev:

print('2. resitev za poprecje:', sum(teze) / len(teze))

# Zanka:
print()
print('Naloga 3.2')
while len(teze) > 0:

    teze.remove(max(teze))
    if len(teze) > 0:
        print('Poprecje:', sum(teze) / len(teze))

print()
print('4. Okljepaji')

oklepaji = "(()()())()"
oklepaji_zaprti = 0

# Naloga 5.

print('NAloga 5.')
print()

izraz = "ABCabc"
sklad = []
pari = {'(': ')', 'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd'}
veljaven = True

if len(izraz) % 2 == 0:
    for znak in izraz:
        if znak in pari.keys():
            sklad.append(znak)
        else:
            if not sklad:
                veljaven = False
                print("Izraz je neveljaven.")
                break
            odpiralni = sklad.pop()
            if znak != pari[odpiralni]:
                veljaven = False
                print("Izraz je neveljaven.")
                break
    if not sklad and veljaven:
        print("Izraz je veljaven.")
else:
    print("Izraz je neveljaven.")





