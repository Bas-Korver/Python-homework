import os
import time
os.system('cls')

def prRed(input):
    return('\033[91m{}\033[00m' .format(input))

def prGreen(input):
    return('\033[92m{}\033[00m' .format(input))

def vraag_moeilijkheid():    
    moelijkheidsgraad = input('Geef het moeilijkheidsniveau op,\n' +
                              'U kan kiezen uit: 1, 2 en 3.\n' +
                              'Niveau 1 geeft u een 6x6 speelveld,\n' +
                              'Niveau 2 geeft u een 8x8 speelveld en\n' +
                              'Niveau 3 geeft u een 10x10 speelveld: ') 
    moelijkheidsgraad = input_error_correction_graad(moelijkheidsgraad)

    return(moelijkheidsgraad)

def input_error_correction_graad(moelijkheidsgraad):
    error_loop = True
    while error_loop:
        try:
            moelijkheidsgraad = int(moelijkheidsgraad)
        except ValueError:
            moelijkheidsgraad = input('U heeft iets anders opgegeven.\n' +
                                      'Geef alstublieft opnieuw het niveu: ')
        else:
            if moelijkheidsgraad < 0 or moelijkheidsgraad > 3:
                moelijkheidsgraad = input('U heeft iets anders opgegeven.\n' +
                                          'Geef alstublieft opnieuw het niveu: ')
            else:
                error_loop = False

    return(moelijkheidsgraad)


def speelveld_generator(moelijkheidsgraad):
    speelveld = []
    temp = []
    grootte = moelijkheidsgraad * 2 + 4
    for i in range(0, grootte):
        for x in range(0, grootte):            
            temp.append(prGreen('#'))
        speelveld.append(temp)
        temp = []

    return(speelveld)

def print_speelveld(speelveld, moelijkheidsgraad):
    lines = []
    koptekst = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    rijtekst = 0
    grootte = moelijkheidsgraad * 2 + 4
    for i in range(0, grootte):
        print(koptekst[i], end = ' ')
    print()
    for x in speelveld:
        rijtekst += 1
        print(*x, rijtekst, sep=" ")


    print('\n'.join(lines))

def vraag_veld(moeilijkheidsgraad):
    invul_veld = input('Welk veld wilt u aanpassen?\n' +
                        'Geef eers de kolom, dan de rij en als laats het cijfer dat u in dat veld wilt invullen.\n' +
                        'Alles gescheiden door een spatie: ').split()        
    invul_veld = input_error_correction_veld(invul_veld, moeilijkheidsgraad)   
        
    return(invul_veld)

def input_error_correction_veld(invul_veld, moeilijkheidsgraad):
    grootte = moelijkheidsgraad * 2 + 4
    error_loop = True
    if len(invul_veld) < 3:
        for i in range(0, (3 - len(invul_veld))):
            invul_veld.append('')
    if len(invul_veld) > 3:
        for i in range((3 - len(invul_veld)), 0):
            del(invul_veld[i])
        invul_veld[0] = ''
        invul_veld[1] = ''
        invul_veld[2] = ''

    while error_loop:        
        if (len(invul_veld[0]) != 1):
            invul_veld[0] = input('U heeft iets anders ingetypt bij de kolom letter\n' +
                                  '         probeer alstublieft opnieuw: ').lower()
            print()
        else:
            error_loop = False

    error_loop = True
    while error_loop:
        try:
            invul_veld[0] = invul_veld[0].lower()
        except IndexError:
            invul_veld[0] = input('U heeft iets anders ingetypt bij de kolom letter\n' +
                                  '         probeer alstublieft opnieuw: ').lower()
            print()
        else:
            error_loop = False   
    invul_veld[0] = (ord(invul_veld[0]) - 97)

    error_loop = True
    while error_loop and invul_veld[0] > grootte or invul_veld[0] < 0:
        if invul_veld[0] > moelijkheidsgraad or invul_veld[0] < 0:            
            invul_veld[0] = input('U heeft iets anders ingetypt bij de kolom letter\n' +
                                  '         probeer alstublieft opnieuw: ').lower()
            print()
            invul_veld[0] = (ord(invul_veld[0]) - 97)
        else:
            error_loop = False


    error_loop = True
    while error_loop:
        try:
            invul_veld[1] = int(invul_veld[1])
        except (ValueError, IndexError):
            invul_veld[1] = input('U heeft iets anders ingetypt bij de rij nummer\n' +
                                  '        probeer alstublieft opnieuw: ')
            print()            
        else:
            if invul_veld[1] > grootte or invul_veld[1] <= 0:
                invul_veld[1] = input('U heeft iets anders ingetypt bij de rij nummer\n' +
                                      '        probeer alstublieft opnieuw: ')
                print()               
            else:
                invul_veld[1] -= 1
                error_loop = False


    error_loop = True
    while error_loop:
        try:
            invul_veld[2] = int(invul_veld[2])
        except (ValueError, IndexError):
            invul_veld[2] = input('U heeft iets anders ingetypt bij het intevulen nummer\n' +
                                  '        probeer alstublieft opnieuw: ')
            print()
        else:
            if invul_veld[2] != 0 and invul_veld[2] != 1:
                invul_veld[2] = input('U heeft iets anders ingetypt bij het intevulen nummer\n' +
                                      '        probeer alstublieft opnieuw: ')
                print()
            else:
                error_loop = False

    return(invul_veld)
    

def veld_controle(speelveld, invul_veld, moeilijkheidsgraad):
    grootte = moelijkheidsgraad * 2 + 4
    error_loop = True
    while error_loop:
        if isinstance(speelveld[invul_veld[1]][invul_veld[0]], int):
            invul_veld = input('U heeft een veld gekozen waar een al gegenereerde cijfer staat.\n' +
                               'Geef alstublieft opnieuw eers de kolom, dan de rij en als laats het cijfer dat u in dat veld wilt invullen.\n' +
                               'Alles gescheiden door een spatie: ').split()
            print()
            invul_veld = input_error_correction(invul_veld, moeilijkheidsgraad)
        else:
            speelveld[invul_veld[1]][invul_veld[0]] = prRed(invul_veld[2])
            error_loop = False

    return (speelveld)

start_time = time.time()
aantal_zetten = 0
moelijkheidsgraad = vraag_moeilijkheid()
speelveld = speelveld_generator(moelijkheidsgraad)
print_speelveld(speelveld, moelijkheidsgraad)
loop = True
while loop:
    aantal_zetten += 1
    invul_veld = vraag_veld(moelijkheidsgraad)
    speelveld = veld_controle(speelveld, invul_veld, moelijkheidsgraad)
    print_speelveld(speelveld)
    if sum(x.count('\033[92m#\033[00m') for x in speelveld) == 0:        
        elapsed_time = (time.time() - start_time) / 60
        print()
        print('U hebt gekozen voor moeilijkheidsgraad:', moelijkheidsgraad)
        print()
        print('Gebruikte zetten:', aantal_zetten)
        print('en je speeltijd was:', elapsed_time, 'minuten')       
        loop = False