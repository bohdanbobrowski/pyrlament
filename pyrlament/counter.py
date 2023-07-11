from typing import List, Dict

from pyrlament.data import (
    DEPUTIES,
    DISTRICTS,
    GENERAL_SUPPORT,
    GERMAN_MINORITY,
    District,
    Party,
)


class SeatsCounter:
    parties: List[Party]
    include_german_minority: bool = True
    districts: List[District] = []

    def __init__(self, parties: List[Party]):
        self.parties = parties

    def _get_german_minority(self):
        if self.include_german_minority:
            if GERMAN_MINORITY not in self.parties:
                self.parties.append(GERMAN_MINORITY)

    def _update_district_support(self) -> Dict:
        district_support = {}
        for party_name in GENERAL_SUPPORT:
            pass
        for district in DISTRICTS:
            pass
        return district_support

    def _calculate_deputies_seats(self):
        for party in self.parties:
            party.seats = DEPUTIES

    def count(self):
        self._update_district_support()
        self._calculate_deputies_seats()
        self._get_german_minority()
