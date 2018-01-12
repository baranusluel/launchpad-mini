"""
Send random notes to the output port.
"""

import sys
import time
from random import *
import mido
from mido import Message

outputPortName = "Launchpad Mini 1"

try:
    with mido.open_output(outputPortName, autoreset=True) as port:
        print('Using {}'.format(port))
        while True:
            note = randint(0, 121)
            on = Message('note_on', note=note, velocity=randint(0, 128))
            print('Sending {}'.format(on))
            port.send(on)
            time.sleep(0.1)

            off = Message('note_off', note=note)
            print('Sending {}'.format(off))
            port.send(off)
            time.sleep(0.05)
except KeyboardInterrupt:
    pass