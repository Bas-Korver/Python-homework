#Gemaakt door Joey Einerhand en Bas Körver
#Module voor het inlezen van de .txt bestand en intevoeren in een array
def readfiles(resultaten_bestand):

    #Initialisatie
    leerlingen = []
    lege_str = ''

    #Ervoor zorgen dat de koptekst niet meegenomen wordt
    resultaten_bestand.readline()

    #Het bestand inlezen en invoeren in een array
    evb = False
    while not evb:
        resultaten_regel = resultaten_bestand.readline()
        if resultaten_regel == lege_str:
            evb = True
        else:
            leerlingen.append(resultaten_regel.strip().split(' '))

    return (leerlingen)

#Initialisatie
niet_gevonden = True

#Vragen naar bestand naam
while niet_gevonden:
    bestand_naam = input('Vul het bestandnaam in zonder het suffix(".txt"): ')
    bestand_naam += str('.txt')
    try:
        resultaten_bestand = open(bestand_naam, 'r')
    except FileNotFoundError:
        print('Bestand niet gevonden')
    else:
        niet_gevonden = False

leerlingen = readfiles(resultaten_bestand)

#Initialisatie
aantal_lln = len(leerlingen)
aantalpunt_ll = []
totpunt_ll = []
gempunt_ll = []
aantalpunt_vak = []
totpunt_vak = []
gempunt_vak = []

#cijfers integers maken
for i in range(0,aantal_lln):
    for x in range(2,7):
        leerlingen[i][x] = int(leerlingen[i][x])

#Berekenen van het aantal punten per leerling
tot = 0
for i in range(0,aantal_lln):
    tot = 0
    for x in range(2,7):
        if leerlingen[i][x] != 0:
            tot += 1
    aantalpunt_ll.append(tot)

#Berekenen van het aantal punten per vak
tot = 0
for i in range (2,7):
    tot = 0
    for x in range(0,aantal_lln):
        if leerlingen[x][i] != 0:
            tot += 1
    aantalpunt_vak.append(tot)

#Berekenen van het totaal punt per leerling
tot = 0
for i in range(0,aantal_lln):
    tot = 0
    for x in range(2,7):
        tot += leerlingen[i][x]
    totpunt_ll.append(tot)

#Berekenen van het totaal punt per vak
tot = 0
for i in range (2,7):
    tot = 0
    for x in range(0,aantal_lln):
        tot += leerlingen[x][i]
    totpunt_vak.append(tot)

#Berekenen van het gemiddelde punt per leerling
for i in range(0,aantal_lln):
    if aantalpunt_ll[i] != 0:
        gempunt_ll.append(round(totpunt_ll[i]/aantalpunt_ll[i], 2))
    else:
        gempunt_ll.append('Geen gemiddelde')

#Berekenen van het gemiddelde punt per vak
for i in range(0,5):
    if aantalpunt_vak[i] != 0:
        gempunt_vak.append(round(totpunt_vak[i]/aantalpunt_vak[i], 2))
    else:
        gempunt_vak.append('Geen gemiddelde')

#Weergeven van het gemiddelde punt per leerling
print('')
print('{:<10}{:<13}{:<0}'.format('Nummer', 'Naam', 'gemiddelde'), sep='')
for i in range(0,aantal_lln):
    print('{:<10}{:<13}{:<0}'.format(leerlingen[i][0], leerlingen[i][1], gempunt_ll[i]), sep='')
   
#Weergeven van het gemiddelde punt per vak
print('')
print('{:<7}{:<0}'.format('vak', 'gemiddelde'), sep='')
for i in range(0,5):
    print('{:<7}{:<0}'.format('vak' + str(i+1), gempunt_vak[i]), sep='')

#Een regel die ervoor zorgt dat het programma niet meteen afsluit
print('')
input("Druk op ENTER om af te sluiten")
