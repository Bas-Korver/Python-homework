#Opdracht 5. Gemaakt door Joey Einerhand en Bas Körver
import pyodbc
conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)}; DBQ=..\TennisDatabase.accdb')
Cursor = conn.cursor()

#Query
Select_string = ("SELECT naam, voorletters, speler.spelersnr, plaats " +
"FROM speler LEFT JOIN teamspeler ON speler.spelersnr = teamspeler.spelersnr " +
"WHERE teamspeler.datumtot IS NULL")
 
Cursor.execute(Select_string)
Cursor_list = Cursor.fetchall()

#Functie die de query print
print('{:<15}{:<14}{:<13}{:<10}'.format('Spelersnummer', 'Naam', 'Voorletters', 'Woonplaats'))
for speler in Cursor_list:
    print('{:<15}{:<14}{:<13}{:<10}'.format(speler.spelersnr, speler.naam, speler.voorletters, speler.plaats))
print('')