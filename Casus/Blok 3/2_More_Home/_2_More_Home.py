import pyodbc
def_loop = True
conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)}; DBQ=..\UrenRegistratie.accdb')
Cursor = conn.cursor()

SQL_command = ("SELECT DATEPART('d', datum), DATEPART('m', datum), DATEPART('yyyy',datum), uren " +
               "FROM medewerker LEFT JOIN uren ON medewerker.persoonscode = uren.persoonscode " +                       
               "WHERE thuis = 'ja'" +
               "ORDER BY uren.datum ASC")
Cursor.execute(SQL_command)
Uren_list = Cursor.fetchall()

Editable_list = []
Day_home_list = []
Date = []

for i in range(0, len(Uren_list)):
    Editable_list.append(list(Uren_list[i]))

for i in range(0, len(Editable_list)):    
    Temp = 0
    Temp_list = []
    Date = Editable_list[i]
    for x in range(0, len(Editable_list)):        
        if Date[0] == Editable_list[x][0] and Date[1] == Editable_list[x][1] and Date[2] == Editable_list[x][2]:            
            Temp += Editable_list[x][3]    
    Temp_list
    Temp_list.append(Date[0])
    Temp_list.append(Date[1])
    Temp_list.append(Date[2])
    Temp_list.append(Temp)
    Day_home_list.append(Temp_list)
Day_home_list = [Day_home_list[i] for i in range(len(Day_home_list)) if i == 0 or Day_home_list[i] != Day_home_list[i-1]]        

print('{:<2}{:<12}{:<0}'.format('','Datum', 'Uren thuis'))

for i in range(0, len(Day_home_list)):
    print('{:<2}{:<0}-{:<0}-{:<8}{:<0}'.format('', Day_home_list[i][0] ,Day_home_list[i][1], Day_home_list[i][2], Day_home_list[i][3]))