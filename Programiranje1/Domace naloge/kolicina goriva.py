def gorivo():

    weight = int(input('Vnesite tezo ladje: '))
    litres = 0
    konec = 0

    while weight > 0:

        weight = weight // 3 - 2
        litres += 1

        #Izracun dodatka
        if weight >= 0:
            konec = weight + konec



    return print('Rabite' ,litres, 'ton goriva in nato se', konec, 'litrov za sam prevoz goriva.')




gorivo()