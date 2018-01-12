"""
Outputs all possible colors across the buttons with matching values (i.e. note = velocity) to output a color palette.
"""

import mido
from mido import Message

outputPortName = "Launchpad Mini 1"

try:
    with mido.open_output(outputPortName) as outputPort:
        print(f'Using {outputPort}')
        for r in range(0, 4):
          for c in range(0, 4):
              n = c + r * 16;
              msg = Message('note_on', note=n, velocity=n)
              print(msg);
              outputPort.send(msg)
except KeyboardInterrupt:
    pass