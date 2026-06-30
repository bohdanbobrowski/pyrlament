from pyrlament.data import PartySupport, PartySupportList
import pytest


class TestData:
    def test_support_generator(self):
        expected = [
            PartySupport(name="A", support=50, year=2000),
            PartySupport(name="B", support=25, year=2000),
            PartySupport(name="C", support=12.5, year=2000),
        ]
        result = (2000, {"A": 50, "B": 25, "C": 12.5})
        assert result, expected

    @pytest.mark.parametrize(
        "year,pis,ko,lewica,psl,konfederacja",
        [
            (2019, 43.59, 27.4, 12.56, 8.55, 6.81),
        ],
    )
    def test_create_party_support_list(self, year, pis, ko, lewica, psl, konfederacja):
        list_1 = PartySupportList.load(
            {
                "PiS": pis,
                "KO": ko,
                "Lewica": lewica,
                "PSL": psl,
                "Konfederacja": konfederacja,
            },
            year,
        )
        assert len(list_1), 5
        assert list_1[-1], PartySupport(name="Konfederacja", support=konfederacja, year=year)
