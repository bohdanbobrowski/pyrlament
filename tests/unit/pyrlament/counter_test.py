from pyrlament.counter import SeatsCounter
from pyrlament.data import DEPUTIES, DISTRICTS, Party


class TestSeatsCounter:
    def test_count_one_takes_all(self):
        parties = [Party(name="A", votes=100.0)]
        election = SeatsCounter(parties=parties)
        election.count()
        assert election.parties[0].seats == DEPUTIES

    def test_get_german_minority(self):
        parties = [Party(name="A", votes=100.0)]
        election = SeatsCounter(parties=parties)
        election._get_german_minority()
        election._get_german_minority()
        assert len(election.parties) == 2

    def test_count_2019_election(self):
        parties = [
            Party(name="PiS", votes=43.59),
            Party(name="KO", votes=27.4),
            Party(name="SLD", votes=12.56),
            Party(name="PSL", votes=8.55),
            Party(name="KWIN", votes=6.81),
        ]
        election = SeatsCounter(parties=parties)
        election.count()
        expected = {
            "PiS": 235,
            "KO": 134,
            "SLD": 49,
            "PSL": 30,
            "KWIN": 11,
        }
        for party in election.parties:
            assert party.seats == expected[party.name]

    def test_districts(self):
        """This test is awkward."""
        assert len(DISTRICTS), 41
