import math

from pyrlament.data import DISTRICTS, GENERAL_SUPPORT, GERMAN_MINORITY, District, Party


class SeatsCounterException(Exception):
    pass


class SeatsCounter:
    parties: list[Party]
    past_support: bool
    include_german_minority: bool = True
    districts: list[District] = []

    def __init__(self, parties: list[Party], past_support=None, include_german_minority=True):
        self.parties = parties
        self.include_german_minority = include_german_minority
        if past_support is not None:
            self.past_support = past_support
        else:
            if len(parties) == 5:
                self.past_support = True
            else:
                self.past_support = False
        self._check_total_support()
        self._set_given_order()

    def _get_german_minority(self):
        if self.include_german_minority:
            if GERMAN_MINORITY not in self.parties:
                self.parties.append(GERMAN_MINORITY)

    def _set_given_order(self):
        """This method sets given order if none is set."""
        if sum([p.order for p in self.parties]) == 0:
            for i in range(0, len(self.parties)):
                self.parties[i].order = i

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
                    if sup.name == party.name and self.past_support:
                        past_support = sup.support
                p_sup = d.get_support(party.name)
                if party.support >= party.threshold:
                    if p_sup and past_support > 0:
                        new_district.add_support(
                            party_name=party.name,
                            party_support=party.support / past_support * p_sup.support,
                        )
                    else:
                        new_district.add_support(party_name=party.name, party_support=party.support)
            self.districts.append(new_district)

    def _check_total_support(self):
        total_support = math.fsum([p.support for p in self.parties])
        if total_support > 100:
            raise SeatsCounterException(f"Total support exceeds 100%! ({total_support})")

    def _get_party_votes(self, district: District) -> dict:
        output = {}
        for party in self.parties:
            party_support_in_district = district.get_support(party_name=party.name)
            if party_support_in_district:
                party_votes = party_support_in_district.support * district.votes / 100
                output[party.name] = int(math.floor(party_votes + 0.5))
        return output

    def _calculate_candidates_votes(
        self,
    ):
        for district in self.districts:
            for party_support in district.support:
                for i in range(1, district.mandates + 1):
                    votes = party_support.votes / i
                    votes = int(math.floor(votes + 0.5))
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
                district.set_seats(party_name=party_name, seats=party_support[party_name])
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

    def sort_parties_by_support(self, reverse: bool = True):
        self.parties.sort(key=lambda x: x.support, reverse=reverse)

    def sort_parties_by_seats(self, reverse: bool = True):
        self.parties.sort(key=lambda x: x.seats, reverse=reverse)  # type: ignore

    def sort_parties_by_order(self, reverse: bool = False):
        self.parties.sort(key=lambda x: x.order, reverse=reverse)

    def count(self):
        self._update_district_support()
        self._calculate_deputies_seats()
        self._get_german_minority()
