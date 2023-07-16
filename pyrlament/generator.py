import random
from typing import List, Optional

import drawsvg
import numpy as np
from pydantic import BaseModel

from pyrlament.configs import PYRLAMENT_PROPERTIES
from pyrlament.data import Party


class Seat(BaseModel):
    cx: float
    cy: float
    number: int
    fill: str = "#ffffff"
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

    _seats_order = []

    seats: List[Seat]
    parties: List[Party]
    logotype: Optional[str] = None
    legend: bool = False

    def __init__(self, parties: List[Party], logotype: Optional[str] = None):
        self.parties = parties
        # self.logotype = logotype
        self._multiply_center_sectors()
        self._generate_seats_order()
        seats = self._left_sector + self._center_sector + self._right_sector
        self.seats = []
        cnt = 1
        for seat in seats:
            self.seats.append(Seat(cx=seat[0], cy=seat[1], number=cnt, order=0))
            cnt += 1

    def _generate_seats_order_l(self, offset: int = 0):
        sequence = [
            [1, 4, 7, 10, 13, 16, 19, 22, 25, 28],
            [2, 5, 8, 11, 14, 17, 20, 23, 26, 29],
            [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],
        ]
        for row in sequence:
            new_row = []
            for nr in row:
                new_row.append(nr + offset)
            self._seats_order.append(new_row)

    def _generate_seats_order_c(self, offset: int = 0):
        sequence = [
            [31, 34, 39, 45, 48, 52, 57, 62, 68, 75, 82],
            [32, 35, 40, 46, 49, 53, 58, 63, 69, 76, 83],
            [36, 41, 47, 50, 54, 59, 64, 70, 77, 84],
            [51, 55, 60, 65, 71, 78, 85],
            [66, 72, 79, 86],
            [73, 80, 87],
            [56, 61, 67, 74, 81, 88],
            [96, 101, 106, 112, 119, 126],
            [113, 120, 127],
            [107, 114, 121, 128],
            [92, 97, 102, 108, 115, 122, 129],
            [37, 42, 89, 93, 98, 103, 109, 116, 123, 130],
            [43, 90, 94, 99, 104, 110, 117, 124, 131],
            [33, 38, 44, 91, 95, 100, 105, 111, 118, 125, 132],
        ]
        for row in sequence:
            new_row = []
            for nr in row:
                new_row.append(nr + offset)
            self._seats_order.append(new_row)

    def _generate_seats_order(self):
        self._seats_order = []
        self._generate_seats_order_l()
        self._generate_seats_order_c()
        self._generate_seats_order_c(102)
        self._generate_seats_order_c(204)
        self._generate_seats_order_c(306)
        self._generate_seats_order_l(438)

    @staticmethod
    def _sseq(start, stop, step=1):
        """Seat sequence generator."""
        num = start
        while num <= stop:
            yield num
            num += step

    @staticmethod
    def _sseq_v(start, stop, step=(5, 6, 3, 4, 5, 5, 6, 7, 7, 8)):
        """Seat sequence generator with variable step"""
        num = start
        cnt = 0
        while num <= stop and cnt < len(step):
            yield num
            num += step[cnt]
            cnt += 1

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

    def _set_seat_color(self, seat: Seat, x: str):
        fill = self.hex_to_rgb(x)
        color = self.invert_rgb(fill)
        seat.fill = self.rgb_to_hex(fill)
        seat.color = self.rgb_to_hex(color)

    def randomize(self):
        for seat in self.seats:
            self._set_seat_color(seat, random.choice(PYRLAMENT_PROPERTIES.COLORS))

    def _get_seat_by_sequence(self, seat_nr: int) -> int:
        cnt = 0
        for row in self._seats_order:
            for real_seat_nr in row:
                if seat_nr == cnt:
                    return real_seat_nr-1
                cnt += 1

    def colorize(self):
        seat_map = []
        for party in self.parties:
            for x in range(0, party.seats):
                seat_map.append(party.color)
        for y in range(0, len(seat_map)):
            real_y = self._get_seat_by_sequence(y)
            seat = self.seats[real_y]
            self._set_seat_color(seat, seat_map[y])


    def colorize_by_sequence(self):
        color = None
        new_color = None
        cnt = 0
        for seats_row in self._seats_order:
            while new_color == color:
                new_color = random.choice(PYRLAMENT_PROPERTIES.COLORS)
            color = new_color
            for seat_number in seats_row:
                seat = self.seats[seat_number - 1]
                if seat.fill != "#ffffff":
                    print(f"{cnt} == {seat.fill}")
                self._set_seat_color(seat, color)
                cnt += 1
        print(f"{cnt} seats generated")

    def _put_logotype(self):
        pass

    def _get_svg(self):
        svg = drawsvg.Drawing(1122, 841, overflow="hidden")
        g = drawsvg.Group(transform="translate(0 50)")
        for seat in self.seats:
            circle = drawsvg.Circle(seat.cx, seat.cy, 9, fill=seat.fill, stroke="black", stroke_width="0.5")
            seat_number = drawsvg.Text(
                f"{seat.number}",
                8,
                seat.cx,
                seat.cy,
                center=0.6,
                fill=seat.color,
                text_anchor="middle",
                font_family="sans-serif",
            )
            g.append(circle)
            g.append(seat_number)
        svg.append(g)

        if self.logotype:
            logotype = drawsvg.Rectangle(0, 0, 190, 190)
            svg.append(logotype)

        return svg

    def get_svg(self):
        svg = self._get_svg()
        return svg.as_svg()

    def get_gif(self):
        svg = self._get_svg()
        return svg.as_gif()

    def save_svg(self, filename):
        svg = self._get_svg()
        svg.save_svg(filename)

    def save_png(self, filename):
        svg = self._get_svg()
        svg.save_png(filename)

    @staticmethod
    def hex_to_rgb(h: str) -> tuple:
        return tuple(int(h[i : i + 2], 16) for i in (0, 2, 4))

    @staticmethod
    def invert_rgb(c: tuple) -> tuple:
        return (255 - c[0], 255 - c[1], 255 - c[2])

    @staticmethod
    def rgb_to_hex(rgb: tuple) -> str:
        return "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])
