from typing import List

from pyrlament.data import DEPUTIES, GERMAN_MINORITY, Party


class SeatsCounter:
    parties: List[Party]
    include_german_minority: bool = True

    def __init__(self, parties: List[Party]):
        self.parties = parties

    def _get_german_minority(self):
        if self.include_german_minority:
            if GERMAN_MINORITY not in self.parties:
                self.parties.append(GERMAN_MINORITY)

    def count(self):
        for party in self.parties:
            party.seats = DEPUTIES
        self._get_german_minority()
