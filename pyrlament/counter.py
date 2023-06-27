from typing import List

from pyrlament.data import DEPUTIES, Party


class SeatsCounter:
    parties: List[Party]

    def __init__(self, parties: List[Party]):
        self.parties = parties

    def count(self):
        for party in self.parties:
            party.seats = DEPUTIES
