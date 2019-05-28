import os
import random

os.system('cls')


def prRed(input): return ("\033[91m{}\033[00m".format(input))


# genereert LEEG speelveld
def speelveld_generator(grootte):
    speelveld = []
    temp = []
    for i in range(0, grootte):
        for x in range(0, grootte):
            temp.append('#')
        speelveld.append(temp)
        temp = []
    return speelveld


# Definitions bedoeld om de inhoud van het speelveld te genereren
# Teves type "R" in documentatie
def willekeurig_cijfer():
    return random.randint(0, 1)


# Regel 1, 2, 3 etc zijn te vinden in "B1D01_2018_B4_Inleveropdracht
# 1_BinairePuzzel".
# Tevens type "X" in documentatie
def check_regel1_horizontaal(speelveldregel, lege_positie_x,
                             functie_indien_false):  #####TODO: assign default functie
    i = lege_positie
    # Checkt voorafgaand aan in te vullen space
    if (speelveldregel[i - 1] == speelveldregel[i - 2]):
        return ((speelveldregel[i - 1] - 1) ** 2)  # Geeft tegenovergesteld cijfer terug

    elif (speelveldregel[i + 1] == speelveldregel[i + 2]):
        return (speelveldregel[i + 1] - 1) ** 2  # idem
    else:
        return functie_indien_false

# Tevens type "X3" in documentatie
def check_regel1_naV(speelveldregel, lege_positie_x,
                             functie_indien_false):  #####TODO: assign default functie
    i = lege_positie
    # Checkt voorafgaand aan in te vullen space
    if (speelveldregel[i - 1] == speelveldregel[i - 2]):
        return ((speelveldregel[i - 1] - 1) ** 2)  # Geeft tegenovergesteld cijfer terug

    elif (speelveldregel[i + 1] == speelveldregel[i + 2]):
        return (speelveldregel[i + 1] - 1) ** 2  # idem
    else:
        return "Y"


# Checkt aan het eind van de grid of een van de twee opties aan het limiet zit
# Tevens type "Y" in documentatie
def check_regel2_horizontaal(speelveldregel, lege_positie_x, functie_indien_false):
    if (speelveldregel.count(0) == (len(speelveldregel) / 2)):
        return 1
    elif (speelveldregel.count(1) == (len(speelveldregel) / 2)):
        return 0
    # Word alleen gebruikt vanaf kolom 3
    else:
        return functie_indien_false

    # Ipv aan het eind, checkt deze vanaf 1 na de helft van de lijn al of regel2


# toegepast kan worden
# Tevens type "Z" in documentatie
def check_regel2_vroegtijdig(speelveldregel, lege_positie_x):
    if (speelveldregel.count(0) == (len(speelveldregel) / 2)):
        return 1
    elif (speelveldregel.count(1) == (len(speelveldregel) / 2)):
        return 0
    else:
        return check_regel_2_horizontaal(speelveldregel, lege_positie)


# check_regel1_horizontaal maar dan verticaal, alleen voorgaand.  Spreekt voor
# zich.
# Tevens type "X2" in documentatie
def check_regel1_vericaal(speelveld, lege_positie_x, lege_positie_y, functie_indien_false):
    i = lege_positie
    # Checkt voorafgaand aan in te vullen space
    if (speelveldregel[i - 1] == speelveldregen[i - 2]):
        return (speelveldregen[i - 1] - 1) ** 2
    else:
        return "V"

def check_regel1_vericaal(speelveld, lege_positie_x, lege_positie_y, functie_indien_false):
    i = lege_positie
    # Checkt voorafgaand aan in te vullen space
    if (speelveldregel[i - 1] == speelveldregen[i - 2]):
        return (speelveldregen[i - 1] - 1) ** 2
    else:
        return "Z"

def check_regel1_vericaal(speelveld, lege_positie_x, lege_positie_y, functie_indien_false):
    i = lege_positie
    # Checkt voorafgaand aan in te vullen space
    if (speelveldregel[i - 1] == speelveldregen[i - 2]):
        return (speelveldregen[i - 1] - 1) ** 2
    else:
        return "Y"

# Tevens type "V"
def wachtrij_opzet_recursief(speelveldregel):
    if (speelveldregel.count(0) + speelveldregel.count(1) + speelveldregel.count("v") == len(speelveldregel)):
        return "X3"

# Type "M"
def sandwich_checker(speelveldregel, lege_positie_x):
    if (speelveldregel[lege_positie_x - 1] == speelveldregel[lege_positie_x + 1]):
        return (speelveldregel[lege_positie_x - 1] - 1) ** 2
    elif speelveldregel.count("R") == 0:
        return "R"
    else:
        return "V"

def invullen_speelveld(speelveld,grootte):
    for i in range(2):
        for j in range(2):
            speelveld[i][j] = "R"
        for j in range(2,4):
            speelveld[i][j] = "X"
        for j in range(4,grootte):
            speelveld[i][j] = "Z"
        speelveld[i][-1] = "Y"


def print_speelveld(speelveld):
    lines = []
    for row in speelveld:
        lines.append(' '.join(str(x) for x in row))
    print('\n'.join(lines))


moeilijkheidsgraad = 1
grootte = moeilijkheidsgraad * 2 + 4
a = invullen_speelveld(speelveld, grootte)
b = input('test ')
c = speelveld_generator(grootte)
a[0][0] = prRed('%s') % (b)
print_speelveld(a)
