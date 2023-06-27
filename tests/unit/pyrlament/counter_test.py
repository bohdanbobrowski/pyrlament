from pyrlament.counter import SeatsCounter
from pyrlament.data import DEPUTIES, Party


class TestSeatsCounter:
    def test_count_one_takes_all(self):
        parties = [Party(name="A", votes=100.0)]
        election = SeatsCounter(parties=parties)
        election.count()
        assert election.parties[0].seats == DEPUTIES

    def test_count_2019_election(self):
        pass
