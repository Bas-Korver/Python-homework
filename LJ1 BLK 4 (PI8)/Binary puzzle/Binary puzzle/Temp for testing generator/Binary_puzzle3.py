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
def check_regel1_horizontaal(speelveldregel, lege_positie_y):
    j = lege_positie_y
    # Checkt voorafgaand aan in te vullen space
    if (speelveldregel[j - 1] == speelveldregel[j - 2]):
        return ((speelveldregel[j - 1] - 1) ** 2)  # Geeft tegenovergesteld cijfer terug

    elif (lege_positie_y < (len(speelveldregel) - 2)) and (speelveldregel[j + 1] == speelveldregel[j + 2]):
        return (speelveldregel[j + 1] - 1) ** 2  # idem
    else:
        return willekeurig_cijfer()

# Tevens type "X3" in documentatie
def check_regel1_naV(speelveldregel, lege_positie_x):
    i = lege_positie_x
    # Checkt voorafgaand aan in te vullen space
    if (speelveldregel[i - 1] == speelveldregel[i - 2]):
        return ((speelveldregel[i - 1] - 1) ** 2)  # Geeft tegenovergesteld cijfer terug

    elif (speelveldregel[i + 1] == speelveldregel[i + 2]):
        return (speelveldregel[i + 1] - 1) ** 2  # idem
    else:
        return "Y"


# Checkt aan het eind van de grid of een van de twee opties aan het limiet zit
# Tevens type "Y" in documentatie
def check_regel2_horizontaal(speelveldregel, functie_indien_false):
    if (speelveldregel.count(0) == (len(speelveldregel) / 2)):
        return 1
    elif (speelveldregel.count(1) == (len(speelveldregel) / 2)):
        return 0
    # Word alleen gebruikt vanaf kolom 3
    else:
        return "M"

    # Ipv aan het eind, checkt deze vanaf 1 na de helft van de lijn al of regel2


# toegepast kan worden
# Tevens type "Z" in documentatie
def check_regel2_vroegtijdig(speelveldregel, lege_positie_x):
    if (speelveldregel.count(0) == (len(speelveldregel) / 2)):
        return 1
    elif (speelveldregel.count(1) == (len(speelveldregel) / 2)):
        return 0
    else:
        return "X"


# check_regel1_horizontaal maar dan verticaal, alleen voorgaand.  Spreekt voor
# zich.
# Tevens type "X2" in documentatie
def check_regel1_vericaal(speelveld, lege_positie_y, lege_positie_x):
    j = lege_positie_x
    i = lege_positie_y
    # Checkt voorafgaand aan in te vullen space
    if (speelveld[i - 1][j] == speelveld[i - 2][j]):
        return (speelveld[i - 1][j] - 1) ** 2
    else:
        return "V"

# Type "W2" gebaseerd op X2 met andere else return
def check_W2(speelveld, lege_positie_y, lege_positie_x):
    j = lege_positie_x
    i = lege_positie_y
    # Checkt voorafgaand aan in te vullen space
    if (speelveld[i - 1][j] == speelveld[i - 2][j]):
        return (speelveld[i - 1][j] - 1) ** 2
    else:
        return "Z"

# Type "W3" gebaseerd op X2 met andere else return
def check_W3(speelveld, lege_positie_y, lege_positie_x):
    j = lege_positie_x
    i = lege_positie_y
    # Checkt voorafgaand aan in te vullen space
    if (speelveld[i - 1][j] == speelveld[i - 2][j]):
        return (speelveld[i - 1][j] - 1) ** 2
    else:
        return "Y"

# Tevens type "V"
def wachtrij_opzet_recursief(speelveldregel):
    if (speelveldregel.count(0) + speelveldregel.count(1) + speelveldregel.count("v") == len(speelveldregel)):
        return "W3"
    else:
        return "Y"

# Type "M"
def sandwich_checker(speelveldregel, lege_positie_x):
    if ((not(lege_positie_x == 0)) or (not(lege_positie_x == len(speelveldregel))) and
        (speelveldregel[lege_positie_x - 1] == speelveldregel[lege_positie_x + 1])):
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
    for i in range(2,grootte):
        for j in range(4):
            speelveld[i][j] = "X2"
        for j in range(4, grootte):
            speelveld[i][j] = "W2"
        speelveld[i][-1] = "W3"

def genereren_cijfers(speelveld, grootte):
    for i in range(grootte):
        while (speelveld[i].count(0) < grootte / 2) or (speelveld[i].count(1) < grootte / 2):
            for j in range(grootte):
                if (speelveld[i][j] == "R"):
                    speelveld[i][j] = willekeurig_cijfer()
                    print_speelveld(speelveld)
                elif (speelveld[i][j] == "X"):
                    speelveld[i][j] = check_regel1_horizontaal(speelveld[i], j)
                    print_speelveld(speelveld)
                elif (speelveld[i][j] == "Z"):
                    speelveld[i][j] = check_regel2_vroegtijdig(speelveld[i], j)
                    print_speelveld(speelveld)
                elif (speelveld[i][j] == "Y"):
                    speelveld[i][j] = check_regel2_horizontaal(speelveld[i], "M")
                    print_speelveld(speelveld)
                elif (speelveld[i][j] == "X2"):
                    speelveld[i][j] = check_regel1_vericaal(speelveld, i, j)
                    print_speelveld(speelveld)
                elif (speelveld[i][j] == "W2"):
                    speelveld[i][j] = check_W2(speelveld, i, j)
                    print_speelveld(speelveld)
                elif (speelveld[i][j] == "W3"):
                    speelveld[i][j] = check_W3(speelveld, i, j)
                    print_speelveld(speelveld)
                elif (speelveld[i][j] == "M"):
                    speelveld[i][j] = sandwich_checker(speelveld[i], j)
                    print_speelveld(speelveld)
                elif (speelveld[i][j] == "M"):
                    speelveld[i][j] = sandwich_checker(speelveld[i], j)
                    print_speelveld(speelveld)



def print_speelveld(speelveld):
    lines = []
    for row in speelveld:
        lines.append(' '.join(str(x) for x in row))
    print('\n'.join(lines))


moeilijkheidsgraad = 1
grootte = moeilijkheidsgraad * 2 + 4
c = speelveld_generator(grootte)
invullen_speelveld(c, grootte)
genereren_cijfers(c, grootte)
print_speelveld(c)
