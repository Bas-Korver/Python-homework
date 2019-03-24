#Opdracht 8
import pyodbc

#Hier wordt de achter
get_name = input('Geef een naam die u wilt weergeven ')
conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)}; DBQ=..\TennisDatabase.accdb')

Cursor = conn.cursor()

#main query
SQL_command = ("SELECT naam, bedrag, functienaam, teamnaam, aanvoerder " +
               "FROM ((((speler LEFT JOIN boete ON speler.spelersnr = boete.spelersnr) " +
               "LEFT JOIN bestuurslid ON speler.spelersnr = bestuurslid.spelersnr) " + 
               "LEFT JOIN teamspeler ON speler.spelersnr = teamspeler.spelersnr) " +
               "LEFT JOIN functie ON bestuurslid.functie = functie.functienr) " +
               "LEFT JOIN team ON teamspeler.teamnr = team.teamnr " +
               "WHERE (naam = '%s') " +
               "ORDER BY bestuurslid.begin_datum, teamspeler.datumvan, boete.datum ASC") %(get_name)

Cursor.execute(SQL_command)
Main_list = Cursor.fetchall()

#Boetes query
SQL_command = ("SELECT bedrag " +
               "FROM speler LEFT JOIN boete ON speler.spelersnr = boete.spelersnr " +
               "WHERE (naam = '%s')" +
               "ORDER BY boete.bedrag DESC") %(get_name)

Cursor.execute(SQL_command)
Boetes_list = Cursor.fetchall()

#Team query
SQL_command = ("SELECT teamnr FROM speler LEFT JOIN teamspeler ON speler.spelersnr = teamspeler.spelersnr WHERE (naam = '%s')") %(get_name)

Cursor.execute(SQL_command)
Team_list = Cursor.fetchall()



Editable_list = []
Team_aantal = len(Team_list)
Boetes_aantal = len(Boetes_list)
TeamXBoete_aantal = Team_aantal*Boetes_aantal
Naam_length = str(len(Main_list[0][0]) + 2)
loop = True
while loop:
    try:
        Boete_length = len(Boetes_list[0][0]) + 2
    except TypeError:
        Boete_length = 8
        loop = False
    else:
        loop = False

loop = True
while loop:
    if Boete_length != 8:
        Boete_length += 1
    else:
        Boete_length = str(Boete_length)
        loop = False
    


for i in range(0, len(Main_list)):    
    Editable_list.append(list(Main_list[i]))

for i in range(1, len(Editable_list)):
    Editable_list[i][0] = ''
    
for i in range(Boetes_aantal, len(Editable_list)):
    Editable_list[i][1] = ''

for i in range(TeamXBoete_aantal, len(Editable_list)):
    Editable_list[i][3] = ''
    Editable_list[i][4] = ''

for i in range(0, len(Editable_list), TeamXBoete_aantal):
    x = 1 + i
    while x < TeamXBoete_aantal + i:
        Editable_list[x][2] = ''
        x += 1

print('{:<{Width1}}{!s:<{Width2}}{!s:<16}{!s:<21}{!s:<0}'.format('naam', 'bedrag', 'functienaam', 'teamnaam', 'aanvoerder', Width1 = Naam_length, Width2 = Boete_length))

for i in range(0, len(Editable_list)):
        print('{:<{Width1}}{!s:<{Width2}}{!s:<16}{!s:<21}{!s:<0}'.format(Editable_list[i][0], Editable_list[i][1], Editable_list[i][2], Editable_list[i][3], Editable_list[i][4], Width1 = Naam_length, Width2 = Boete_length))

#print(len(Editable_list))
#print(len(Boetes_list))
#print(len(Team_list))
#print(Editable_list)
#print(Boetes_list)
#print(Team_list)


#("SELECT naam, bedrag, functienaam, teamnaam, aanvoerder " +
#"FROM speler, boete, functie, bestuurslid, team, teamspeler " +
#"WHERE (naam = '%s') AND #(speler.spelersnr = boete.spelersnr) AND #(speler.spelersnr = bestuurslid.spelersnr) AND (bestuurslid.functie = functie.functienr) " +
#"AND #(speler.spelersnr = teamspeler.spelersnr) AND (teamspeler.teamnr = team.teamnr) ORDER BY bestuurslid.begin_datum, teamspeler.datumvan, boete.datum ASC") %(get_name)