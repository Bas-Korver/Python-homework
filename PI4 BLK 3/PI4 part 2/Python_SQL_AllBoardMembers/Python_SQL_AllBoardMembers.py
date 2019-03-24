#Opdracht 7. Gemaakt door Joey Einerhand en Bas Körver.
import pyodbc
conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)}; DBQ=..\TennisDatabase1.accdb')
Cursor = conn.cursor()

#Query
Select_string = ("SELECT naam, functienaam " +
"FROM (functie LEFT JOIN bestuurslid on functie.functienr = bestuurslid.functie) " +
"LEFT JOIN speler ON bestuurslid.spelersnr = speler.spelersnr " +
"WHERE eind_datum IS NULL")
 
Cursor.execute(Select_string)
Cursor_list = Cursor.fetchall()

#Functie die de query uitprint
print('{:<14}{:<0}'.format('Naam', 'Functienaam'))
for i in range(0, len(Cursor_list)):
    print('{:<14}{:<0}'.format(Cursor_list[i][0], Cursor_list[i][1]))
print('')
