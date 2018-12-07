from operator import itemgetter, attrgetter
# read file
tekstBestand = open("adreslijst.txt", "r")
totaalTabel = []
empty = False
while (not empty):
    tabelRegel = tekstBestand.readline()
    if (tabelRegel == ""):
        empty = True
    else:
        totaalTabel.append(tabelRegel.strip().split(","))
totaalTabel.sort(key = itemgetter(0))
print('')
print('{:<20}{:<20}{:<20}{:<20}{:<20}'.format('Persoonsnummer', 'Achternaam', 'Voornaam', 'Straatnaam', 'Stadsnaam'), sep='')
for i in range(0, len(totaalTabel)):
    for d in range (0, len(totaalTabel[i])):
        c = d * 3
        print('{:<20}'.format(totaalTabel[i][d]), end="" )
    print()
