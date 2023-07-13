from typing import Dict, List

from pyrlament.data import DISTRICTS, GENERAL_SUPPORT, GERMAN_MINORITY, District, Party


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

    def _update_district_support(self):
        self.districts = []
        for d in DISTRICTS:
            new_district = District(
                mandates=d.mandates,
                votes=d.votes,
                capital=d.capital,
                voivodeship=d.voivodeship,
                support=[],
            )
            past_support = 0
            for party in self.parties:
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
                        party_name=party.name, party_support=party.support
                    )
            self.districts.append(new_district)

    def _get_party_votes(self, district: District) -> Dict:
        output = {}
        for party in self.parties:
            party_support_in_district = district.get_support(party_name=party.name)
            output[party.name] = round(
                party_support_in_district.support * district.votes / 100, 0
            )
        return output

    def _calculate_candidates_votes(
        self,
    ):
        for district in self.districts:
            for party_support in district.support:
                for i in range(1, district.mandates + 1):
                    votes = round(party_support.votes / i)
                    party_support.add_candidate_vote(party_support.name, votes)
                    district.add_candidate_vote(party_support.name, votes)
                party_support.sort_candidates_votes()
            district.sort_candidates_votes()

    def _calculate_mandates(self):
        total_party_support = {}
        for district in self.districts:
            party_support = {}
            for cv in district.candidates_votes:
                if cv.party_name not in party_support:
                    party_support[cv.party_name] = 0
                    if cv.party_name not in total_party_support:
                        total_party_support[cv.party_name] = 0
                party_support[cv.party_name] += 1
                total_party_support[cv.party_name] += 1
            for party_name in party_support:
                district.set_seats(
                    party_name=party_name, seats=party_support[party_name]
                )
        for party in self.parties:
            if party.name in total_party_support:
                party.seats = total_party_support[party.name]
            else:
                party.seats = 0

    def _calculate_deputies_seats(self):
        for district in self.districts:
            party_votes = self._get_party_votes(district)
            for party_name in party_votes:
                district.set_votes(party_name=party_name, votes=party_votes[party_name])
        self._calculate_candidates_votes()
        self._calculate_mandates()

    def count(self):
        self._update_district_support()
        self._calculate_deputies_seats()
        self._get_german_minority()
        pass
