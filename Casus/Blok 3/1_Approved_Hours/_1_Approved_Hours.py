#Casus.
print()
print()

def Name_finder():
    import pyodbc
    def_loop = True
    while def_loop:
        conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)}; DBQ=..\UrenRegistratie.accdb')
        Cursor = conn.cursor()

        #Datum query van alle uren.
        SQL_command = ("SELECT DATEPART('m', datum), DATEPART('yyyy',datum) " +
                       "FROM uren " +
                       "ORDER BY uren.datum ASC")
        Cursor.execute(SQL_command)
        Alle_data_set = Cursor.fetchall()

        #Initiatie van variabelen.
        Alle_data_list = []
        
        #De maand en jaar eerst toevoegen aan een tijdelijke list en dan deze tijdelijke list in de uiteindelijke list plaatsen.
        for i in range(0, len(Alle_data_set)):
            temp = []
            temp.append(str(Alle_data_set[i][0]))
            temp.append(str(Alle_data_set[i][1]))
            Alle_data_list.append(temp)
        
        #Alle dubbele waardes verwijderen uit de list halen.
        Alle_data_list = [Alle_data_list[i] for i in range(len(Alle_data_list)) if i == 0 or Alle_data_list[i] != Alle_data_list[i-1]]        

        #Print koptekst.
        print('  Kies een datum die u wilt weergeven')
        print('{:<2}{:<7}{:<0}'.format('', 'Maand', 'Jaar'))
                
        #Functie voor het afdrukken van 15 data's per keer en om de 15 data's vragen of de gebruiker de datum heeft gevonden.
        Loop = True
        Fout_loop = True
        n = 0
        while Loop:            
            for i in range(0, len(Alle_data_list)):                
                Fout_loop = True
                if n < 15 and len(Alle_data_list) > 15:
                    print('{:<2}{:<7}{:<0}'.format('', Alle_data_list[i][0], Alle_data_list[i][1]))                    
                    n += 1
                elif n == 15:
                    print()
                    a = input('  Druk enter voor de volgende pagina of typ stop als u de datum heeft gevonden. ')
                    print()
                    while Fout_loop:                                         
                        if a.lower() != '' and a.lower() != 'stop':
                            a = input('  u heeft iets anders ingetypt druk op enter of typ stop als u de datum heeft gevonden. ')
                            print()
                        elif a.lower() == 'stop':                            
                            n = 16
                            Loop = False
                            Fout_loop = False                                                            
                        else:
                            print('{:<2}{:<7}{:<0}'.format('', Alle_data_list[i][0], Alle_data_list[i][1]))
                            n = 0
                            Fout_loop = False                   
                elif n != 16:
                    print('{:<2}{:<7}{:<0}'.format('', Alle_data_list[i][0], Alle_data_list[i][1]))
            Loop = False
        print()        

        #Functie die aan de gebruiker de maand en jaar vraagd.
        Loop = True
        Try_loop = True
        Fout_loop = True
        while Loop:
            Get_date = input('  Geef de maand en dan het jaar(in die volgorde) die u wilt weergeven gescheiden door een spatie. ').split()
            if Get_date in Alle_data_list:
                Loop = False
            else:
                while Fout_loop:
                    if not Get_date in Alle_data_list:
                        Try_loop = True
                        print()
                        Get_date = input('  Maand en jaar niet gevonden in de database,\n' +
                                         '  check of u een spellingsfout heeft gemaakt en voer opieuw in. ').split()                                                 
                    else:
                        Fout_loop = False
                        Loop = False
        print()

        #Naam query van alle namen.
        SQL_command = ("SELECT medewerker.persoonscode, familienaam, naam " +
                       "FROM medewerker LEFT JOIN uren ON medewerker.persoonscode = uren.persoonscode " +
                       "WHERE MONTH(datum) = %d AND YEAR(datum) = %d " +                       
                       "ORDER BY medewerker.familienaam ASC") %(int(Get_date[0]), int(Get_date[1]))
        Cursor.execute(SQL_command)
        Alle_naam_list = Cursor.fetchall()

        Alle_persoonscode_grote = []
        Alle_familienaam_grote = []
        Editable_list = []

        #Maakt een nieuwe list aan die aangepast kan worden en zet hiet de persoonscode, familienaam en naam in.
        for i in range(0, len(Alle_naam_list)):
            Editable_list.append(list(Alle_naam_list[i]))        
        
        #Verwijderd dubbele waardes.
        Editable_list = [Editable_list[i] for i in range(len(Editable_list)) if i == 0 or Editable_list[i] != Editable_list[i-1]]
        
        #Maakt een speciale list aan met alle persoonscodes.
        for i in range(0, len(Alle_naam_list)):    
            Alle_persoonscode_grote.append(str(Alle_naam_list[i][0]))

        #Maakt een speciale list aan met alle familienamen.
        for i in range(0, len(Alle_naam_list)):    
            Alle_familienaam_grote.append(Alle_naam_list[i][1])

        #Functie die kijkt hoeveel karakters de persoonscode uit bestaat.
        Alle_persoonscode_lengte = len(max(Alle_persoonscode_grote, key=len)) + 2

        #Functie die kijkt hoeveel karakters de familienaam uit bestaat.
        Alle_familienaam_grote = len(max(Alle_familienaam_grote, key=len)) + 2     
                   

        #Functie die kijkt of de aantal karakters 16 is, als dat niet zo is wordt de lengte automatisch 16.
        Loop = True
        while Loop:
            if Alle_persoonscode_lengte < 16:
                Alle_persoonscode_lengte = 16
            else:
                Alle_persoonscode_lengte = str(Alle_persoonscode_lengte)
                Loop = False

         #Functie die kijkt of de aantal karakters 13 is, als dat niet zo is wordt de lengte automatisch 13.
        Loop = True
        while Loop:
            if Alle_familienaam_grote < 13:
                Alle_familienaam_grote = 13
            else:
                Alle_familienaam_grote = str(Alle_familienaam_grote)
                Loop = False
            
        #Print koptekst.
        print('  Kies een naam die u wilt weergeven')
        print('{:<2}{:<{Width1}}{:<{Width2}}{:<0}'.format('', 'Medewerkercode', 'Familienaam', 'Naam', Width1 = Alle_persoonscode_lengte, Width2 = Alle_familienaam_grote))

        #Functie voor het afdrukken van 15 namen per keer en om de 15 namen vragen of de gebruiker de naam heeft gevonden.
        Loop = True
        Fout_loop = True
        n = 0
        while Loop:            
            for i in range(0, len(Editable_list)):                
                Fout_loop = True
                if n < 15 and len(Editable_list) > 15:
                    print('{:<2}{:<{Width1}}{:<{Width2}}{:<0}'.format('', Editable_list[i][0], Editable_list[i][1], Editable_list[i][2], Width1 = Alle_persoonscode_lengte, Width2 = Alle_familienaam_grote))                    
                    n += 1
                elif n == 15:
                    print()
                    a = input('  Druk enter voor de volgende pagina of typ stop als u de naam heeft gevonden. ')
                    print()
                    while Fout_loop:                                         
                        if a.lower() != '' and a.lower() != 'stop':
                            a = input('  u heeft iets anders ingetypt druk op enter of typ stop als u de naam heeft gevonden. ')
                            print()
                        elif a.lower() == 'stop':                            
                            n = 16
                            Loop = False
                            Fout_loop = False                                                            
                        else:
                            print('{:<2}{:<{Width1}}{:<{Width2}}{:<0}'.format('', Editable_list[i][0], Editable_list[i][1], Editable_list[i][2], Width1 = Alle_persoonscode_lengte, Width2 = Alle_familienaam_grote))
                            n = 0
                            Fout_loop = False                   
                elif n != 16:
                    print('{:<2}{:<{Width1}}{:<{Width2}}{:<0}'.format('', Editable_list[i][0], Editable_list[i][1], Editable_list[i][2], Width1 = Alle_persoonscode_lengte, Width2 = Alle_familienaam_grote))
            Loop = False
        print() 
        
        #Functie die aan de gebruiker de persoonscode van de medewerker vraagd.
        Loop = True
        Try_loop = True
        Fout_loop = True
        while Loop:
            while Try_loop:
                try:
                    Get_name = int(input('  Geef de medewerkercode die u wilt weergeven. '))
                except ValueError:
                    print()
                    print('  Heeft u perongelijk op enter gedrukt zonder iets in te typen?\n' +
                          '                        probeer opnieuw')
                    print()
                else:
                    Try_loop = False
            
            if any(Get_name in sublist for sublist in Alle_naam_list):
                Loop = False
            else:
                while Fout_loop:
                    if not any(Get_name in sublist for sublist in Alle_naam_list):
                        Try_loop = True
                        print()
                        while Try_loop:
                            try:
                                Get_name = int(input('  Naam niet gevonden in de database, check of u een spellingsfout heeft gemaakt en voer opieuw in. '))
                            except ValueError:
                                print()
                                print('  Heeft u perongelijk op enter gedrukt zonder iets in te typen?\n' +
                                      '                        probeer opnieuw')
                                print()
                            else:
                                Try_loop = False                       
                    else:
                        Fout_loop = False
                        Loop = False
        print()
                                
        #Naam en uurtarief query.
        SQL_command = ("SELECT naam, uurtarief " +
                       "FROM medewerker LEFT JOIN uren ON medewerker.persoonscode = uren.persoonscode " +
                       "WHERE (medewerker.persoonscode = %d) AND (MONTH(datum) = %d) AND (YEAR(datum) = %d)") %(Get_name, int(Get_date[0]), int(Get_date[1]))
        Cursor.execute(SQL_command)
        Naam_list = Cursor.fetchall()        

        #Activiteit query.
        SQL_command = ("SELECT activiteitnaam " +
                       "FROM (medewerker LEFT JOIN uren ON medewerker.persoonscode = uren.persoonscode) " +
                       "LEFT JOIN activiteit ON uren.activiteitcode = activiteit.activiteitcode " +
                       "WHERE (medewerker.persoonscode = %d) AND (MONTH(datum) = %d) AND (YEAR(datum) = %d) " +
                       "ORDER BY uren.datum ASC") %(Get_name, int(Get_date[0]), int(Get_date[1]))
        Cursor.execute(SQL_command)
        Activiteit_list = Cursor.fetchall()

        #Uur en thuis(ja/nee) query.
        SQL_command = ("SELECT uren, thuis " +
                       "FROM medewerker LEFT JOIN uren ON medewerker.persoonscode = uren.persoonscode " +                       
                       "WHERE (medewerker.persoonscode = %d) AND (MONTH(datum) = %d) AND (YEAR(datum) = %d) " +
                       "ORDER BY uren.datum ASC") %(Get_name, int(Get_date[0]), int(Get_date[1]))
        Cursor.execute(SQL_command)
        Uren_list = Cursor.fetchall()

        #Initialisatie van variabelen.
        Print_list = []
        Activiteit_grote = []
        Uren_groote = []        
        Activiteit_aantal = len(Activiteit_list)   
        Uren_aantal = len(Uren_list)        

        #Kijkt voor de langste lijst.
        loop = True
        while loop:
            if Activiteit_aantal >= Uren_aantal:
                Max_lengte = Activiteit_aantal
                loop = False

            if Uren_aantal >= Activiteit_aantal:
                Max_lengte = Uren_aantal
                loop = False

        #Functie die een aantal lists in een list aanmaakt.
        for i in range (0, Max_lengte + 1):
            Print_list.append(['', '', '', '', ''])        
        
        #Voegt naam van medewerker toe aan nieuwe list.
        Print_list[0][0] = Naam_list[0][0]
        
        #Voegt de activiteiten toe aan een de nieuwe list.
        for i in range (0, Activiteit_aantal):
            Print_list[i][1] = Activiteit_list[i][0]

        #Voegt de aantal uren en thuis(ja/nee) toe aan de nieuwe list.
        for i in range (0, Uren_aantal):
            Print_list[i][2] = Uren_list[i][0]
            Print_list[i][3] = Uren_list[i][1]

        #Voegt de kosten toe aan de nieuwe list.
        for i in range (0, Uren_aantal):
            Print_list[i][4] = Uren_list[i][0] * Naam_list[0][1]
        
        #Voegt een aantal waardes toe aan de nieuwe list.
        Print_list[-1][0] = 'Totaal'
        Print_list[-1][2] = 0
        Print_list[-1][4] = 0        

        #Voegt de totaal aantal uren en totaal aantal kosten toe aan de nieuwe list.
        for i in range (0, Uren_aantal):
            Print_list[-1][4] += Print_list[i][4]
            Print_list[-1][2] += Print_list[i][2]

        #Voegt de activiteit naam toe aan een speciale list.
        for i in range(0, len(Activiteit_list)):    
            Activiteit_grote.append(Activiteit_list[i][0])

        #Voegt de uren toe aan een speciale list.
        for i in range(0, len(Uren_list)):    
            Uren_groote.append(Uren_list[i][0])

        #Functie die kijkt hoeveel karakters de medewerkersnaam uit bestaat.        
        Naam_lengte = len(Naam_list[0][0]) + 2

        #Functie die kijkt of de aantal karakters 6 is, als dat zo is wordt de lengte automatisch 8.
        Loop = True
        while Loop:
            if Naam_lengte < 8:
                Naam_lengte = 8
            else:
                Naam_lengte = str(Naam_lengte)
                Loop = False 

        #Functie die kijkt hoeveel karakters de activiteitenaam uit bestaat wanneer er geen boetes zijn en en er none bij boetes staat
        #Wordt de lengte automatisch 12.
        Loop = True
        while Loop:
            try:
                Activiteit_lengte = len(max(Activiteit_grote, key=len)) + 2                
            except TypeError:
                Activiteit_lengte = 12                
                Loop = False                
            else:                
                Loop = False        

        #Functie die kijkt of de aantal karakters 12 is, als dat niet zo is wordt de lengte automatisch 12.
        Loop = True
        while Loop:
            if Activiteit_lengte < 12:
                Activiteit_lengte = 12
            else:
                Activiteit_lengte = str(Activiteit_lengte)
                Loop = False

        #Functie die kijkt hoeveel karakters de grootste aantal uren uit bestaat wanneer er geen functies zijn en en er none bij functies staat
        #Wordt de lengte automatisch 6.
        Loop = True
        while Loop:
            try:                
                Uren_lengte = len(max(Uren_groote, key=len)) + 2
            except TypeError:                
                Uren_lengte = 6
                Loop = False
            else:                
                Loop = False

        #Functie die kijkt of de aantal karakters 6 is, als dat niet zo is wordt de lengte automatisch 6.
        Loop = True
        while Loop:
            if Uren_lengte < 6:
                Uren_lengte = 6
            else:
                Uren_lengte = str(Uren_lengte)
                Loop = False 

        #Print functie die alle kopnamen uitprint met variabele format lengtes.
        print('{:<2}{:<{Width1}}{:<{Width2}}{:<{Width3}}{:<7}{:<0}'.format('','Naam', 'Activiteit', 'Uren', 'Thuis', 'Kosten', Width1 = Naam_lengte, Width2 = Activiteit_lengte, Width3 = Uren_lengte))

        #Print functie die alle informatie uitprint met variabele format lengtes.
        for i in range(0, Max_lengte):
                print('{:<2}{:<{Width1}}{:<{Width2}}{:<{Width3}}{:<7}{:<0}'.format('', Print_list[i][0], Print_list[i][1], Print_list[i][2], Print_list[i][3], Print_list[i][4], Width1 = Naam_lengte, Width2 = Activiteit_lengte, Width3 = Uren_lengte))
        
        #Print een lijn.
        print('{:<2}{:#<{Width1}}'.format('', '#', Width1 = str(int(Naam_lengte) + int(Activiteit_lengte) + int(Uren_lengte) + 13)))

        #print de totaal variabelen.
        print('{:<2}{:<{Width1}}{:<{Width2}}{:<{Width3}}{:<7}{:<0}'.format('', Print_list[-1][0], Print_list[-1][1], Print_list[-1][2], Print_list[-1][3], Print_list[-1][4], Width1 = Naam_lengte, Width2 = Activiteit_lengte, Width3 = Uren_lengte))

        #Functie die vraagt of je nog een speler wilt opzoeken.
        print()
        Loop = True
        Fout_loop = True
        while Loop:
            a = input('  Wilt u nog een medewerker opzoeken?\n' +
                             '  Ja?, druk op enter\n' +
                             '  Nee?, typ stop: ')
            print()
            if a.lower() != '' and a.lower() != 'stop':
                while Fout_loop:
                    if a.lower() != '' and a.lower() != 'stop':
                        a = input('  u heeft iets anders ingetypt druk op enter of typ stop als u geen nieuwe medewerker wilt zoeken. ')
                        print()
                    elif a.lower() == 'stop':
                        Loop = False
                        Fout_loop = False
                        def_loop = False
                    else:
                        Loop = False
                        Fout_loop = False
                        print('{:<2}{:=<102}'.format('', '='))
                        print()
            elif a.lower() == 'stop':
                Loop = False
                def_loop = False
            else:
                Loop = False
                print('{:<2}{:=<102}'.format('', '='))
                print()

#Roept dev aan
Name_finder()