import math

def tekmovanje():

    tekmovalec1 = tekmovalec2 = runde = 0
    while 1:
        if runde % 2 == 0:
            num = int(input('Tekmovalec 1 Vnesi stevilko: '))
            num2 = int(input('Tekmovalec 1 Vnesi 2 stevilo: '))
            answer = int(input('Tekmovalec 2 Vnesi odgovor: '))
            rac = num * num2
        else:
            num = int(input('Tekmovalec 2 Vnesi stevilko: '))
            num2 = int(input('Tekmovalec 2 Vnesi 2 stevilo: '))
            answer = int(input('Tekmovalec 1 Vnesi odgovor: '))
            rac = num * num2

        if answer == rac:
            if runde % 2 == 0:
                runde += 1
                tekmovalec1 += 1
            else:
                runde += 1
                tekmovalec2 += 1

        if tekmovalec2 == 4:
            print('Bravo drugi. Prvi cvekk!!!')
            break
        elif tekmovalec1 == 4:
            print('Bravo prvi. Drugi cvekk!!!')
            break
        print(rac)

        print(' Trenutni rezultat:', tekmovalec1,':', tekmovalec2)


tekmovanje()




