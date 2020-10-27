from random import randint
from os import system
alpha = ('b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z','a','e','i','o','u')
asci = ['_', 'W', '"', 'Q', "'", 'j', '^', 'N', ')', '&', 'e', 'd', 'L', 'P', 'F', ';', 'w', '%', 'C', 'V', 'x', '0', '`', '[', 'A', '!', ' ', '*', 'B', 'z', ':', 'Z', 'u', 'U', 'h', 'i', 'n', '/', 'p', '>', 'E', '‘', '(', 'f', '1', '3', '4', 'T', '#', '5', 'r', 'J', 'H', 'Y', 'O', '2', '8', 'v', 'c', '?', 's', '6', 'o', 'y', '9', 'S', '$', '7', ']', '.', 'K', 'X', '@', 'b', 'k', 't', 'q', 'R', 'l', ',', 'M', '=', 'g', 'G', '+', 'a', 'I', 'D', 'm', '-', '', '_', 'W', '"', 'Q', "'", 'j', '^', 'N', ')', '&', 'e', 'd', 'L', 'P', 'F', ';', 'w', '%', 'C', 'V', 'x', '0', '`', '[', 'A', '!', ' ', '*', 'B','z', ':', 'Z', 'u', 'U', 'h', 'i', 'n', '/', 'p', '>', 'E', '‘', '(', 'f', '1', '3', '4', 'T', '#', '5', 'r', 'J', 'H', 'Y', 'O', '2', '8', 'v', 'c', '?', 's', '6', 'o', 'y', '9', 'S', '$', '7', ']', '.', 'K', 'X', '@', 'b', 'k', 't', 'q', 'R', 'l', ',', 'M', '=', 'g', 'G', '   ', '+', 'a', 'I', 'D', 'm', '–']
pgp1 = [754, 5456, 98, 64156, 2876, 1546, 2876, 112, 7865, 7115, 187, 81355, 645, 435, 31523, 5560, 478, 4952, 2546, 31215, 156, 7456, 125656, 7123, 35735, 7102, 268, 923, 45, 4, 578, 7456, 154, 4835, 3655, 17456]


def codificar(text):
 lvl = randint(0,88)
 cod = []
 texto = ''
 j = 0 
 o = 0
 i = 0 
 while i != len(text):
    if text[i] != asci[o]:
        if o == 90:
            o = -1
        o += 1
    else:
        ho = o + pgp1[j] + len(text) + lvl + i
        while ho > 89:
            ho -= 90
        cod.append(asci[ho])
        i += 1
        if j == 33:
            j = 0
        else:
            j += 1
 i = 0
 texto = ''
 while i != len(cod):
    texto += cod[i]
    i += 1
 cod = []
 texto += asci[lvl]
 print('\n')
 print(texto)
 texto = ''

def decod(text):
    cod = []
    i = 0
    o = 0
    j = 0
    joa = ''
    k = 0
    ult = len(text)-1
    while text[ult] != joa:
        joa = asci[k]
        k += 1
    text = text[:-1]
    while i != len(text):
        if text[i] != asci[o]:
            if o == 90:
                o = 0
            else:
                o += 1
        else:
            ho = o - pgp1[j] - len(text) - k + 1 - i
            while ho > 89:
                ho -= 90
            while ho < 0:
                ho += 90
            cod.append(asci[ho])
            i += 1
            if j == 33:
                j = 0
            else:
                j += 1 
    i = 0
    texto = ''
    while i != len(cod):
       texto += cod[i]
       i += 1
    cod = []
    print('\n')
    print(texto)
       

while True:
    system('cls')
    textt = ''
    oi = str(input(">>> "))
    if oi == "cod":
        textt = str(input("Texto: "))
        codificar(textt)
        textt = ''
    if oi == 'decod':
        textt = str(input("Texto: "))
        decod(textt)
        textt = ''
    mk = input('')

    
