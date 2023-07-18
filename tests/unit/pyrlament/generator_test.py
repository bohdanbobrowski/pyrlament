import unittest

from pyrlament import SeatsGenerator


class TestSeatsPositions(unittest.TestCase):
    @staticmethod
    def get_seat_by_number(c, x):
        for s in c:
            if s[2] == x:
                return s

    def test_two_center_columns_seat_y_position(self):
        generator = SeatsGenerator(parties=[])
        center = generator.get_center()
        l1 = [168, 173, 179, 226, 230, 235, 240, 246, 253, 260, 267]
        l2 = [268, 271, 276, 282, 285, 289, 294, 299, 305, 312, 319]
        for x in range(len(l1)):
            seat1 = self.get_seat_by_number(center, l1[x])
            seat2 = self.get_seat_by_number(center, l2[x])
            assert seat1[1] == seat2[1]

    def test_last_horizontal_row(self):
        generator = SeatsGenerator(parties=[])
        center = generator.get_center()
        for x in [372, 377, 383, 430, 434, 439, 444, 450, 457, 464, 471]:
            seat = self.get_seat_by_number(center, x)
            assert seat[1] == 543
