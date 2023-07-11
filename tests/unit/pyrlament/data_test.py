from pyrlament.data import ArchivalSupport, sg


class TestData:
    def test_support_generator(self):
        expected = [
            ArchivalSupport(name="A", support=50, year=2000),
            ArchivalSupport(name="B", support=25, year=2000),
            ArchivalSupport(name="C", support=12.5, year=2000),
        ]
        result = sg(year=2000, support={"A": 50, "B": 25, "C": 12.5})
        assert result, expected
