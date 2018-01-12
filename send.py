"""
Send given note to given port with given velocity.
"""

import sys
import mido
from mido import Message

outputPortName = "Launchpad Mini 1"

if len(sys.argv) == 3:
    note = int(sys.argv[1])
    velocity = int(sys.argv[2])
else:
    print("Usage: python send.py <note: [0-120]> <velocity>");
    sys.exit();

try:
    with mido.open_output(outputPortName, autoreset=True) as port:
        print('Using {}'.format(port))
        msg = Message('note_on', note=note, velocity=velocity)
        print('Sending {}'.format(msg))
        port.send(msg)
except KeyboardInterrupt:
    pass