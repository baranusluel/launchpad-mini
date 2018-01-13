"""
Example of non-blocking reception from input port.

Adapted from Mido examples.
"""

import sys
import time
import mido

if len(sys.argv) > 1:
    portname = sys.argv[1]
else:
    portname = None  # Use default port

try:
    with mido.open_input(portname) as port:
        print('Using {}'.format(port))
        while True:
            for message in port.iter_pending():
                print('\nReceived {}'.format(message))

            print(".", end="")
            sys.stdout.flush()
            time.sleep(0.5)
except KeyboardInterrupt:
    pass