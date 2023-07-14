import random
from typing import Dict, List

import drawsvg
import numpy as np
from pydantic import BaseModel

from pyrlament.configs import PYRLAMENT_PROPERTIES


class Seat(BaseModel):
    cx: float
    cy: float
    number: int
    fill: str = "#000000"
    color: str = "#000000"
    order: int


class SeatsGenerator:
    _left_sector = [
        (396, 638, 34),
        (396, 616, 35),
        (396, 594, 36),
        (353, 638, 37),
        (353, 616, 38),
        (353, 594, 39),
        (310, 638, 40),
        (310, 616, 41),
        (310, 594, 42),
        (267, 638, 43),
        (267, 616, 44),
        (267, 594, 45),
        (224, 638, 46),
        (224, 616, 47),
        (224, 594, 48),
        (182, 638, 49),
        (182, 616, 50),
        (182, 594, 51),
        (138, 638, 52),
        (138, 616, 53),
        (138, 594, 54),
        (96, 638, 55),
        (96, 616, 56),
        (96, 594, 57),
        (54, 638, 58),
        (54, 616, 59),
        (54, 594, 60),
        (11, 638, 61),
        (11, 616, 62),
        (11, 594, 63),
    ]

    _left_center_sector = [
        (436, 543, 64),
        (442, 522, 65),
        (451, 502, 66),
        (395, 543, 67),
        (399, 524, 68),
        (404, 506, 69),
        (411, 488, 70),
        (422, 471, 71),
        (353, 543, 72),
        (356, 521, 73),
        (362, 500, 74),
        (370, 480, 75),
        (380, 460, 76),
        (393, 440, 77),
    ]
    _left_center_sector_left = [
        (311, 543, 78),
        (313, 520, 79),
        (318, 497, 80),
        (269, 543, 81),
        (271, 521, 82),
        (275, 500, 83),
        (280, 480, 84),
        (227, 543, 85),
        (228, 523, 86),
        (230, 503, 87),
        (235, 483, 88),
        (240, 463, 89),
        (182, 543, 90),
        (184, 518, 91),
        (188, 493, 92),
        (194, 468, 93),
        (200, 444, 94),
        (140, 543, 95),
        (142, 518, 96),
        (145, 494, 97),
        (149, 472, 98),
        (154, 451, 99),
        (160, 427, 100),
        (97, 543, 101),
        (98, 519, 102),
        (100, 496, 103),
        (104, 473, 104),
        (110, 452, 105),
        (116, 431, 106),
        (122, 410, 107),
        (54, 543, 108),
        (55, 514, 109),
        (57, 490, 110),
        (61, 465, 111),
        (67, 442, 112),
        (73, 416, 113),
        (81, 393, 114),
        (11, 543, 115),
        (13, 512, 116),
        (16, 485, 117),
        (20, 458, 118),
        (26, 429, 119),
        (34, 402, 120),
        (43, 376, 121),
    ]

    _right_sector = [
        (725, 594, 472),
        (725, 616, 473),
        (725, 638, 474),
        (768, 594, 475),
        (768, 616, 476),
        (768, 638, 477),
        (810, 594, 478),
        (810, 616, 479),
        (810, 638, 480),
        (853, 594, 481),
        (853, 616, 482),
        (853, 638, 483),
        (896, 594, 484),
        (896, 616, 485),
        (896, 638, 486),
        (939, 594, 487),
        (939, 616, 488),
        (939, 638, 489),
        (981, 594, 490),
        (981, 616, 491),
        (981, 638, 492),
        (1025, 594, 493),
        (1025, 616, 494),
        (1025, 638, 495),
        (1067, 594, 496),
        (1067, 616, 497),
        (1067, 638, 498),
        (1110, 594, 499),
        (1110, 616, 500),
        (1110, 638, 501),
    ]

    seats: List[Seat]

    def __init__(self):
        self._multiply_center_sectors()
        seats = self._left_sector + self._center_sector + self._right_sector
        self.seats = []
        for seat in seats:
            self.seats.append(Seat(cx=seat[0], cy=seat[1], number=seat[2], order=0))

    @staticmethod
    def _rotate(points, origin, angle):
        rotated = (points - origin) * np.exp(complex(0, angle)) + origin
        return (rotated.real, rotated.imag)

    def _rotate_sector(self, sector, angle, seat_nr, rotate_by=complex(561, 561), move_by=(0, 0)):
        result = []
        for seat in sector:
            rotated = self._rotate(complex(seat[0], seat[1]), rotate_by, np.deg2rad(angle))
            result.append((rotated[0] + move_by[0], rotated[1] + move_by[1], seat_nr))
            seat_nr += 1
        return result

    def _multiply_center_sectors(self):
        left_center_sector_right = self._rotate_sector(
            self._left_center_sector_left, angle=21, seat_nr=122, move_by=(5, -5)
        )
        left_center_sector = self._left_center_sector + self._left_center_sector_left + left_center_sector_right
        self._center_sector = (
            left_center_sector
            + self._rotate_sector(left_center_sector, angle=45, seat_nr=166, move_by=(5, 0))
            + self._rotate_sector(left_center_sector, angle=92, seat_nr=268, move_by=(-5, 5))
            + self._rotate_sector(left_center_sector, angle=135, seat_nr=370, move_by=(1, 16))
        )

    def randomize(self):
        for seat in self.seats:
            fill = self.get_rgb(random.choice(PYRLAMENT_PROPERTIES.COLORS))
            color = self.invert_rgb(fill)
            seat.fill = self.rgb_to_hex(fill)
            seat.color = self.rgb_to_hex(color)

    def colorize(self, parties: Dict):
        # TODO: still needs implementation
        pass

    def svg(self) -> str:
        svg = '<svg width="1122" height="841" xmlns="http://www.w3.org/2000/svg" overflow="hidden">'
        svg += '<g clip-path="url(#clip0)" transform="translate(0 50)">'
        for seat in self.seats:
            svg += f'<circle r="9" stroke="black" stroke-width="1" fill="{seat.fill}" '
            svg += f'cx="{seat.cx}" cy="{seat.cy}">'
            svg += f"<title>{seat.number}</title>"
            svg += "</circle>"
            svg += f'<text font-family="Helvetica, sans-serif" font-size="0.4em" x="{seat.cx}" y="{seat.cy}" '
            svg += f'text-anchor="middle" stroke="{seat.color}" fill="{seat.color}" stroke-width="0.1" '
            svg += f'dy=".3em" stroke-opacity="0.3">{seat.number}</text>'
        svg += "</g></svg>"
        return svg

    def svg_drawsvg(self):
        drawsvg.Drawing(1122, 841, overflow="hidden")
        drawsvg.g()

    @staticmethod
    def get_rgb(h: str) -> tuple:
        return tuple(int(h[i : i + 2], 16) for i in (0, 2, 4))

    @staticmethod
    def invert_rgb(c: tuple) -> tuple:
        return (255 - c[0], 255 - c[1], 255 - c[2])

    @staticmethod
    def rgb_to_hex(rgb: tuple) -> str:
        return "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])
