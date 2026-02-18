import pytest


from pyrlament import SeatsGenerator


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
