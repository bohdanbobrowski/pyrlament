import math
import random
from typing import List, Optional

import drawsvg
import numpy as np
from cairosvg.surface import PNGSurface
from pydantic import BaseModel

from pyrlament.configs import PYRLAMENT_PROPERTIES
from pyrlament.data import GERMAN_MINORITY, Party


class Seat(BaseModel):
    cx: float
    cy: float
    number: int
    label: int
    fill: str = "#ffffff"
    color: str = "#000000"
    order: int

    def reset_colors(self):
        self.fill = "#ffffff"
        self.color = "#000000"


class SeatsGenerator:
    _left_center_sector = [
        (436, 543, 64),
        (442, 520, 65),
        (451, 499, 66),
        (395, 543, 67),
        (399, 524, 68),
        (404, 506, 69),
        (411, 488, 70),
        (421, 469, 71),
        (353, 543, 72),
        (356, 521, 73),
        (362, 500, 74),
        (370, 480, 75),
        (380, 460, 76),
        (391, 439, 77),
    ]
    _left_center_sector_left = [
        (311, 543, 78),
        (313, 520, 79),
        (317, 497, 80),
        (269, 543, 81),
        (271, 521, 82),
        (276, 501, 83),
        (282, 482, 84),
        (227, 543, 85),
        (228, 523, 86),
        (230, 503, 87),
        (235, 483, 88),
        (240, 463, 89),
        (182, 543, 90),
        (184, 518, 91),
        (188, 493, 92),
        (194, 468, 93),
        (202, 446, 94),
        (140, 543, 95),
        (142, 518, 96),
        (145, 494, 97),
        (149, 472, 98),
        (154, 451, 99),
        (161, 428, 100),
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

    seats_order = []

    seats: List[Seat]
    parties: List[Party]
    logotype: Optional[str] = None
    legend: bool = False
    caption: str = ""

    _skip_empty_seats = True

    def __init__(
        self,
        parties: List[Party],
        logotype: Optional[str] = None,
        legend: bool = True,
        skip_empty_seats: bool = True,
        caption: str = "",
    ):
        self.parties = parties
        self.logotype = logotype if logotype else "assets/pyRLAMENT_logo.svg"
        self.legend = legend
        self.caption = caption
        self._skip_empty_seats = skip_empty_seats
        self.seats = []
        cnt = 1
        for seat in self._get_seat_positions_and_numbers():
            self.seats.append(Seat(cx=seat[0], cy=seat[1], number=cnt, label=seat[2], order=0))
            cnt += 1

    def get_center(self):
        return self._get_center_sectors()

    def _get_seat_positions_and_numbers(self) -> List[tuple]:
        return self._get_left_sector() + self._get_center_sectors() + self._get_right_sector()

    def _get_left_sector(self) -> List[tuple]:
        """This method generates positions of seats in LEFT sector.
        :return: [(<seat x>, <seat y>, <seat label>)]
        """
        ls = []
        seat_label = 34
        seat_x = 396
        for i in range(10):
            seat_y = 638
            for j in range(3):
                ls.append((seat_x, seat_y, seat_label))
                seat_y -= 22
                seat_label += 1
            seat_x -= 43
        return ls

    def _get_right_sector(self) -> List[tuple]:
        """This method generates positions of seats in RIGHT sector.
        :return: [(<seat x>, <seat y>, <seat label>)]
        """
        ls = []
        seat_label = 472
        seat_x = 725
        for i in range(10):
            seat_y = 594
            for j in range(3):
                ls.append((seat_x, seat_y, seat_label))
                seat_y += 22
                seat_label += 1
            seat_x += 43
        return ls

    def _generate_seats_order_l(self, offset: int = 0) -> List[List[int]]:
        seats_order = []
        sequence = [
            [1, 4, 7, 10, 13, 16, 19, 22, 25, 28],
            [2, 5, 8, 11, 14, 17, 20, 23, 26, 29],
            [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],
        ]
        for row in sequence:
            new_row = []
            for nr in row:
                new_row.append(nr + offset)
            seats_order.append(new_row)
        return seats_order

    def _generate_seats_order_c(self, offset: int = 0) -> List[List[int]]:
        seats_order = []
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
            seats_order.append(new_row)
        return seats_order

    def _move_random_seats_to_end(self, seats_to_move: int = 9):
        seats_moved = []
        rows_modified = []
        while len(seats_moved) < seats_to_move:
            row_nr = random.randint(2, 59)
            if row_nr not in rows_modified:
                row = self.seats_order[row_nr]
                seats_moved.append(row[-1])
                self.seats_order[row_nr] = row[:-1]
                rows_modified.append(row_nr)
        self.seats_order.append(seats_moved)

    def _generate_seats_order(self):
        self.seats_order = []
        self.seats_order += self._generate_seats_order_l()
        self.seats_order += self._generate_seats_order_c()
        self.seats_order += self._generate_seats_order_c(102)
        self.seats_order += self._generate_seats_order_c(204)
        self.seats_order += self._generate_seats_order_c(306)
        self.seats_order += self._generate_seats_order_l(438)
        self._move_random_seats_to_end()

    @staticmethod
    def _rotate(points, origin, angle):
        rotated = (points - origin) * np.exp(complex(0, angle)) + origin
        return (rotated.real, rotated.imag)

    def _rotate_sector(self, sector, angle, seat_nr, rotate_by=complex(561, 561), move_by=(0, 0)):
        result = []
        for seat in sector:
            rotated = self._rotate(complex(seat[0], seat[1]), rotate_by, np.deg2rad(angle))
            pos_x = int(math.floor(rotated[0] + move_by[0] + 0.5))
            pos_y = int(math.floor(rotated[1] + move_by[1] + 0.5))
            result.append((pos_x, pos_y, seat_nr))
            seat_nr += 1
        return result

    def _get_center_sectors(self) -> List[tuple]:
        left_center_sector_right = self._rotate_sector(
            self._left_center_sector_left, angle=21, seat_nr=122, move_by=(5, -5)
        )
        left_center_sector = self._left_center_sector + self._left_center_sector_left + left_center_sector_right
        return (
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

    def _get_seat_by_number(self, seat_nr: int) -> Seat:
        for seat in self.seats:
            if seat.number == seat_nr:
                return seat

    def _get_seat_by_sequence(self, seat_nr: int) -> int:
        cnt = 0
        for row in self.seats_order:
            for real_seat_nr in row:
                if seat_nr == cnt:
                    return real_seat_nr - 1
                cnt += 1

    def _get_seats_for_german_minority(self) -> List[int]:
        seats_order = []
        seats_order += self._generate_seats_order_c()
        seats_order += self._generate_seats_order_c(102)
        seats_order += self._generate_seats_order_c(204)
        seats_order += self._generate_seats_order_c(306)
        seats_for_german_minority = []
        for row in seats_order:
            seats_for_german_minority.append(row[-1])
        return seats_for_german_minority

    def _get_seats_fill_colors(self, seats: List[int]) -> List[str]:
        seats_colors = []
        for seat in self.seats:
            if seat.number in seats:
                seats_colors.append(seat.fill)
        return seats_colors

    def _check_for_good_position_for_german_minority(self) -> Optional[int]:
        possible_seats = self._get_seats_for_german_minority()
        possible_seats_f = self._get_seats_fill_colors(possible_seats)
        good_seat = None
        for x in range(1, len(possible_seats) - 1):
            p_f = possible_seats_f[x - 1]
            n_f = possible_seats_f[x + 1]
            if p_f != n_f and "#ffffff" not in [p_f, n_f] and possible_seats_f[x] == "#ffffff":
                good_seat = possible_seats[x]
        return good_seat

    def _get_seat_map(self, parties: List[Party]):
        seat_map = []
        for party in parties:
            for x in range(0, party.seats):
                seat_map.append(party.color)
        return seat_map

    def _get_parties_and_german_minority(self):
        german_minority = None
        if self.parties[-1].name == GERMAN_MINORITY.name:
            parties = self.parties[:-1]
            german_minority = self.parties[-1]
        else:
            parties = self.parties
        return german_minority, parties

    def _clear_colors(self):
        for seat in self.seats:
            seat.reset_colors()

    def _colorize_seats(self, seat_map):
        self._generate_seats_order()
        for y in range(0, len(seat_map)):
            real_y = self._get_seat_by_sequence(y)
            seat = self.seats[real_y]
            self._set_seat_color(seat, seat_map[y])

    def colorize(self):
        german_minority, parties = self._get_parties_and_german_minority()
        seat_map = self._get_seat_map(parties)
        if german_minority:
            good_position = None
            while good_position is None:
                self._clear_colors()
                self._colorize_seats(seat_map)
                good_position = self._check_for_good_position_for_german_minority()
                if good_position:
                    german_minority_seat = self._get_seat_by_number(good_position)
                    self._set_seat_color(german_minority_seat, german_minority.color)
        else:
            self._clear_colors()
            self._colorize_seats(seat_map)

    def colorize_by_sequence(self):
        self._generate_seats_order()
        color = None
        new_color = None
        cnt = 0
        for seats_row in self.seats_order:
            while new_color == color:
                new_color = random.choice(PYRLAMENT_PROPERTIES.COLORS)
            color = new_color
            for seat_number in seats_row:
                seat = self.seats[seat_number - 1]
                self._set_seat_color(seat, color)
                cnt += 1

    def _get_svg(self):
        svg = drawsvg.Drawing(1122, 841, overflow="hidden")
        if self.parties and self.logotype:
            svg.append(self._draw_logotype())
            svg.append(
                drawsvg.Text("https://pyrlament.pl", 15, 100, 130, fill="#000000", center=1, font_family="sans-serif")
            )
        if self.parties and self.legend:
            svg.append(self._draw_legend())
        svg.append(self._draw_seats())
        svg.append(self._draw_caption())
        return svg

    def _draw_seats(self) -> drawsvg.Group:
        seats = drawsvg.Group(transform="translate(0 50)")
        for seat in self.seats:
            if not self._skip_empty_seats or (self._skip_empty_seats and seat.fill != "#ffffff"):
                circle = drawsvg.Circle(seat.cx, seat.cy, 9, fill=seat.fill, stroke="black", stroke_width="0.5")
                seat_number = drawsvg.Text(
                    f"{seat.label}",
                    8,
                    seat.cx,
                    seat.cy,
                    center=0.6,
                    fill=seat.color,
                    text_anchor="middle",
                    font_family="sans-serif",
                )
                seats.append(circle)
                seats.append(seat_number)
        return seats

    def _draw_logotype(self) -> drawsvg.Image:
        return drawsvg.Image(x="0", y="0", width="200", height="115", path=self.logotype, embed=True)

    def _draw_caption(self) -> drawsvg.Text:
        return drawsvg.Text(self.caption, 14, 0, 730, fill="#000000", font_family="sans-serif")

    def _draw_legend(self) -> drawsvg.Group:
        legend = drawsvg.Group(transform="translate(900 20)")
        legend.append(drawsvg.Text("Legenda:", 15, 0, 0, fill="#000000", font_family="sans-serif"))
        cr_x = 20
        cr_y = 20
        for p in self.parties:
            legend.append(drawsvg.Circle(cr_x - 12, cr_y - 3, 5, fill=f"#{p.color}"))
            legend.append(
                drawsvg.Text(
                    f"{p.label} - {p.support}% ({p.seats} {self._get_mandates_label(p.seats)})",
                    9,
                    cr_x,
                    cr_y,
                    fill="#000000",
                    font_family="sans-serif",
                )
            )
            cr_y += 15
        return legend

    @staticmethod
    def _get_mandates_label(seats) -> str:
        if seats == 1:
            return "mandat"
        if 1 < seats < 6 or seats > 20 and str(seats)[-1] in ["2", "3", "4"]:
            return "mandaty"
        return "mandatów"

    def get_svg(self):
        svg = self._get_svg()
        return svg.as_svg()

    def save_svg(self, svg_filename: str):
        svg = self._get_svg()
        svg.save_svg(svg_filename)

    @staticmethod
    def convert_svg_to_png(svg_filename: str, png_filename: str):
        with open(svg_filename, "rb") as svg_file:
            PNGSurface.convert(bytestring=svg_file.read(), width=1122, height=841, write_to=open(png_filename, "wb"))

    @staticmethod
    def hex_to_rgb(h: str) -> tuple:
        return tuple(int(h[i : i + 2], 16) for i in (0, 2, 4))

    @staticmethod
    def invert_rgb(c: tuple) -> tuple:
        return 255 - c[0], 255 - c[1], 255 - c[2]

    @staticmethod
    def rgb_to_hex(rgb: tuple) -> str:
        return "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])
