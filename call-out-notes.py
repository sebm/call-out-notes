import musicalbeeps
import os
from random import choice
from time import sleep

ACCIDENTALS = ['', 'b', '#']
ACCIDENTALMAP = {
    '': '',
    'b': ' flat',
    '#': ' sharp'
}
NOTES = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
STRINGS = ['low E', 'A', 'D', 'G', 'B', 'high E']

SPEED = 2

player = musicalbeeps.Player()

while True:
    note = choice(NOTES)
    accidental = choice(ACCIDENTALS)
    string = choice(STRINGS)
    octave = 4 if string == STRINGS[0] else 5
    note_pronounced = "Ey" if note == NOTES[0] else note

    instruction = ('%s%s on the %s string' %
                   (note_pronounced, ACCIDENTALMAP[accidental], string))
    print(instruction)

    os.system(f"say {instruction}")

    sleep(SPEED)

    player.play_note('%s%s%s' % (note, octave, accidental), 0.2)

    sleep(SPEED)
