#!/usr/bin/env python3

import pydobot
import sys


port = "/dev/ttyUSB0"

device = pydobot.Dobot(port=port, verbose=True)

(x, y, z, r, j1, j2, j3, j4) = device.pose()
print(f'x:{x} y:{y} z:{z} j1:{j1} j2:{j2} j3:{j3} j4:{j4}')

# for i in range(2):
#     device.move_to(x + 20, y, z, r, wait=True)
#     device.speed(1,10)
#     device.wait(1000)
#     device.move_to(x, y, z, r, wait=True)
#     device.wait(1000)
try:
    while True:
        (x, y, z, r, j1, j2, j3, j4) = device.pose()
        print(f'x:{x} y:{y} z:{z}')
except KeyboardInterrupt:
    device.close()
    sys.exit(0)
