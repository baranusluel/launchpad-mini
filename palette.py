"""
Outputs all possible colors across all the buttons (i.e. color palette)
"""

from __future__ import print_function
import mido
from mido import Message

outputPortName = "Launchpad Mini 1"

try:
    with mido.open_output(outputPortName) as outputPort:
        print(f'Using {outputPort}')
        for x in range(0, 121):
            outputPort.send(Message('note_on', note=x, velocity=x))
except KeyboardInterrupt:
    pass

print()