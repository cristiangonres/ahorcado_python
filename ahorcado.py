import random
from ahorcado_lista_dibujos import *

def choice_level():
    level = 0
    while level < 1 or level > 3:
        level = int(input('Selecciona un nivel de dificultad (1, 2, 3)): '))
    return level

def load_dictionary(level):
    min = 0
    max = 0
    if level == 1:
        min = 3
        max = 5
    if level == 2:
        min = 5
        max = 7
    if level == 3:
        min = 7
        max = 20
    with open('0_palabras_todas_no_conjugaciones.txt', 'r') as file:
        lista = [palabra.strip() for palabra in file if len(palabra.strip()) >= min and len(palabra.strip()) <= max ]
    return lista

def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b)
    return s

def choice_word(lista):
    word = random.choice(lista)
    word = normalize(word)
    return word

def draw_panel(word, live, letter_list):
    for l in word:
        flag = True
        for letter in letter_list:
            if l == letter:
                print(letter, end = '')
                flag = False
        if flag:
            print('_', end = '')
    print(ahorcado[live])        

def check_letter(letter, word, letter_list):
    for l in letter_list:
        if l == letter:
            print(f"YA HAS ELEGIDO LA LETRA '{letter}' ANTES")
            return "r"
    for l in word:
        if l == letter:
            print("HAS ACERTADO ESTA LETRA!")
            return "f"
    print(f"LA PALABRA NO CONTIENE LA LETRA '{letter}'")
    return "nf"

def check_win(letter_list, word):
    for l in word:
        flag = False
        for letter in letter_list:
            if l == letter:
                flag = True
        if not flag:
            return False
    return True
                



level = choice_level()
lista = load_dictionary(level)
word = choice_word(lista)
letter_list = set()
live = 0
while True:
    letter = normalize(input('Elige una letra: ')).lower()
    check_let = check_letter(letter, word, letter_list)
    letter_list.add(letter)
    if check_let == "nf":
        live += 1
        print(f"Te quedan {6 - live} vidas")
        if 6 - live == 0:
            print('HAS PEDIDO')
            print(f"La palabra era '{word}'")
            break
    elif check_let == "r":
        continue
    elif check_let == "f":
        if check_win(letter_list, word):
            print("Has ganado!")
            print(f"La palabra era '{word}'")
            break
    draw_panel(word, live, letter_list)
    