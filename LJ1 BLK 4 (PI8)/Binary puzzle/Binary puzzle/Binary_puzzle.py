import os
os.system('cls')

def prRed(input): return("\033[91m{}\033[00m" .format(input))

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

a = speelveld_generator(1)
b = input('test ')
a[0][0] = prRed('%s') %(b)
print_speelveld(a)
