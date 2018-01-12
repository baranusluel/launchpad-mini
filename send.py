"""
Send given note to given port with given velocity.
"""

import sys
import mido
from mido import Message


if len(sys.argv) == 4:
    portname = sys.argv[1]
    note = int(sys.argv[2])
    velocity = int(sys.argv[3])
    print("yes");
else:
    print("Usage: python send.py <MIDI device> <note: [0-120]> <velocity>");
    sys.exit();

try:
    with mido.open_output(portname, autoreset=True) as port:
        print('Using {}'.format(port))
        msg = Message('note_on', note=note, velocity=velocity)
        print('Sending {}'.format(msg))
        port.send(msg)
except KeyboardInterrupt:
    pass