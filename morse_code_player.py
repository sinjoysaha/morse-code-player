import time
from pygame import mixer

mixer.init()
dit = mixer.Sound('dit.wav')
dah = mixer.Sound('dah.wav')

s = "-- --- .-. ... .   -.-. --- -.. ."
delay = 1
charspace = 0.25
wordspace = 0.7
wordspace -= charspace

code = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--',
        '?': '..--..', '=': '-...-'}


def translate(inp):
    s = ""
    for i in inp:
        if i == ' ':
            s = s + '|'
        else:
            s = s + code[i] + ' '

    return s


inp = input("Enter a string: ")
print(inp)
inp = inp.upper()
print(inp)
s = ""
s = translate(inp)
print(s)
inp = input("Enter any key to continue: ")


def playdit():
    dit.play()
    time.sleep(delay * 0.18)


def playdah():
    dah.play()
    time.sleep(delay * 0.35)


tic = time.time()
for i in s:
    if i == '.':
        playdit()
    elif i == '_' or i == '-':
        playdah()
    elif i == ' ':
        time.sleep(charspace)
    elif i == '|':
        time.sleep(wordspace)

print(time.time() - tic)
