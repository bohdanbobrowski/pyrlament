"""
This file is usable for debugging.

TODO: change it to a unit tests

"""

from pyrlament import SeatsGenerator

generator = SeatsGenerator(parties=[])
center = generator.get_center()

def ggg(c, x):
    for s in c:
        if s[2] == x:
            return s

l1 = [168, 173, 179, 226, 230, 235, 240, 246, 253, 260, 267]
l2 = [268, 271, 276, 282, 285, 289, 294, 299, 305, 312, 319]

for x in range(len(l1)):
    seat1 = ggg(center, l1[x])
    seat2 = ggg(center, l2[x])
    if seat1[1] != seat2[1]:
        print(seat1, seat2)

print("---")

for x in [372, 377, 383, 430, 434, 439, 444, 450, 457, 464, 471]:
    seat = ggg(center, x)
    if seat[1] != 543:
        print(seat)
