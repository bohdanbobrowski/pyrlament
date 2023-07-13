import unittest

from pyrlament.counter import SeatsCounter
from pyrlament.data import DEPUTIES, DISTRICTS, Candidate, Party


class TestSeatsCounter(unittest.TestCase):
    def test_count_one_takes_all(self):
        parties = [Party(name="PiS", support=100.0)]
        election = SeatsCounter(parties=parties)
        election.count()
        assert election.parties[0].seats == DEPUTIES

    def test_get_german_minority(self):
        parties = [Party(name="A", support=100.0)]
        election = SeatsCounter(parties=parties)
        election._get_german_minority()
        election._get_german_minority()
        assert len(election.parties) == 2

    def test_count_2019_election(self):
        parties = [
            Party(name="PiS", support=43.59, threshold=8),
            Party(name="KO", support=27.4, threshold=8),
            Party(name="SLD", support=12.56),
            Party(name="PSL", support=8.55),
            Party(name="Konfederacja", support=6.81),
        ]
        election = SeatsCounter(parties=parties)
        election.count()
        expected = {
            "PiS": 235,
            "KO": 134,
            "SLD": 49,
            "PSL": 30,
            "Konfederacja": 11,
        }
        all_seats = 0
        for party in election.parties:
            all_seats += party.seats
        assert all_seats, DEPUTIES
        for party in election.parties:
            assert party.seats == expected[party.name]

    def test_district_support(self):
        # given
        parties = [
            Party(name="PiS", support=43.59),
            Party(name="KO", support=27.4),
            Party(name="SLD", support=12.56),
            Party(name="PSL", support=8.55),
            Party(name="Konfederacja", support=6.81),
        ]
        expected_district_support = [
            {
                "PiS": 42.40,
                "KO": 25.02,
                "Lewica": 16.43,
                "PSL": 7.17,
                "Konfederacja": 5.85,
                "PL2050": 0,
            },
            {
                "PiS": 40.54,
                "KO": 32.09,
                "Lewica": 12.53,
                "PSL": 7.25,
                "Konfederacja": 5.42,
                "PL2050": 0,
            },
            {
                "PiS": 34.67,
                "KO": 32.80,
                "Lewica": 15.41,
                "PSL": 6.46,
                "Konfederacja": 7.45,
                "PL2050": 0,
            },
            {
                "PiS": 36.43,
                "KO": 31.05,
                "Lewica": 15.17,
                "PSL": 9.02,
                "Konfederacja": 7.05,
                "PL2050": 0,
            },
            {
                "PiS": 40.38,
                "KO": 26.42,
                "Lewica": 14.83,
                "PSL": 10.88,
                "Konfederacja": 6.33,
                "PL2050": 0,
            },
            {
                "PiS": 55.39,
                "KO": 19.30,
                "Lewica": 9.10,
                "PSL": 7.81,
                "Konfederacja": 7.07,
                "PL2050": 0,
            },
            {
                "PiS": 59.50,
                "KO": 14.80,
                "Lewica": 6.83,
                "PSL": 11.86,
                "Konfederacja": 5.84,
                "PL2050": 0,
            },
            {
                "PiS": 34.30,
                "KO": 31.27,
                "Lewica": 15.61,
                "PSL": 11.63,
                "Konfederacja": 7.19,
                "PL2050": 0,
            },
            {
                "PiS": 32.90,
                "KO": 35.82,
                "Lewica": 20.10,
                "PSL": 4.53,
                "Konfederacja": 6.65,
                "PL2050": 0,
            },
            {
                "PiS": 56.21,
                "KO": 15.64,
                "Lewica": 10.95,
                "PSL": 10.44,
                "Konfederacja": 6.76,
                "PL2050": 0,
            },
            {
                "PiS": 49.81,
                "KO": 20.48,
                "Lewica": 11.98,
                "PSL": 10.29,
                "Konfederacja": 5.88,
                "PL2050": 0,
            },
            {
                "PiS": 53.48,
                "KO": 23.04,
                "Lewica": 8.51,
                "PSL": 7.90,
                "Konfederacja": 7.06,
                "PL2050": 0,
            },
            {
                "PiS": 39.56,
                "KO": 30.48,
                "Lewica": 13.01,
                "PSL": 7.27,
                "Konfederacja": 7.99,
                "PL2050": 0,
            },
            {
                "PiS": 65.80,
                "KO": 13.83,
                "Lewica": 6.07,
                "PSL": 7.35,
                "Konfederacja": 6.95,
                "PL2050": 0,
            },
            {
                "PiS": 59.59,
                "KO": 14.00,
                "Lewica": 5.94,
                "PSL": 13.35,
                "Konfederacja": 7.11,
                "PL2050": 0,
            },
            {
                "PiS": 52.45,
                "KO": 16.85,
                "Lewica": 8.76,
                "PSL": 15.17,
                "Konfederacja": 5.24,
                "PL2050": 0,
            },
            {
                "PiS": 57.82,
                "KO": 17.15,
                "Lewica": 7.43,
                "PSL": 10.20,
                "Konfederacja": 5.89,
                "PL2050": 0,
            },
            {
                "PiS": 59.76,
                "KO": 13.94,
                "Lewica": 6.45,
                "PSL": 11.94,
                "Konfederacja": 6.49,
                "PL2050": 0,
            },
            {
                "PiS": 27.49,
                "KO": 42.05,
                "Lewica": 18.19,
                "PSL": 4.75,
                "Konfederacja": 7.51,
                "PL2050": 0,
            },
            {
                "PiS": 40.89,
                "KO": 28.61,
                "Lewica": 13.09,
                "PSL": 8.60,
                "Konfederacja": 6.63,
                "PL2050": 0,
            },
            {
                "PiS": 37.64,
                "KO": 26.71,
                "Lewica": 11.74,
                "PSL": 10.31,
                "Konfederacja": 5.70,
                "PL2050": 0,
            },
            {
                "PiS": 63.36,
                "KO": 15.94,
                "Lewica": 6.04,
                "PSL": 7.85,
                "Konfederacja": 6.81,
                "PL2050": 0,
            },
            {
                "PiS": 62.38,
                "KO": 14.39,
                "Lewica": 6.59,
                "PSL": 7.79,
                "Konfederacja": 8.25,
                "PL2050": 0,
            },
            {
                "PiS": 52.04,
                "KO": 21.04,
                "Lewica": 9.09,
                "PSL": 9.33,
                "Konfederacja": 6.96,
                "PL2050": 0,
            },
            {
                "PiS": 32.10,
                "KO": 41.31,
                "Lewica": 13.47,
                "PSL": 5.90,
                "Konfederacja": 7.21,
                "PL2050": 0,
            },
            {
                "PiS": 36.43,
                "KO": 35.85,
                "Lewica": 12.47,
                "PSL": 7.94,
                "Konfederacja": 7.30,
                "PL2050": 0,
            },
            {
                "PiS": 46.76,
                "KO": 27.20,
                "Lewica": 11.48,
                "PSL": 7.13,
                "Konfederacja": 7.48,
                "PL2050": 0,
            },
            {
                "PiS": 44.28,
                "KO": 22.63,
                "Lewica": 15.59,
                "PSL": 8.68,
                "Konfederacja": 6.07,
                "PL2050": 0,
            },
            {
                "PiS": 37.75,
                "KO": 32.61,
                "Lewica": 13.38,
                "PSL": 5.99,
                "Konfederacja": 7.67,
                "PL2050": 0,
            },
            {
                "PiS": 48.28,
                "KO": 27.71,
                "Lewica": 9.68,
                "PSL": 5.64,
                "Konfederacja": 7.17,
                "PL2050": 0,
            },
            {
                "PiS": 39.19,
                "KO": 37.20,
                "Lewica": 11.92,
                "PSL": 4.37,
                "Konfederacja": 7.33,
                "PL2050": 0,
            },
            {
                "PiS": 37.13,
                "KO": 29.66,
                "Lewica": 21.90,
                "PSL": 4.85,
                "Konfederacja": 6.45,
                "PL2050": 0,
            },
            {
                "PiS": 55.18,
                "KO": 16.65,
                "Lewica": 9.95,
                "PSL": 9.88,
                "Konfederacja": 5.95,
                "PL2050": 0,
            },
            {
                "PiS": 40.86,
                "KO": 28.43,
                "Lewica": 11.64,
                "PSL": 10.89,
                "Konfederacja": 5.66,
                "PL2050": 0,
            },
            {
                "PiS": 38.82,
                "KO": 26.46,
                "Lewica": 13.84,
                "PSL": 13.19,
                "Konfederacja": 6.97,
                "PL2050": 0,
            },
            {
                "PiS": 42.48,
                "KO": 24.72,
                "Lewica": 13.43,
                "PSL": 12.80,
                "Konfederacja": 6.57,
                "PL2050": 0,
            },
            {
                "PiS": 47.29,
                "KO": 20.48,
                "Lewica": 15.04,
                "PSL": 9.81,
                "Konfederacja": 6.74,
                "PL2050": 0,
            },
            {
                "PiS": 35.64,
                "KO": 30.60,
                "Lewica": 13.28,
                "PSL": 13.86,
                "Konfederacja": 6.62,
                "PL2050": 0,
            },
            {
                "PiS": 25.33,
                "KO": 45.38,
                "Lewica": 16.49,
                "PSL": 6.20,
                "Konfederacja": 6.61,
                "PL2050": 0,
            },
            {
                "PiS": 36.83,
                "KO": 32.31,
                "Lewica": 15.44,
                "PSL": 9.43,
                "Konfederacja": 5.98,
                "PL2050": 0,
            },
            {
                "PiS": 35.11,
                "KO": 35.71,
                "Lewica": 15.25,
                "PSL": 7.40,
                "Konfederacja": 6.53,
                "PL2050": 0,
            },
        ]
        # when
        election = SeatsCounter(parties=parties)
        election.count()
        # then
        assert len(expected_district_support), len(election.districts)
        for i in range(0, len(expected_district_support)):
            expected = expected_district_support[i]
            given = election.districts[i]
            for given_p in given.support:
                assert given_p.support, expected[given_p.name]

    def test_district_support_votes(self):
        # given
        parties = [
            Party(name="PiS", support=43.59, threshold=8),
            Party(name="KO", support=27.4, threshold=8),
            Party(name="SLD", support=12.56),
            Party(name="PSL", support=8.55),
            Party(name="Konfederacja", support=6.81),
        ]
        expected_candidates_votes = [
            [
                Candidate(party_name="PiS", votes=183353),
                Candidate(party_name="KO", votes=108195),
                Candidate(party_name="PiS", votes=91676),
                Candidate(party_name="PiS", votes=61118),
                Candidate(party_name="SLD", votes=54314),
                Candidate(party_name="KO", votes=54098),
                Candidate(party_name="PiS", votes=45838),
                Candidate(party_name="PiS", votes=36671),
                Candidate(party_name="KO", votes=36065),
                Candidate(party_name="PSL", votes=31006),
                Candidate(party_name="PiS", votes=30559),
                Candidate(party_name="SLD", votes=27157),
            ]
        ]
        # when
        election = SeatsCounter(parties=parties)
        election.count()
        # then
        # assert len(expected_candidates_votes), len(election.districts)
        for i in range(0, len(expected_candidates_votes)):
            expected = expected_candidates_votes[i]
            given = election.districts[i]
            for expected_candidate in expected:
                self.assertIn(expected_candidate, given.candidates_votes)

    def test_districts(self):
        """This test is awkward."""
        assert len(DISTRICTS), 41
