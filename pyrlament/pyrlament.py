import numpy as np


class SeatsGenerator:

    _left_sector = [
        (396.3, 638, 34),
        (396.3, 616, 35),
        (396.3, 594, 36),
        (353.3, 638, 37),
        (353.3, 616, 38),
        (353.3, 594, 39),
        (310.6, 638, 40),
        (310.6, 616, 41),
        (310.6, 594, 42),
        (267.5, 638, 43),
        (267.5, 616, 44),
        (267.5, 594, 45),
        (224.8, 638, 46),
        (224.8, 616, 47),
        (224.8, 594, 48),
        (182.1, 638, 49),
        (182.1, 616, 50),
        (182.1, 594, 51),
        (138.6, 638, 52),
        (138.6, 616, 53),
        (138.6, 594, 54),
        (96.5, 638, 55),
        (96.5, 616, 56),
        (96.5, 594, 57),
        (54.0, 638, 58),
        (54.0, 616, 59),
        (54.0, 594, 60),
        (11, 638, 61),
        (11, 616, 62),
        (11, 594, 63),
    ]

    _left_center_sector = [
        (436, 543, 64),
        (442, 522, 65),
        (451.6, 502, 66),
        (395, 543, 67),
        (399, 524, 68),
        (404, 506, 69),
        (411, 488, 70),
        (421, 472, 71),
        (353, 543, 72),
        (356, 521, 73),
        (362, 500, 74),
        (370, 480, 75),
        (380, 460, 76),
        (392, 441, 77),
        (311, 543, 78),
        (313, 520, 79),
        (318, 497, 80),

        (269, 543, 81),
        (271, 521, 82),
        (275, 500, 83),
        (280, 480, 84),

    ]

    _right_sector = [
        (725.4, 594, 472),
        (725.4, 616, 473),
        (725.4, 638, 474),
        (768.4, 594, 475),
        (768.4, 616, 476),
        (768.4, 638, 477),
        (810.9, 594, 478),
        (810.9, 616, 479),
        (810.9, 638, 480),
        (853.0, 594, 481),
        (853.0, 616, 482),
        (853.0, 638, 483),
        (896.5, 594, 484),
        (896.5, 616, 485),
        (896.5, 638, 486),
        (939.2, 594, 487),
        (939.2, 616, 488),
        (939.2, 638, 489),
        (981.9, 594, 490),
        (981.9, 616, 491),
        (981.9, 638, 492),
        (1025.0, 594, 493),
        (1025.0, 616, 494),
        (1025.0, 638, 495),
        (1067.7, 594, 496),
        (1067.7, 616, 497),
        (1067.7, 638, 498),
        (1110.7, 594, 499),
        (1110.7, 616, 500),
        (1110.7, 638, 501),
    ]

    @staticmethod
    def _rotate(points, origin, angle):
        rotated = (points - origin) * np.exp(complex(0, angle)) + origin
        return (rotated.real, rotated.imag)

    def _rotate_sector(self, sector, rotate_by, angle, seat_nr):
        result = []
        for seat in sector:
            rotated = self._rotate(
                complex(seat[0], seat[1]), rotate_by, np.deg2rad(angle)
            )
            result.append((rotated[0], rotated[1], seat_nr))
            seat_nr += 1
        return result

    def _multiply_center_sectors(self):
        self._center_sector = (
            self._left_center_sector
            + self._rotate_sector(
                self._left_center_sector,
                rotate_by=complex(571, 561),
                angle=45,
                seat_nr=166,
            )
            + self._rotate_sector(
                self._left_center_sector,
                rotate_by=complex(568, 568),
                angle=90,
                seat_nr=268,
            )
            + self._rotate_sector(
                self._left_center_sector,
                rotate_by=complex(561, 571),
                angle=135,
                seat_nr=370,
            )
        )

    def get_seats(self):
        self._multiply_center_sectors()
        seats = self._left_sector + self._center_sector + self._right_sector
        return seats
