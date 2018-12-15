#Gemaakt door Joey Einerhand, Bas Körver, Araya Mingels, Sander Schmeitz en Maud Reijnen


#Module voor het inlezen van het .csv bestand en intevoeren in een array
def leesBestand(bestand_naam, bestand_sep):

    #Initialisatie
    bestand_lijst = []
    lege_str = ''

    #Ervoor zorgen dat de koptekst niet meegenomen wordt
    bestand_naam.readline()

    #Het bestand inlezen en invoeren in een array
    evb = False
    while not evb:
        bestand_regel = bestand_naam.readline()
        if bestand_regel == lege_str:
            evb = True
        else:
            bestand_lijst.append(bestand_regel.replace('"','').strip().split(bestand_sep))

    return (bestand_lijst)

#In verband met tijdsgebrek kon dit niet gemaakt worden zie documentatie bestandA
#Module voor het schrijven van het .csv bestand
#def schrijfBestand(bestand_naam, bestand_sep, tabel):
#    bestand = open(bestand_naam, 'w')
#    for rij in tabel:
#        regel = ''
#        for kolom in rij:
#            if regel == '':
#                regel = kolom
#            else:
#                regel = regel + bestand_sep + kolom
#        bestand.write(regel + '\n')
#    bestand.close()

#Modlule voor een keuzen menu
def keuze_menu():    
    loop = True
    while loop == True:
        print('__________________________________________________________')
        print('│  Maak een keuze uit de volgende opties:                │')
        print('│  1. Druk een overzicht af van deelnemers per workshop  │')
        print('│  2. Druk een overzicht af van alle groepen             │')
        print('│  3. Kies een groepnummer om af te drukken              │')
        print('│  4. Druk alle leden af + emailadres                    │')
        print('│  5. Zoek naar een lid                                  │')
        print('│  6. Druk workshopplanning af                           │')
        print('│  7. Exit                                               │')
        print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')

        print('')
        menu_keuze = input('Welke optie? ')
        if menu_keuze == '1':
            for i in range(0, aantal_workshops):
                print('')
                print(workshop_lijst[i][0])
                for x in range(8, 8 + workshop_lijst[i][5]):        
                    print(workshop_lijst[i][x])
            print('')

        elif menu_keuze == '2':
            for i in range (0, len(groepen)):
                print('')
                print(groepen[i][0])
                for x in range (1, len(groepen[i])):
                    print(groepen[i][x])
            print('')

        elif menu_keuze == '3':
            print('')
            groep_keuze = int(input('Welke groep wil je afdrukken? '))
            while groep_keuze > len(groepen):
                print('Deze groep bestaat niet ')
                groep_keuze = int(input('Welke groep wil je afdrukken? '))
            else:
                groep_keuze = groep_keuze - 1
                print('')
                print(groepen[groep_keuze][0])
                for i in range (1, len(groepen[groep_keuze])):
                    print(groepen[groep_keuze][i])
            print('')
        
        elif menu_keuze == '4':
            for i in range(0, len(leden_lijst)):
                print('')
                print(leden_lijst[i][2],end = ' ')
                print(leden_lijst[i][1])
            print('')
                
        elif menu_keuze == '5':
            zoek_naam = input('Wat is de naam van de persoon die je zoekt? (voor- en achternaam gescheiden door een spatie) ')
            for i in range(0, len(leden_lijst)):
                if leden_lijst[i][2].casefold() == zoek_naam.casefold():
                        print('Naam: ',end = '')
                        print(leden_lijst[i][2])
                        print('Leerlingnr: ',end = '')
                        print(leden_lijst[i][3])
                        print('Emailadres: ',end = '')
                        print(leden_lijst[i][1])
                        print('Lezing: ',end = '')
                        print(leden_lijst[i][9])
                        print('vegetarisch?: ',end = '')
                        print(leden_lijst[i][4])
                        print('Allergieën?: ',end = '')
                        print(leden_lijst[i][5])
                        if leden_lijst[i][5].casefold() == 'ja':
                            print('Welke allergieën?: ',end = '')
                            print(leden_lijst[i][6])
            print('')
                        
        elif menu_keuze == '6':
            keuze_6 = '0'
            print('Wil je een overzicht van een specifieke workshop, kies 1 ')
            print('Wil je een volledig overzicht, kies 2 ')
            keuze_6 = input('Keuze: ')
            while keuze_6 != '1' and keuze_6 != '2':
                keuze_6 = input('Vul 1 of 2 in ')
            if keuze_6 == '1':
                print('')
                for i in range(0, len(workshop_lijst)):                    
                    print('voor: ', workshop_lijst[i][0], '. Kies ' + str(i + 1), sep = '')
                print('')
                workshop_keuze = int(input('Van welke workshop wil je meer informatie? (vul het nummer in) '))
                workshop_keuze = workshop_keuze - 1
                print('')
                print('Workshop: ', workshop_planning[workshop_keuze][0], sep = '')
                print('')
                for i in range(1, (len(workshop_planning[workshop_keuze]))):                    
                    print('________________')
                    print('Begintijd: ', workshop_planning[workshop_keuze][i][0], 'uur', sep = '')
                    print('Eindtijd: ', workshop_planning[workshop_keuze][i][1], 'uur', sep = '')
                    print('')
                    for x in range(2, len(workshop_planning[workshop_keuze][i])):
                        print(workshop_planning[workshop_keuze][i][x])
            elif keuze_6 == '2':
                print('')
                for x in range (0, len(workshop_planning)):
                    print('')
                    print(workshop_planning[x][0])
                    for i in range(1, len(workshop_planning[x])):                    
                        print('________________')
                        print('Begintijd: ', workshop_planning[x][i][0], 'uur', sep = '')
                        print('Eindtijd: ', workshop_planning[x][i][1], 'uur', sep = '')
                        print('')
                        for y in range(2, len(workshop_planning[x][i])):
                            print(workshop_planning[x][i][y])
            print('')
                
            
        elif menu_keuze == '7':
            loop = False
            
        else:
            print('Maak een keuze tussen de gegeven nummers ')


#Initialisatie
niet_gevonden = True

#Vragen naar de bestandsnaam van het inschrijfformulier
while niet_gevonden:
    bestand_naam = input('Vul de bestandsnaam in van het inschrijfformulier zonder het suffix(".csv"): ')
    bestand_naam += str('.csv')    
    try:
        formulier_bestand = open(bestand_naam, 'r')
    except FileNotFoundError:
        print('Bestand niet gevonden')
    else:
        niet_gevonden = False

leden_sep = input('Welke seperator hanteert het inschrijfformulierbestand? (Bijvoorbeeld ,  of ; ) ')
leden_lijst = leesBestand(formulier_bestand, leden_sep)

#Initialisatie
print('')
niet_gevonden = True

#Vragen naar de bestandsnaam van de workshop
while niet_gevonden:
    bestand_naam = input('Vul de bestandsnaam in van de workshop zonder het suffix(".csv"): ')
    bestand_naam += str('.csv')    
    try:
        workshop_bestand = open(bestand_naam, 'r')
    except FileNotFoundError:
        print('Bestand niet gevonden')
    else:
        niet_gevonden = False

workshop_sep = input('Welke seperator hanteert het workshopbestand? (Bijvoorbeeld ,  of ; ) ')
workshop_lijst = leesBestand(workshop_bestand, workshop_sep)

#Initialisatie
team_num = 1
groepen = []
aantal_leden = len(leden_lijst)

#Module voor het toevoegen van een teamnaam aan de leden die in een groep horen. Ook wordt er een aparte array maken voor de groepen
for i in range(0, aantal_leden):
    
    #Hier wordt gecheckt of de persoon de groepsleider is,
    #zo ja dan wordt in de leden_lijst array aan het eind een team naam toegevoegd en
    #wordt de teamnaam plus de groepsleider's naam toegevoegd aan de temp_groep list
    if leden_lijst[i][14].casefold() == 'ja':
        temp_groep = []
        temp_groep.append('team ' + str(team_num))
        temp_groep.append(leden_lijst[i][2])      
        leden_lijst[i].append('team ' + str(team_num))
        aantal_groepsleden = int(leden_lijst[i][22])    
        
        #Hier wordt de groepslid op plek 15 en verder toegevoegd aan de temp_groep list.
        for x in range(15, 15 + aantal_groepsleden):            
            groeps_lid = leden_lijst[i][x]
            temp_groep.append(groeps_lid)
            
            #Hier wordt gekeken naar de groepsleden die op plek 15 staan en verder,
            #en wordt gekeken of er namen overeen komen in de rest van de lijst zo ja dan wordt dezelfde team naam toegevoegd
            for y in range(0, aantal_leden):
                if groeps_lid.lower() == leden_lijst[y][2].lower():
                    leden_lijst[y].append('team ' + str(team_num))
        groepen.append(temp_groep)
        team_num += 1

#Initialisatie
aantal_groepen = len(groepen)
temp_groep = []
a = 0

#Module voor het checken of groepen kleiner dan 8 zijn zo ja dan worden er automatisch de nodige leden bij gezet
for i in range(0, aantal_groepen):
    if len(groepen[i]) != 9:        
        len_groep = len(groepen[i])
        for x in range(0, aantal_leden):            
            if len(leden_lijst[x]) != 24: 
                if a < (9 - len_groep):
                    groepen[i].append(leden_lijst[x][2])
                    leden_lijst[x].append(groepen[i][0])
                    a += 1               
                else:                    
                    x -= 1
        a = 0

#Initialisatie
temp_groep = []
a = 0

#Module voor het checken of er nog steeds mensen zijn die geen groep hebben 
for i in range(0, aantal_leden):
    if len(leden_lijst[i]) != 24:
        if a < 8:
            leden_lijst[i].append('team ' + str(team_num))
            temp_groep.append(leden_lijst[i][2])
            a += 1            
            if (i + 1) == aantal_leden:
                temp_groep.insert(0, 'team ' + str(team_num))
                groepen.append(temp_groep)
                team_num += 1
                temp_groep = []
        else:   
            temp_groep.insert(0, 'team ' + str(team_num))
            groepen.append(temp_groep)
            team_num += 1
            temp_groep = []
            a = 0
            i -= 1
    elif (i + 1) == aantal_leden:
        temp_groep.insert(0, 'team ' + str(team_num))
        groepen.append(temp_groep)
        team_num += 1
        temp_groep = [] 

#Initialisatie
aantal_workshops = len(workshop_lijst)

#Module voor het checken welke workshop het lid gekozen en dit lid toevoegen aan de workshop_lijst
#en de aantal deelnemers toevoegen
for i in range(0, aantal_leden):
    for x in range(0, aantal_workshops):
        for y in range(10, 12):
            if workshop_lijst[x][0] == leden_lijst[i][y]:                
                workshop_lijst[x][5] = (int(workshop_lijst[x][5]) + 1)
                workshop_lijst[x].append(leden_lijst[i][2])

#Module voor het berekenen hoeveel keer de workshop moet worden gehouden en wat de eindtijd is
for i in range(0, aantal_workshops):
    workshop_lijst[i][6] = (int(round((workshop_lijst[i][5] / int(workshop_lijst[i][7])) + 0.5)))
    workshop_lijst[i][3] = (int(workshop_lijst[i][2]) + (int(workshop_lijst[i][4]) * workshop_lijst[i][6]))

#Initialisatie
workshop_planning = []
temp_planning = []
temp_planning2d = []
a = 8
notoutofrange = True
tijd = 0

#module om alle leden van een workshop in een 3d array te zetten en de begin en eindtijd te berkenen
for i in range(0, aantal_workshops):
    if workshop_lijst[i][6] != 0:
        temp_planning2d = []
        temp_planning2d.append(workshop_lijst[i][0])
        for x in range(0, workshop_lijst[i][6]):
            temp_planning = []
            a = 8
            temp_planning.append(int(workshop_lijst[i][2]) + tijd)
            temp_planning.append(int(workshop_lijst[i][2]) + int(workshop_lijst[i][4]) + tijd)
            notoutofrange = True
            while a < 28 and notoutofrange:
                try:
                    workshop_lijst[i][a]
                except IndexError:
                    notoutofrange = False
                else:
                    temp_planning.append(workshop_lijst[i][a])
                    a += 1
            tijd += int(workshop_lijst[i][4])
            temp_planning2d.append(temp_planning)
    workshop_planning.append(temp_planning2d)
    tijd = 0

#Open menu
keuze_menu()