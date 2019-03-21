#Assignment 8
import pyodbc
conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)}; DBQ=..\TennisDatabase.accdb')
Cursor = conn.cursor()

Select_string = "SELECT naam, voorletters, spelersnr, plaats FROM speler;"
 
Cursor.execute(Select_string)
Cursor_list = Cursor.fetchall()

print('{:<15}{:<14}{:<13}{:<10}'.format('Spelersnummer', 'Naam', 'Voorletters', 'Woonplaats'))
for speler in Cursor_list:
    print('{:<15}{:<14}{:<13}{:<10}'.format(speler.spelersnr, speler.naam, speler.voorletters, speler.plaats))
print('')