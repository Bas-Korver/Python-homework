#Opdracht 8. Gemaakt door Joey Einerhand en Bas Körver.

def Name_finder():
    import pyodbc
    def_loop = True
    while def_loop:
        conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)}; DBQ=..\TennisDatabase.accdb')
        Cursor = conn.cursor()

        #Naam query van alle namen.
        SQL_command = ("SELECT spelersnr, naam " +
                       "FROM speler " +
                       "ORDER BY speler.naam ASC")
        Cursor.execute(SQL_command)
        All_naam_list = Cursor.fetchall()

        print('  Kies een naam die u wilt weergeven')

        #Functie voor het afdrukken van 15 namen per keer en om de 15 namen vragen of de gebruiker de naam heeft gevonden.
        Loop = True
        Fout_loop = True
        n = 0
        while Loop:
            for speler in All_naam_list:
                if n < 15 and len(All_naam_list) > 15:
                    print(' ', speler.spelersnr, speler.naam)
                    n += 1
                elif n == 15:
                    print('')
                    a = input('  Druk enter voor de volgende pagina of typ stop als u de naam heeft gevonden. ')
                    print('')
                    if a.lower() != '' and a.lower() != 'stop':
                        while Fout_loop:
                            if a.lower() != '' and a.lower() != 'stop':
                                a = input('  u heeft iets anders ingetypt druk op enter of typ stop als u de naam heeft gevonden. ')
                                print('')
                            elif a.lower() == 'stop':
                                Loop = False
                                Fout_loop = False
                                n = 16                                
                            else:
                                print(' ', speler.spelersnr, speler.naam)
                                n = 0
                                Fout_loop = False
                        
                    elif a.lower() == 'stop':
                        Loop = False
                        n = 16
                    else:
                        print(' ', speler.spelersnr, speler.naam)
                        n = 0
                elif n != 16:
                    print(' ', speler.spelersnr, speler.naam)
            Loop = False
        print('')        
        #Functie die aan de gebruiker de achternaam van de speler gevraagd.
        Loop = True
        Try_loop = True
        Fout_loop = True
        while Loop:
            while Try_loop:
                try:
                    Get_name = int(input('  Geef de spelers nummer die u wilt weergeven. '))
                except ValueError:
                    print('')
                    print('  Heeft u perongelijk op enter gedrukt zonder iets in te typen?\n' +
                          '                        probeer opnieuw')
                    print('')
                else:
                    Try_loop = False
            
            if any(Get_name in sublist for sublist in All_naam_list):
                Loop = False
            else:
                while Fout_loop:
                    if not any(Get_name in sublist for sublist in All_naam_list):
                        Try_loop = True
                        print('')
                        while Try_loop:
                            try:
                                Get_name = int(input('  Naam niet gevonden in de database, check of u een spellingsfout heeft gemaakt en voer opieuw in. '))
                            except ValueError:
                                print('')
                                print('  Heeft u perongelijk op enter gedrukt zonder iets in te typen?\n' +
                                      '                        probeer opnieuw')
                                print('')
                            else:
                                Try_loop = False                       
                    else:
                        Fout_loop = False
                        Loop = False
        print('')

        #Naam query.
        SQL_command = ("SELECT naam " +
                       "FROM speler " +
                       "WHERE (speler.spelersnr = %d)") %(Get_name)
        Cursor.execute(SQL_command)
        Naam_list = Cursor.fetchall()

        #Boetes query.
        SQL_command = ("SELECT bedrag " +
                       "FROM speler LEFT JOIN boete ON speler.spelersnr = boete.spelersnr " +
                       "WHERE (speler.spelersnr = %d)" +
                       "ORDER BY boete.datum ASC") %(Get_name)
        Cursor.execute(SQL_command)
        Boetes_list = Cursor.fetchall()

        #Functie query.
        SQL_command = ("SELECT functienaam " +
                       "FROM (speler LEFT JOIN bestuurslid ON speler.spelersnr = bestuurslid.spelersnr) " +
                       "LEFT JOIN functie ON bestuurslid.functie = functie.functienr " +
                       "WHERE (speler.spelersnr = %d)" +
                       "ORDER BY bestuurslid.begin_datum ASC") %(Get_name)
        Cursor.execute(SQL_command)
        Functie_list = Cursor.fetchall()

        #Team query.
        SQL_command = ("SELECT teamnaam, aanvoerder " +
                       "FROM (speler LEFT JOIN teamspeler ON speler.spelersnr = teamspeler.spelersnr) " +
                       "LEFT JOIN team ON teamspeler.teamnr = team.teamnr " +
                       "WHERE (speler.spelersnr = %d)" +
                       "ORDER BY teamspeler.datumvan ASC") %(Get_name)
        Cursor.execute(SQL_command)
        Team_list = Cursor.fetchall()

        #Initialisatie van variabelen.
        Print_list = []
        Boetes_groote = []
        Functie_groote = []
        Team_groote = []
        Boetes_aantal = len(Boetes_list)
        Team_aantal = len(Team_list)
        Functie_aantal = len(Functie_list)

         #Kijkt voor de langste lijst
        loop = True
        while loop:
            if Boetes_aantal >= Team_aantal and Boetes_aantal >= Functie_aantal:
                Max_lengte = Boetes_aantal
                loop = False

            if Team_aantal >= Boetes_aantal and Team_aantal >= Functie_aantal:
                Max_lengte = Team_aantal
                loop = False

            if Functie_aantal >= Boetes_aantal and Functie_aantal >= Team_aantal:
                Max_lengte = Functie_aantal
                loop = False

        #Functie die de aantal lists in lists aanmaakt
        for i in range (0, Max_lengte):
            Print_list.append(['', '', '', '', ''])        

        Print_list[0][0] = Naam_list[0][0]        

        for i in range (0, Boetes_aantal):
            Print_list[i][1] = Boetes_list[i][0]

        for i in range (0, Functie_aantal):
            Print_list[i][2] = Functie_list[i][0]

        for i in range (0, Team_aantal):
            Print_list[i][3] = Team_list[i][0]
            Print_list[i][4] = Team_list[i][1]

        for i in range(0, len(Boetes_list)):    
            Boetes_groote.append(str(Boetes_list[i][0]))

        for i in range(0, len(Functie_list)):    
            Functie_groote.append(Functie_list[i][0])

        for i in range(0, len(Team_list)):    
            Team_groote.append(Team_list[i][0])

        #Functie die kijkt hoeveel karakters de speler naam uit bestaat.        
        Naam_lengte = len(Naam_list[0][0]) + 2

        #Functie die kijkt of de aantal karakters 6 is, als dat zo is wordt de lengte automatisch 6.
        Loop = True
        while Loop:
            if Naam_lengte < 6:
                Naam_lengte = 6
            else:
                Naam_lengte = str(Naam_lengte)
                Loop = False 

        #Functie die kijkt hoeveel karakters de boete bedrag uit bestaat wanneer er geen boetes zijn en en er none bij boetes staat
        #Wordt de lengte automatisch 8.
        Loop = True
        while Loop:
            try:
                Boetes_lengte = len(max(Boetes_groote, key=len)) + 2                
            except TypeError:
                Boetes_lengte = 8                
                Loop = False                
            else:                
                Loop = False        

        #Functie die kijkt of de aantal karakters 8 is, als dat niet zo is wordt de lengte automatisch 8.
        Loop = True
        while Loop:
            if Boetes_lengte < 8:
                Boetes_lengte = 8
            else:
                Boetes_lengte = str(Boetes_lengte)
                Loop = False

        #Functie die kijkt hoeveel karakters de functienaam uit bestaat wanneer er geen functies zijn en en er none bij functies staat
        #Wordt de lengte automatisch 13.
        Loop = True
        while Loop:
            try:                
                Functie_lengte = len(max(Functie_groote, key=len)) + 2
            except TypeError:                
                Functie_lengte = 13
                Loop = False
            else:                
                Loop = False

        #Functie die kijkt of de aantal karakters 13 is, als dat niet zo is wordt de lengte automatisch 13.
        Loop = True
        while Loop:
            if Functie_lengte < 13:
                Functie_lengte = 13
            else:
                Functie_lengte = str(Functie_lengte)
                Loop = False 

        #Functie die kijkt hoeveel karakters de teamnaam uit bestaat wanneer er geen namen zijn en en er none bij namen staat
        #Wordt de lengte automatisch 10.
        Loop = True
        while Loop:
            try:
                Team_lengte = len(max(Team_groote, key=len)) + 2
            except TypeError:
                Team_lengte = 10
                Loop = False
            else:
                Loop = False

        #Functie die kijkt of de aantal karakters 10 is, als dat niet zo is wordt de lengte automatisch 10.
        Loop = True
        while Loop:
            if Team_lengte < 10:
                Team_lengte = 10
            else:
                Team_lengte = str(Team_lengte)
                Loop = False 

        #Print functie die alle kopnamen uitprint met variabele format lengtes.
        print('{:<2}{:<{Width1}}{:<{Width2}}{:<{Width3}}{:<{Width4}}{:<0}'.format('','Naam', 'Boete', 'Functienaam', 'Teamnaam', 'Aanvoerder', Width1 = Naam_lengte, Width2 = Boetes_lengte, Width3 = Functie_lengte, Width4 = Team_lengte))

        #Print functie die alle informatie uitprint met variabele format lengtes.
        for i in range(0, Max_lengte):
                print('{:<2}{:<{Width1}}{!s:<{Width2}}{!s:<{Width3}}{!s:<{Width4}}{!s:<0}'.format('', Print_list[i][0], Print_list[i][1], Print_list[i][2], Print_list[i][3], Print_list[i][4], Width1 = Naam_lengte, Width2 = Boetes_lengte, Width3 = Functie_lengte, Width4 = Team_lengte))
        
        #Functie die vraagt of je nog een speler wilt opzoeken.
        print('')
        Loop = True
        Fout_loop = True
        while Loop:
            a = input('  Wilt u nog een Speler opzoeken?\n' +
                             '  Ja?, druk op enter\n' +
                             '  Nee?, typ stop: ')
            print('')
            if a.lower() != '' and a.lower() != 'stop':
                while Fout_loop:
                    if a.lower() != '' and a.lower() != 'stop':
                        a = input('  u heeft iets anders ingetypt druk op enter of typ stop als u geen nieuwe speler wilt zoeken. ')
                        print('')
                    elif a.lower() == 'stop':
                        Loop = False
                        Fout_loop = False
                        def_loop = False
                    else:
                        Loop = False
                        Fout_loop = False                
            elif a.lower() == 'stop':
                Loop = False
                def_loop = False
            else:
                Loop = False

Name_finder()