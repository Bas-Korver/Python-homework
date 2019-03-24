    #Opdracht 8 Gemaakt door Joey Einerhand en Bas Körver.

def Name_finder():
    import pyodbc
    def_loop = True
    while def_loop:
        conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)}; DBQ=..\TennisDatabase.accdb')
        Cursor = conn.cursor()

        #Naam query.
        SQL_command = ("SELECT naam " +
                       "FROM speler " +
                       "ORDER BY speler.naam ASC")
        Cursor.execute(SQL_command)
        Naam_list = Cursor.fetchall()

        print('  Kies een naam die u wilt weergeven')

        #Functie voor het afdrukken van 15 namen per keer en om de 15 namen vragen of de gebruiker de naam heeft gevonden.
        Loop = True
        Fout_loop = True
        n = 0
        while Loop:
            for speler in Naam_list:
                if n < 15 and len(Naam_list) > 15:
                    print(' ', speler.naam)
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
                                print(' ', speler.naam)
                                n = 0
                                Fout_loop = False
                        
                    elif a.lower() == 'stop':
                        Loop = False
                        n = 16
                    else:
                        print(' ', speler.naam)
                        n = 0
                elif n != 16:
                    print(' ', speler.naam)
            Loop = False
        print('')

        #Functie die aan de gebruiker de achternaam van de speler gevraagd.
        Loop = True
        Fout_loop = True
        while Loop:
            Get_name = input('  Geef de naam die u wilt weergeven.\n  Let op de zoekopdracht is hoofletter gevoelig, dus typ de naam zoals weergegeven is. ')
            if any(Get_name in sublist for sublist in Naam_list):
                Loop = False
            else:
                while Fout_loop:
                    if not any(Get_name in sublist for sublist in Naam_list):
                        print('')
                        Get_name = input('  Naam niet gevonden in de database, check of u een spellingsfout heeft gemaakt en voer opieuw in.\n' +
                                         '  Let op de zoekopdracht is hoofletter gevoelig, dus typ de naam zoals weergegeven is. ')
                    else:
                        Fout_loop = False
                        Loop = False
        print('')

        #Main query.
        SQL_command = ("SELECT naam, bedrag, functienaam, teamnaam, aanvoerder " +
                       "FROM ((((speler LEFT JOIN boete ON speler.spelersnr = boete.spelersnr) " +
                       "LEFT JOIN bestuurslid ON speler.spelersnr = bestuurslid.spelersnr) " + 
                       "LEFT JOIN teamspeler ON speler.spelersnr = teamspeler.spelersnr) " +
                       "LEFT JOIN functie ON bestuurslid.functie = functie.functienr) " +
                       "LEFT JOIN team ON teamspeler.teamnr = team.teamnr " +
                       "WHERE (naam = '%s') " +
                       "ORDER BY bestuurslid.begin_datum, teamspeler.datumvan, boete.datum ASC") %(Get_name)
        Cursor.execute(SQL_command)
        Main_list = Cursor.fetchall()

        #Boetes query.
        SQL_command = ("SELECT bedrag " +
                       "FROM speler LEFT JOIN boete ON speler.spelersnr = boete.spelersnr " +
                       "WHERE (naam = '%s')" +
                       "ORDER BY boete.bedrag DESC") %(Get_name)
        Cursor.execute(SQL_command)
        Boetes_list = Cursor.fetchall()

        #Functie query.
        SQL_command = ("SELECT functienaam " +
                       "FROM (speler LEFT JOIN bestuurslid ON speler.spelersnr = bestuurslid.spelersnr) " +
                       "LEFT JOIN functie ON bestuurslid.functie = functie.functienr " +
                       "WHERE (naam = '%s')" +
                       "ORDER BY LEN(functienaam) DESC") %(Get_name)
        Cursor.execute(SQL_command)
        Functie_list = Cursor.fetchall()

        #Team query.
        SQL_command = ("SELECT teamnaam " +
                       "FROM (speler LEFT JOIN teamspeler ON speler.spelersnr = teamspeler.spelersnr) " +
                       "LEFT JOIN team ON teamspeler.teamnr = team.teamnr " +
                       "WHERE (naam = '%s')" +
                       "ORDER BY LEN(teamnaam) DESC") %(Get_name)
        Cursor.execute(SQL_command)
        Team_list = Cursor.fetchall()

        #Initialisatie van variabelen.
        Editable_list = []
        Boetes_aantal = len(Boetes_list)
        Team_aantal = len(Team_list)
        TeamXBoete_aantal = Team_aantal*Boetes_aantal

        #Functie die kijkt hoeveel karakters de speler naam uit bestaat.
        Naam_length = len(Main_list[0][0]) + 2

        #Functie die kijkt of de aantal karakters 6 is, als dat zo is wordt de lengte automatisch 6.
        Loop = True
        while Loop:
            if Naam_length < 6:
                Naam_length += 1
            else:
                Naam_length = str(Naam_length)
                Loop = False 

        #Functie die kijkt hoeveel karakters de boete bedrag uit bestaat wanneer er geen boetes zijn en en er none bij boetes staat
        #Wordt de lengte automatisch 8.
        Loop = True
        while Loop:
            try:
                Boete_length = len(Boetes_list[0][0]) + 2
            except TypeError:
                Boete_length = 8
                Loop = False
            else:
                Loop = False

        #Functie die kijkt of de aantal karakters 8 is, als dat niet zo is wordt de lengte automatisch 8.
        Loop = True
        while Loop:
            if Boete_length < 8:
                Boete_length += 1
            else:
                Boete_length = str(Boete_length)
                Loop = False

        #Functie die kijkt hoeveel karakters de functienaam uit bestaat wanneer er geen functies zijn en en er none bij functies staat
        #Wordt de lengte automatisch 13.
        Loop = True
        while Loop:
            try:
                Functie_length = len(Functie_list[0][0]) + 2
            except TypeError:
                Functie_length = 13
                Loop = False
            else:
                Loop = False

        #Functie die kijkt of de aantal karakters 13 is, als dat niet zo is wordt de lengte automatisch 13.
        Loop = True
        while Loop:
            if Functie_length < 13:
                Functie_length += 1
            else:
                Functie_length = str(Functie_length)
                Loop = False 

        #Functie die kijkt hoeveel karakters de teamnaam uit bestaat wanneer er geen namen zijn en en er none bij namen staat
        #Wordt de lengte automatisch 10.
        Loop = True
        while Loop:
            try:
                Team_length = len(Team_list[0][0]) + 2
            except TypeError:
                Team_length = 10
                Loop = False
            else:
                Loop = False

        #Functie die kijkt of de aantal karakters 10 is, als dat niet zo is wordt de lengte automatisch 10.
        Loop = True
        while Loop:
            if Team_length < 10:
                Team_length += 1
            else:
                Team_length = str(Team_length)
                Loop = False 

        #Maak een list aan voer daar de main list in.
        for i in range(0, len(Main_list)):    
            Editable_list.append(list(Main_list[i]))

        #Functie de dubbele namen verwijderd.
        for i in range(1, len(Editable_list)):
            Editable_list[i][0] = ''
    
        #Functie die de dubbele boetes verwijderd.
        for i in range(Boetes_aantal, len(Editable_list)):
            Editable_list[i][1] = ''
            Editable_list[i][1] = ''

        #Functie die een deel van de dubbele teams en aanvoerder(J/N) verwijderd.
        x = 0
        for i in range(0, len(Editable_list), Boetes_aantal):
            x = 1 + i
            while x < Boetes_aantal + i:
                Editable_list[x][3] = ''
                Editable_list[x][4] = ''
                x += 1

        #Functie die de rest van de dubbele teams en aanvoerder(J/N) verwijderd.
        for i in range(TeamXBoete_aantal, len(Editable_list)):
            Editable_list[i][3] = ''
            Editable_list[i][4] = ''

        #Functie die de dubbele functies verwijderd.
        x = 0
        for i in range(0, len(Editable_list), TeamXBoete_aantal):
            x = 1 + i
            while x < TeamXBoete_aantal + i:
                Editable_list[x][2] = ''
                x += 1

        #Functie die alle witruimtes tussen functies verwijderd
        x = 0
        if len(Editable_list) > len(Functie_list):
            for i in range(TeamXBoete_aantal, len(Editable_list), TeamXBoete_aantal):
                x += 1
                Editable_list[x][2] = Editable_list[i][2]
                Editable_list[i][2] = ''

        #Functie die alle witruimtes tussen teams en aanvoerder(J/N) verwijderd
        x = 0
        if Boetes_aantal >= Team_aantal:
            for i in range(Boetes_aantal, len(Editable_list), Boetes_aantal):
                x += 1
                Editable_list[x][3] = Editable_list[i][3]
                Editable_list[x][4] = Editable_list[i][4]
                Editable_list[i][3] = ''
                Editable_list[i][4] = ''

        #Functie die kijkt welke 'kolom' het langst is
        Loop = True
        while Loop:
            if len(Functie_list) > len(Boetes_list) and len(Functie_list) > len(Team_list):
                Max_length = len(Functie_list)
                Loop = False
            elif len(Team_list) > len(Boetes_list):
                Max_length = len(Team_list)
                Loop = False
            elif len(Boetes_list) > len(Team_list):
                Max_length = len(Boetes_list)
                Loop = False
            elif len(Boetes_list) == len(Team_list):
                Max_length = len(Boetes_list)
                Loop = False
        
        #Functie die kijkt wat de maximale lengte is zodat hij die lists kan overslaan        
        for i in range(Max_length, len(Editable_list)):
            Editable_list.remove(['', '', '', '', ''])

        #Print functie die alle kopnamen uitprint met variabele format lengtes.
        print('{:<2}{:<{Width1}}{:<{Width2}}{:<{Width3}}{:<{Width4}}{:<0}'.format('','Naam', 'Bedrag', 'Functienaam', 'Teamnaam', 'Aanvoerder', Width1 = Naam_length, Width2 = Boete_length, Width3 = Functie_length, Width4 = Team_length))

        #Print functie die alle informatie uitprint met variabele format lengtes.
        for i in range(0, len(Editable_list)):
                print('{:<2}{:<{Width1}}{!s:<{Width2}}{!s:<{Width3}}{!s:<{Width4}}{!s:<0}'.format('', Editable_list[i][0], Editable_list[i][1], Editable_list[i][2], Editable_list[i][3], Editable_list[i][4], Width1 = Naam_length, Width2 = Boete_length, Width3 = Functie_length, Width4 = Team_length))
        
        #Functie die vraagt of je nog een speler wilt opzoeken
        print('')
        Loop = True
        Fout_loop = True
        while Loop:
            a = input('  Wilt u nog een Speler opzoeken?\n' +
                             '  Ja?, druk op enter\n' +
                             '  Nee?, typ stop ')
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