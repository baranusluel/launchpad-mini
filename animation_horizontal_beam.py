"""
Turns the pressed button's light on for as long as it is pressed.
"""

import mido
from mido import Message
import time

inputPortName = "Launchpad Mini 0"
outputPortName = "Launchpad Mini 1"

try:
    with mido.open_output(outputPortName) as outputPort, mido.open_input(inputPortName) as inputPort:
        print(f'Using {inputPort} and {outputPort}')
        while True:
            for message in inputPort:
                if message.velocity == 0:
                    continue
                left = right = message.note;
                leftDone = False
                rightDone = False
                while not (leftDone and rightDone):
                    if not leftDone:
                        outputPort.send(Message('note_on', note=left, velocity=127))
                    if not rightDone:
                        outputPort.send(Message('note_on', note=right, velocity=127))
                    time.sleep(0.03)
                    if not leftDone:
                        outputPort.send(Message('note_on', note=left, velocity=0))
                    if not rightDone:
                        outputPort.send(Message('note_on', note=right, velocity=0))
                    if left % 16 > 0:
                        left -= 1
                    else:
                        leftDone = True
                    if right % 8 > 0 or right % 16 == 0:
                        right += 1
                    else:
                        rightDone = True
except KeyboardInterrupt:
    pass