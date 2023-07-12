from pyrlament.data import PartySupport, PartySupportList, sg


class TestData:
    def test_support_generator(self):
        expected = [
            PartySupport(name="A", support=50, year=2000),
            PartySupport(name="B", support=25, year=2000),
            PartySupport(name="C", support=12.5, year=2000),
        ]
        result = sg(year=2000, support={"A": 50, "B": 25, "C": 12.5})
        assert result, expected

    def test_create_party_support_list(self):
        list_1 = PartySupportList(
            2019,
            {
                "PiS": 43.59,
                "KO": 27.4,
                "Lewica": 12.56,
                "PSL": 8.55,
                "Konfederacja": 6.81,
            },
        )
        print(list_1)
