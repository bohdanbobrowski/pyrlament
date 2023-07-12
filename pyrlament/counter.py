from typing import List

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
    districts_updated: List[District] = []

    def __init__(self, parties: List[Party]):
        self.parties = parties

    def _get_german_minority(self):
        if self.include_german_minority:
            if GERMAN_MINORITY not in self.parties:
                self.parties.append(GERMAN_MINORITY)

    def _update_district_support(self) -> List:
        self.districts_updated = []
        for d in DISTRICTS:
            new_district = District(
                mandates=d.mandates,
                votes=d.votes,
                capital=d.capital,
                voivodeship=d.voivodeship,
            )
            for party in self.parties:
                past_support = 0
                for sup in GENERAL_SUPPORT:
                    if sup.name == party.name:
                        past_support = sup.support
                p_sup = d.get_support(party.name)
                new_district.add_support(
                    party_name=party.name,
                    party_support=party.support / past_support * p_sup.support,
                )
            self.districts_updated.append(new_district)

    def _calculate_deputies_seats(self):
        for party in self.parties:
            party.seats = DEPUTIES

    def count(self):
        self._update_district_support()
        self._calculate_deputies_seats()
        self._get_german_minority()
