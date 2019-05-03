import pyodbc
def_loop = True
conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)}; DBQ=..\UrenRegistratie.accdb')
Cursor = conn.cursor()

SQL_command = ("SELECT DATEPART('m', datum), DATEPART('yyyy',datum), medewerker.persoonscode, naam, uren, uren_volgens_contract_per_week " +
               "FROM medewerker LEFT JOIN uren ON medewerker.persoonscode = uren.persoonscode " +   
               "WHERE thuis = 'ja' OR thuis = 'nee' " +
               "ORDER BY uren.datum ASC")
Cursor.execute(SQL_command)
Uren_list = Cursor.fetchall()

Editable_list = []
Day_home_list = []
Date_name = []

for i in range(0, len(Uren_list)):
    Editable_list.append(list(Uren_list[i]))

for i in range(0, len(Editable_list)):    
    Temp = 0
    Temp_list = []
    Date_name = Editable_list[i]
    for x in range(0, len(Editable_list)):        
        if Date_name[0] == Editable_list[x][0] and Date_name[1] == Editable_list[x][1] and Date_name[2] == Editable_list[x][2]:            
            Temp += round(((Editable_list[x][4] / (Editable_list[x][5] * 4)) * 100), 2)    
    Temp_list
    Temp_list.append(Date_name[0])
    Temp_list.append(Date_name[1])
    Temp_list.append(Date_name[2])
    Temp_list.append(Date_name[3])
    Temp_list.append(Temp)
    Day_home_list.append(Temp_list)
Day_home_list = [Day_home_list[i] for i in range(len(Day_home_list)) if i == 0 or Day_home_list[i] != Day_home_list[i-1]]

print('{:<2}{:<12}{:<14}{:<13}{:<0}'.format('','Datum', 'Persoonscode', 'Naam', 'Bezettingsgraad'))

for i in range(0, len(Day_home_list)):
    print('{:<2}{:<0}-{:<10}{:<14}{:<13}{:<0}'.format('', Day_home_list[i][0] ,Day_home_list[i][1], Day_home_list[i][2], Day_home_list[i][3], Day_home_list[i][4]))