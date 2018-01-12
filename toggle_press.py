"""
Turns the pressed button's light on for as long as it is pressed.
"""

import mido
from mido import Message

inputPortName = "Launchpad Mini 0"
outputPortName = "Launchpad Mini 1"

try:
    with mido.open_output(outputPortName) as outputPort, mido.open_input(inputPortName) as inputPort:
        print(f'Using {inputPort} and {outputPort}')
        while True:
            for message in inputPort:
                outputPort.send(message)
except KeyboardInterrupt:
    pass