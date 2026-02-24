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
        seats_numbers_2 = [None, 472, 475, 478, 481, 484, 487, 490, 493, 496, 499]
        # When
        x_list = []
        x_list_2 = []
        y_list = []
        y_list_2 = []
        for label in seats_numbers:
            seat = given_generator._get_seat_by_label(label)
            x_list.append(seat.cx)
            y_list.append(seat.cy)
        for label in seats_numbers_2:
            if label:
                seat = given_generator._get_seat_by_label(label)
                x_list_2.append(seat.cx)
                y_list_2.append(seat.cy)
            else:
                x_list_2.append(None)
                y_list_2.append(None)
        # Then
        print()
        print(y_list)
        print(y_list_2)
        print(x_list)
        print(x_list_2)

        # Expected 372-471 Positions
        expected = []
        for x in range(len(x_list)):
            expected.append((543, 677+x*43))
        print(expected)

        for y in y_list:
            pass
            # assert y == y_list[0]
        for i in range(0, len(x_list_2) - 1):
            pass
            # assert x_list[i] == x_list[i+1] - 43
            # assert x_list_2[i] == x_list_2[i+1] - 43
