import pytest
from unittest.mock import patch

from pyrlament import SeatsGenerator
from pyrlament.data import Party


@pytest.fixture
def given_generator():
    return SeatsGenerator(parties=[])


def get_seat_by_number(c, x):
    for s in c:
        if s[2] == x:
            return s


class TestSeatsPositions:
    def test_two_center_columns_seat_y_position(self):
        generator = SeatsGenerator(parties=[])
        center = generator.get_center()
        l1 = [168, 173, 179, 226, 230, 235, 240, 246, 253, 260, 267]
        l2 = [268, 271, 276, 282, 285, 289, 294, 299, 305, 312, 319]
        for x in range(len(l1)):
            seat1 = get_seat_by_number(center, l1[x])
            seat2 = get_seat_by_number(center, l2[x])
            assert seat1[1] == seat2[1]

    def test_last_horizontal_row(self):
        generator = SeatsGenerator(parties=[])
        center = generator.get_center()
        for x in [372, 377, 383, 430, 434, 439, 444, 450, 457, 464, 471]:
            seat = get_seat_by_number(center, x)
            assert seat[1] == 543

    @pytest.mark.parametrize(
        "given_amount,expected_result",
        [
            (1, "mandat"),
            (2, "mandaty"),
            (5, "mandatów"),
            (22, "mandaty"),
            (55, "mandatów"),
        ],
    )
    def test_get_mandates_label(self, given_generator, given_amount, expected_result):
        # When
        result = given_generator._get_mandates_label(given_amount)
        # Then
        assert result == expected_result

    @pytest.mark.parametrize(
        "given_parties,expected_result",
        [
            (
                [
                    Party(name="AAA", support=50, seats=2),
                    Party(name="BBB", support=50, seats=2),
                ],
                4,
            ),
        ],
    )
    @patch("pyrlament.generator.SeatsGenerator._set_seat_color")
    def test_colorize_seats(self, set_seat_color_mock, given_generator, given_parties, expected_result):
        # When
        seats_generator = SeatsGenerator(parties=given_parties)
        seats_generator.colorize()
        # Then
        assert set_seat_color_mock.call_count == expected_result

    def test_seats_placement(self):
        # Given
        given_generator = SeatsGenerator(parties=[])
        seats_numbers = [372, 377, 383, 430, 434, 439, 444, 450, 457, 464, 471]
        # Expected 372-471 Positions
        expected = []
        for x in range(len(seats_numbers)):
            expected.append((677 + x * 43, 543, seats_numbers[x]))
        # When
        for x in range(len(seats_numbers)):
            seat = given_generator._get_seat_by_label(seats_numbers[x])
            # print(expected[x][0], "==", seat.cx, " | ", expected[x][1], "==", seat.cy)
            assert expected[x][0] - seat.cx <= 1
            assert expected[x][0] - seat.cx >= -5
            assert expected[x][1] - seat.cy <= 3
            assert expected[x][1] - seat.cy >= -1

    @pytest.mark.parametrize(
        "seats_numbers",
        [
            ([34, 35, 36]),
            ([34, 37, 40, 43, 46]),
            ([63, 60, 57]),
            ([64, 65, 66]),
            ([67, 68, 69, 70, 71]),
            ([72, 73, 74, 75, 76, 77]),
            ([78, 79, 80]),
            ([370, 371, 372]),
        ],
    )
    def test_seats_in_line(self, seats_numbers):
        # Given
        print()
        print(seats_numbers)
        given_generator = SeatsGenerator(parties=[])
        # When
        seat_positions = []
        for x in range(len(seats_numbers)):
            seat = given_generator._get_seat_by_label(seats_numbers[x])
            seat_positions.append((seat.cx, seat.cy))
        # Then
        start = seat_positions.pop(0)
        end = seat_positions.pop(-1)
        for x in range(len(seat_positions)):
            x1 = round((end[0] - start[0]) / (len(seat_positions) + 1))
            y1 = round((end[1] - start[1]) / (len(seat_positions) + 1))
            expected = (start[0] + x1 * (x + 1), start[1] + y1 * (x + 1))
            print(seat_positions[x])
            print(expected)
            assert seat_positions[x] == expected
