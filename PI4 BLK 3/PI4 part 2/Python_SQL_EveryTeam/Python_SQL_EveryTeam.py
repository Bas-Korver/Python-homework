#Opdracht 6. Gemaakt door Joey Einerhand en Bas Körver.
import pyodbc
conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)}; DBQ=..\TennisDatabase1.accdb')
Cursor = conn.cursor()

#Query
Select_string = ("SELECT teamnaam, divisie, naam " +
"FROM (team LEFT JOIN teamspeler ON team.teamnr = teamspeler.teamnr) " +
"LEFT JOIN speler ON teamspeler.spelersnr = speler.spelersnr " +
"WHERE (aanvoerder = 'J' OR aanvoerder IS NULL)")
 
Cursor.execute(Select_string)
Cursor_list = Cursor.fetchall()

#Functie die de query print
print('{:<21}{:<14}{:<0}'.format('Teamnaam', 'Divisie', 'Naam'))
for i in range(0, len(Cursor_list)):
    print('{:<21}{:<14}{!s:<0}'.format(Cursor_list[i][0], Cursor_list[i][1], Cursor_list[i][2]))
print('')

