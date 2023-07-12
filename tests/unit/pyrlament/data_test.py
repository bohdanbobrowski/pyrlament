from pyrlament.data import PartySupport, PartySupportList


class TestData:
    def test_support_generator(self):
        expected = [
            PartySupport(name="A", support=50, year=2000),
            PartySupport(name="B", support=25, year=2000),
            PartySupport(name="C", support=12.5, year=2000),
        ]
        result = (2000, {"A": 50, "B": 25, "C": 12.5})
        assert result, expected

    def test_create_party_support_list(self):
        list_1 = PartySupportList.load(
            {
                "PiS": 43.59,
                "KO": 27.4,
                "Lewica": 12.56,
                "PSL": 8.55,
                "Konfederacja": 6.81,
            },
            2019,
        )
        assert len(list_1), 5
        assert list[-1], PartySupport(name="Konfederacja", support=6.81, year=2019)
