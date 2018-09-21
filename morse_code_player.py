import time
from pygame import mixer

mixer.init()
dit = mixer.Sound('dit.wav')
dah = mixer.Sound('dah.wav')

s = "__ ___ ._. ... .   _._. ___ _.. ."
delay = 0.2


def playdit():
    dit.play()
    time.sleep(delay)


def playdah():
    dah.play()
    time.sleep(delay + 0.15)


for i in s:
    if i == '.':
        playdit()
    elif i == '_':
        playdah()
    elif i == ' ':
        time.sleep(delay * 2)
