"""
Send message to all notes with given port and given velocity.
"""

import sys
import mido
from mido import Message

outputPortName = "Launchpad Mini 1"

if len(sys.argv) == 2:
    velocity = int(sys.argv[1])
else:
    print("Usage: python send.py <velocity>");
    sys.exit();

try:
    with mido.open_output(outputPortName, autoreset=True) as port:
        print('Using {}'.format(port))
        for note in range(0, 121):
          msg = Message('note_on', note=note, velocity=velocity)
          print('Sending {}'.format(msg))
          port.send(msg)
except KeyboardInterrupt:
    pass