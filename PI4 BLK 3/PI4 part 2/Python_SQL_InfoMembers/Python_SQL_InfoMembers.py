#Assignment 5
import pyodbc
conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)}; DBQ=..\TennisDatabase.accdb')
Cursor = conn.cursor()

SelectString = "SELECT * FROM speler WHERE huisnr = '43'"
 
Cursor.execute(SelectString)
CursorList = Cursor.fetchall()

print (CursorList)