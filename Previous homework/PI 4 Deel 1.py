#Gemaakt door Joey Einerhand en Bas Körver

andereModuleBerekenen = True
while andereModuleBerekenen == True:
    aantalPIs = int(input("Aantal PI's: "))
    nummerPIs = []
    moetVoldPIs = []
    wegingPIs = []
    wegingTotaal = 0
    opnieuwBerekenen = True
    print('')
    n = 0
    while (n < aantalPIs):
        nummerPIs.append(input('Wat is het PI nummer van de ' + str(n + 1) + 'e PI?: '))
        n += 1
    print('')
    n = 0
    while (n < aantalPIs):
        wegingPIs.append(int(input('Wat is de weging van PI #' + nummerPIs[n] + '?: ')))
        n += 1
    print('')
    n = 0
    while (n < aantalPIs):
        moetVold = input('Moet PI' + nummerPIs[n] + ' Voldoende zijn? (J/N): ')
        if (moetVold == 'J' or moetVold == 'j' or moetVold == 'ja' or moetVold == 'Ja' or moetVold == 'JA' or moetVold == 'jA'):
            moetVoldPIs.append(1)
        else:
            moetVoldPIs.append(0)
        n += 1
    print('')
    n = 0
    while (n < aantalPIs):
        wegingTotaal += wegingPIs[n]
        n += 1
    n = 0
    while (opnieuwBerekenen == True):
        aantalLln = int(input('Aantal leerlingen?: '))
        lln = 0
        while (aantalLln > 0):
            cijfersPIs = []
            gewogenGem = 0
            eindCijfer = 0            
            lln += 1
            print('')
            print('Deze berekening geldt voor de ' + str(lln) + 'e leerling.')
            n = 0
            while (n < aantalPIs):                
                cijfersPIs.append(float(input('Wat is het cijfer van PI' + nummerPIs[n] + '?: ')))
                n += 1
            print('')
            n = 0
            while (n < aantalPIs):
                gewogenGem += (cijfersPIs[n] * wegingPIs[n])
                n += 1
            n = 0
            gewogenGem /= wegingTotaal
            while (n < aantalPIs):
                if (gewogenGem >= 5.0) and (cijfersPIs[n] < 5.5) and (moetVoldPIs[n] == 1):
                    eindCijfer = 5.0
                    n = aantalPIs
                else:
                    eindCijfer = gewogenGem
                n += 1
            n = 0
            print('Het eindcijfer is: ', round(eindCijfer, 1), sep = '')
            aantalLln -= 1
        print('')
        opnieuwLln = input('Wil je voor meer leerlingen het eindcijfer voor deze module berekenen? (J/N): ')
        if (opnieuwLln == 'J' or opnieuwLln == 'j' or opnieuwLln == 'ja' or opnieuwLln == 'Ja' or opnieuwLln == 'JA' or opnieuwLln == 'jA'):
            print('')
            print('Vul opnieuw het aantal leerlingen in voor wie je het eindcijfer wilt berekenen.')
            print('')
        else:
            opnieuwBerekenen = False
    print('')
    opnieuwMod = input('Wil je voor een andere module eindcijfers berekenen? (J/N): ')
    if (opnieuwMod == 'J' or opnieuwMod == 'j' or opnieuwMod == 'ja' or opnieuwMod == 'Ja' or opnieuwMod == 'JA' or opnieuwMod == 'jA'):
        print('')
        print("Vul opnieuw de informatie over de desbetreffende PI's in.")
        print(format('','-^57'))
    else:
        andereModuleBerekenen = False
print('')
print('Bedankt voor het gebruiken van dit programma.\n', format('Tot ziens!', "^42"))
print('')