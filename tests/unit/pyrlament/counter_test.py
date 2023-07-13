import json
import unittest

from pyrlament.configs import PYRLAMENT_PROPERTIES
from pyrlament.counter import SeatsCounter
from pyrlament.data import DISTRICTS, Candidate, Party

PARTIES_2019 = [
    Party(name="PiS", support=43.59, threshold=8),
    Party(name="KO", support=27.4, threshold=8),
    Party(name="Lewica", support=12.56),
    Party(name="PSL", support=8.55),
    Party(name="Konfederacja", support=6.81),
]


class TestSeatsCounter(unittest.TestCase):
    def test_count_one_takes_all(self):
        parties = [Party(name="PiS", support=100.0)]
        election = SeatsCounter(parties=parties)
        election.count()
        total_seats = sum(p.seats for p in election.parties)
        assert total_seats == PYRLAMENT_PROPERTIES.DEPUTIES

    def test_get_german_minority(self):
        parties = [Party(name="A", support=100.0)]
        election = SeatsCounter(parties=parties)
        election._get_german_minority()
        election._get_german_minority()
        assert len(election.parties) == 2

    def test_count_2019_election(self):
        election = SeatsCounter(parties=PARTIES_2019)
        election.count()
        expected = {
            "PiS": 235,
            "KO": 134,
            "Lewica": 49,
            "PSL": 30,
            "Konfederacja": 11,
            "Mniejszość niemiecka": 1,
        }
        all_seats = 0
        for party in election.parties:
            all_seats += party.seats
        assert all_seats, PYRLAMENT_PROPERTIES.DEPUTIES
        for party in election.parties:
            assert party.seats == expected[party.name]

    def test_district_support(self):
        # given
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
        election = SeatsCounter(parties=PARTIES_2019)
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
        expected_candidates_votes = [[['PiS', 183353], ['KO', 108195], ['PiS', 91676], ['Lewica', 71049], ['PiS', 61118], ['KO', 54098], ['PiS', 45838], ['PiS', 36671], ['KO', 36065], ['Lewica', 35524], ['PSL', 31006], ['PiS', 30559]], [['PiS', 114729], ['KO', 90815], ['PiS', 57364], ['KO', 45408], ['PiS', 38243], ['Lewica', 35460], ['KO', 30272], ['PiS', 28682]], [['PiS', 226900], ['KO', 214661], ['PiS', 113450], ['KO', 107330], ['Lewica', 100852], ['PiS', 75633], ['KO', 71554], ['PiS', 56725], ['KO', 53665], ['Lewica', 50426], ['Konfederacja', 48757], ['PiS', 45380], ['KO', 42932], ['PSL', 42278]], [['PiS', 167571], ['KO', 142824], ['PiS', 83786], ['KO', 71412], ['Lewica', 69779], ['PiS', 55857], ['KO', 47608], ['PiS', 41893], ['PSL', 41490], ['KO', 35706], ['Lewica', 34890], ['PiS', 33514]], [['PiS', 182651], ['KO', 119506], ['PiS', 91326], ['Lewica', 67081], ['PiS', 60884], ['KO', 59753], ['PSL', 49214], ['PiS', 45663], ['KO', 39835], ['PiS', 36530], ['Lewica', 33540], ['PiS', 30442], ['KO', 29876]], [['PiS', 313284], ['PiS', 156642], ['KO', 109160], ['PiS', 104428], ['PiS', 78321], ['PiS', 62657], ['KO', 54580], ['PiS', 52214], ['Lewica', 51469], ['PiS', 44755], ['PSL', 44173], ['Konfederacja', 39988], ['PiS', 39160], ['KO', 36387], ['PiS', 34809]], [['PiS', 238784], ['PiS', 119392], ['PiS', 79595], ['PiS', 59696], ['KO', 59395], ['PiS', 47757], ['PSL', 47596], ['PiS', 39797], ['PiS', 34112], ['PiS', 29848], ['KO', 29698], ['Lewica', 27410]], [['PiS', 150206], ['KO', 136937], ['PiS', 75103], ['KO', 68468], ['Lewica', 68359], ['PSL', 50930], ['PiS', 50069], ['KO', 45646], ['PiS', 37552], ['KO', 34234], ['Lewica', 34180], ['Konfederacja', 31486]], [['KO', 148846], ['PiS', 136713], ['Lewica', 83524], ['KO', 74423], ['PiS', 68356], ['KO', 49615], ['PiS', 45571], ['Lewica', 41762], ['KO', 37212], ['PiS', 34178]], [['PiS', 194670], ['PiS', 97335], ['PiS', 64890], ['KO', 54165], ['PiS', 48668], ['PiS', 38934], ['Lewica', 37923], ['PSL', 36156], ['PiS', 32445]], [['PiS', 258700], ['PiS', 129350], ['PiS', 86233], ['KO', 71981], ['PiS', 64675], ['PiS', 51740], ['Lewica', 50396], ['PSL', 48049], ['PiS', 43117], ['PiS', 36957], ['KO', 35990], ['PiS', 32338]], [['PiS', 157506], ['PiS', 78753], ['KO', 64761], ['PiS', 52502], ['PiS', 39376], ['Lewica', 37882], ['PSL', 32538], ['KO', 32380]], [['PiS', 256858], ['KO', 197903], ['PiS', 128429], ['KO', 98952], ['PiS', 85619], ['Lewica', 84472], ['KO', 65968], ['PiS', 64214], ['Konfederacja', 51878], ['PiS', 51372], ['KO', 49476], ['PSL', 47203], ['PiS', 42810], ['Lewica', 42236]], [['PiS', 243591], ['PiS', 121796], ['PiS', 81197], ['PiS', 60898], ['KO', 51199], ['PiS', 48718], ['PiS', 40598], ['PiS', 34799], ['PiS', 30449], ['PSL', 27210]], [['PiS', 206830], ['PiS', 103415], ['PiS', 68943], ['PiS', 51708], ['KO', 48592], ['PSL', 46336], ['PiS', 41366], ['PiS', 34472], ['PiS', 29547]], [['PiS', 194359], ['PiS', 97180], ['PiS', 64786], ['KO', 62440], ['PSL', 56214], ['PiS', 48590], ['PiS', 38872], ['Lewica', 32461], ['PiS', 32393], ['KO', 31220]], [['PiS', 193702], ['PiS', 96851], ['PiS', 64567], ['KO', 57454], ['PiS', 48426], ['PiS', 38740], ['PSL', 34171], ['PiS', 32284], ['KO', 28727]], [['PiS', 270657], ['PiS', 135328], ['PiS', 90219], ['PiS', 67664], ['KO', 63135], ['PiS', 54131], ['PSL', 54077], ['PiS', 45110], ['PiS', 38665], ['PiS', 33832], ['KO', 31568], ['PiS', 30073]], [['KO', 581096], ['PiS', 379889], ['KO', 290548], ['Lewica', 251371], ['KO', 193699], ['PiS', 189944], ['KO', 145274], ['PiS', 126630], ['Lewica', 125686], ['KO', 116219], ['Konfederacja', 103782], ['KO', 96849], ['PiS', 94972], ['Lewica', 83790], ['KO', 83014], ['PiS', 75978], ['KO', 72637], ['PSL', 65641], ['KO', 64566], ['PiS', 63315]], [['PiS', 244819], ['KO', 171296], ['PiS', 122410], ['KO', 85648], ['PiS', 81606], ['Lewica', 78373], ['PiS', 61205], ['KO', 57099], ['PSL', 51491], ['PiS', 48964], ['KO', 42824], ['PiS', 40803]], [['PiS', 152984], ['KO', 108560], ['PiS', 76492], ['KO', 54280], ['PiS', 50995], ['Lewica', 47716], ['PSL', 41904], ['PiS', 38246], ['KO', 36187], ['PiS', 30597], ['KO', 27140]], [['PiS', 247472], ['PiS', 123736], ['PiS', 82491], ['KO', 62259], ['PiS', 61868], ['PiS', 49494], ['PiS', 41245], ['PiS', 35353], ['KO', 31130], ['PiS', 30934], ['PSL', 30661]], [['PiS', 367285], ['PiS', 183642], ['PiS', 122428], ['PiS', 91821], ['KO', 84726], ['PiS', 73457], ['PiS', 61214], ['PiS', 52469], ['Konfederacja', 48575], ['PiS', 45911], ['PSL', 45866], ['KO', 42363], ['PiS', 40809], ['Lewica', 38801], ['PiS', 36728]], [['PiS', 270909], ['PiS', 135454], ['KO', 109530], ['PiS', 90303], ['PiS', 67727], ['KO', 54765], ['PiS', 54182], ['PSL', 48570], ['Lewica', 47321], ['PiS', 45152], ['PiS', 38701], ['KO', 36510], ['Konfederacja', 36232], ['PiS', 33864]], [['KO', 218459], ['PiS', 169754], ['KO', 109230], ['PiS', 84877], ['KO', 72820], ['Lewica', 71233], ['PiS', 56585], ['KO', 54615], ['KO', 43692], ['PiS', 42438], ['Konfederacja', 38129], ['KO', 36410]], [['PiS', 211557], ['KO', 208189], ['PiS', 105778], ['KO', 104094], ['Lewica', 72416], ['PiS', 70519], ['KO', 69396], ['PiS', 52889], ['KO', 52047], ['PSL', 46109], ['Konfederacja', 42393], ['PiS', 42311], ['KO', 41638], ['Lewica', 36208]], [['PiS', 182016], ['KO', 105878], ['PiS', 91008], ['PiS', 60672], ['KO', 52939], ['PiS', 45504], ['Lewica', 44687], ['PiS', 36403], ['KO', 35293]], [['PiS', 125984], ['KO', 64386], ['PiS', 62992], ['Lewica', 44356], ['PiS', 41995], ['KO', 32193], ['PiS', 31496]], [['PiS', 128594], ['KO', 111085], ['PiS', 64297], ['KO', 55542], ['Lewica', 45579], ['PiS', 42865], ['KO', 37028], ['PiS', 32148], ['KO', 27771]], [['PiS', 161176], ['KO', 92506], ['PiS', 80588], ['PiS', 53725], ['KO', 46253], ['PiS', 40294], ['Lewica', 32315], ['PiS', 32235], ['KO', 30835]], [['PiS', 184049], ['KO', 174703], ['PiS', 92024], ['KO', 87352], ['PiS', 61350], ['KO', 58234], ['Lewica', 55980], ['PiS', 46012], ['KO', 43676], ['PiS', 36810], ['KO', 34941], ['Konfederacja', 34424]], [['PiS', 124546], ['KO', 99489], ['Lewica', 73459], ['PiS', 62273], ['KO', 49744], ['PiS', 41515], ['Lewica', 36730], ['KO', 33163], ['PiS', 31136]], [['PiS', 314466], ['PiS', 157233], ['PiS', 104822], ['KO', 94887], ['PiS', 78616], ['PiS', 62893], ['Lewica', 56704], ['PSL', 56305], ['PiS', 52411], ['KO', 47444], ['PiS', 44924], ['PiS', 39308], ['PiS', 34941], ['Konfederacja', 33909], ['KO', 31629], ['PiS', 31447]], [['PiS', 102485], ['KO', 71308], ['PiS', 51242], ['KO', 35654], ['PiS', 34162], ['Lewica', 29195], ['PSL', 27314], ['PiS', 25621]], [['PiS', 128760], ['KO', 87764], ['PiS', 64380], ['Lewica', 45905], ['KO', 43882], ['PSL', 43749], ['PiS', 42920], ['PiS', 32190], ['KO', 29255], ['PiS', 25752]], [['PiS', 195048], ['KO', 113502], ['PiS', 97524], ['PiS', 65016], ['Lewica', 61664], ['PSL', 58771], ['KO', 56751], ['PiS', 48762], ['PiS', 39010], ['KO', 37834], ['PiS', 32508], ['Lewica', 30832]], [['PiS', 166953], ['PiS', 83476], ['KO', 72303], ['PiS', 55651], ['Lewica', 53097], ['PiS', 41738], ['KO', 36152], ['PSL', 34633], ['PiS', 33391]], [['PiS', 124402], ['KO', 106810], ['PiS', 62201], ['KO', 53405], ['PSL', 48378], ['Lewica', 46354], ['PiS', 41467], ['KO', 35603], ['PiS', 31100]], [['KO', 233492], ['PiS', 130330], ['KO', 116746], ['Lewica', 84846], ['KO', 77831], ['PiS', 65165], ['KO', 58373], ['KO', 46698], ['PiS', 43443], ['Lewica', 42423]], [['PiS', 100071], ['KO', 87790], ['PiS', 50036], ['KO', 43895], ['Lewica', 41952], ['PiS', 33357], ['KO', 29263], ['PSL', 25622]], [['KO', 168026], ['PiS', 165203], ['KO', 84013], ['PiS', 82602], ['Lewica', 71756], ['KO', 56009], ['PiS', 55068], ['KO', 42006], ['PiS', 41301], ['Lewica', 35878], ['PSL', 34819], ['KO', 33605]]]

        # when
        election = SeatsCounter(parties=PARTIES_2019)
        election.count()
        # then
        assert len(expected_candidates_votes), len(election.districts)

        for i in range(0, len(expected_candidates_votes)):
            expected = expected_candidates_votes[i]
            given = election.districts[i]
            for expected_candidate_data in expected:
                expected_candidate = Candidate(
                    party_name=expected_candidate_data[0],
                    votes=expected_candidate_data[1],
                )
                self.assertIn(expected_candidate, given.candidates_votes)

    def test_district_mandates(self):
        # given
        # when
        election = SeatsCounter(parties=PARTIES_2019)
        election.count()
        # then

    def test_districts(self):
        """This test is awkward."""
        assert len(DISTRICTS), 41
