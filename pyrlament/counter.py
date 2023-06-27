from typing import List

from pyrlament.data import Party, Election


class SeatsCounter:
    election: Election

    def __init__(self, parties: List[Party]):
        self.election = Election(parties=parties)

    def count(self):
        pass
