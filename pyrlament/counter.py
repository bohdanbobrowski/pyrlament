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
    districts_updated: List[District] = []

    def __init__(self, parties: List[Party]):
        self.parties = parties

    def _get_german_minority(self):
        if self.include_german_minority:
            if GERMAN_MINORITY not in self.parties:
                self.parties.append(GERMAN_MINORITY)

    def _update_district_support(self):
        self.districts_updated = []
        for d in DISTRICTS:
            new_district = District(
                mandates=d.mandates,
                votes=d.votes,
                capital=d.capital,
                voivodeship=d.voivodeship,
                support=[],
            )
            for party in self.parties:
                past_support = 0
                for sup in GENERAL_SUPPORT:
                    if sup.name == party.name:
                        past_support = sup.support
                p_sup = d.get_support(party.name)
                if p_sup and past_support > 0:
                    new_district.add_support(
                        party_name=party.name,
                        party_support=party.support / past_support * p_sup.support,
                    )
                else:
                    new_district.add_support(
                        party_name=party.name,
                        party_support=party.support
                    )
            self.districts_updated.append(new_district)

    def _get_party_votes(self, district: District) -> Dict:
        output = {}
        for party in self.parties:
            party_support_in_district = district.get_support(party_name=party.name)
            output[party.name] = round(party_support_in_district.support * district.votes / 100, 0)
        return output

    def _calculate_deputies_seats(self):
        for district in self.districts_updated:
            party_votes = self._get_party_votes(district)


        for party in self.parties:
            party.seats = DEPUTIES

    def count(self):
        self._update_district_support()
        self._calculate_deputies_seats()
        self._get_german_minority()
