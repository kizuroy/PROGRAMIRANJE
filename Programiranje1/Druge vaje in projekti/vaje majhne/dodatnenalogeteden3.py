#   Nepadajoca zaporedja
from re import S


print("Nepadajoca zaporedja")
print("-" * 50)

l = [1,4,6,2,3,4,7,1,4,5,8,2,4,1,4,5,5,6,8,7,3,5,5,3,5,7,1,2,2,5,7,9,9,9,1,2]

najdaljse = 0
to = 1

for stev in range(1, len(l)):
    najdaljse = max(to, najdaljse)
    to = to * (l[stev] >= l[stev-1]) + 1
print(najdaljse)
print()

#   Razceplenje nizov
print("Razceplenje nizov")
print("-" * 50)

stavek = 'Tole je primer          za domaco nalogo'
zadnji_presl = -1
besede = []

for i in range(len(stavek) + 1): #For zanka gre skozi celoten niz.
    if i == len(stavek) or stavek[i] == " ": #Si zapomni kje je videl zadnji presledek.
        if i != zadnji_presl+1: #Ce ni presleda dodamo vse kar je videl do prejsnjeda presledka.
            besede.append(stavek[zadnji_presl+1:i]) 
        zadnji_presl = i
    
print(besede)
print()

#   Mati, bonbonov bi
print("Mati, bonbonov bi")
print("-" * 50)

#Segrevanje
# s = [int(x) for x in input("Seznam: ").split()]
# for st in s:
#     if st % 2 != 0:
#         print("da")
#     else:
#         print("ne")
#Naloga

otroci = [4, 0, 2, 3, 2, 0, 3, 4, 4, 4]

for otroci in range(6):
    if range in otroci:
        print("usi so dobili bonbone")
    else:
        print("USi niso dobili bonbone")

