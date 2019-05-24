import os
os.system('cls')

def prRed(input):
    return("\033[91m{}\033[00m" .format(input))

def prGreen(input):
    return("\033[92m{}\033[00m" .format(input))

def speelveld_generator(moelijkheidsgraad):
    speelveld = []
    temp = []
    grootte = moelijkheidsgraad * 2 + 4
    for i in range(0, grootte):
        for x in range(0, grootte):            
            temp.append('#')
        speelveld.append(temp)
        temp = []
    return(speelveld)

def print_speelveld(speelveld):
    lines = []    
    for row in speelveld:
        lines.append(' '.join(str(x) for x in row))
    print('\n'.join(lines))

def vraag_input():
        invul_veld = input('Welk veld wilt u aanpassen?\n' +
                           'Geef eers de kolom, dan de rij en als laats het cijfer dat u in dat veld wilt invullen.\n' +
                           'Alles gescheiden door een spatie: ').split()
        return(invul_veld)

def input_error_correction(invul_veld, moeilijkheidsgraad):
    invul_veld[0] = [ord(char) - 97 for char in invul_veld[0].lower()]
    while error_loop and not kolom < moelijkheidsgraad and kolom >= 0:
        if kolom < moelijkheidsgraad and kolom >=0:
            print('')
            print('U heeft iets anders ingetypt bij de kolom letter\n' +
                  '      probeer alstublieft opnieuw opnieuw')
            print('')
            invul_veld[0] = input('Welk veld wilt u aanpassen?\n' +
                                  'Geef eers de kolom, de rij en als laats het cijfer dat u hier wilt invullen.\n' +
                                  'Alles gescheiden door een spatie: ').split()
            invul_veld[0] = [ord(char) - 97 for char in invul_veld[0].lower()]
        else:
            error_loop = False


    error_loop = True
    while error_loop:
        try:
            invul_veld[1] = int(invul_veld[1])
        except ValueError:            
            print('')
            print('U heeft iets anders ingetypt bij de rij nummer\n' +
                  '      probeer alstublieft opnieuw opnieuw')
            print('')
            invul_veld[1] = input('Welk veld wilt u aanpassen?' +
                                  'Geef eers de kolom, de rij en als laats het cijfer dat u hier wilt invullen.' +
                                  'Alles gescheiden door een spatie: ').split()
        else:
            invul_veld[1] -= 1
            error_loop = False


    error_loop = True
    while error_loop and invul_veld[2] != 0 and invul_veld[2] != 1:
        try:
            invul_veld[2] = int(invul_veld[2])
        except ValueError:            
            print('')
            print('U heeft iets anders ingetypt bij de rij nummer\n' +
                    '      probeer alstublieft opnieuw opnieuw')
            print('')
            invul_veld[2] = input('Welk veld wilt u aanpassen?' +
                                    'Geef eers de kolom, de rij en als laats het cijfer dat u hier wilt invullen.' +
                                    'Alles gescheiden door een spatie: ').split()
        else:
            error_loop = False



                        
        while loop and int(invulveld[0][1]):



a = speelveld_generator(1)
b = input('test ')
a[0][0] = prRed('%s') %(b)
print_speelveld(a)
