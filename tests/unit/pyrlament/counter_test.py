from pyrlament.counter import SeatsCounter
from pyrlament.data import DEPUTIES, DISTRICTS, Party


class TestSeatsCounter:
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
            Party(name="PiS", support=43.59),
            Party(name="KO", support=27.4),
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
        district_support = [
            {
                "Liczba mandatow": 12,
                "Glosy wazne": 432436,
                "Siedziba": "Legnica",
                "Wojewodztwo": "dolnośląskie",
                "PiS": "42.40",
                "KO": "25.02",
                "Lewica": "16.43",
                "PSL": "7.17",
                "Konfederacja": "5.85",
                "PL2050": 0
            },
            {
                "Liczba mandatow": 8,
                "Glosy wazne": 283002,
                "Siedziba": "Wałbrzych",
                "Wojewodztwo": "dolnośląskie",
                "PiS": "40.54",
                "KO": "32.09",
                "Lewica": "12.53",
                "PSL": "7.25",
                "Konfederacja": "5.42",
                "PL2050": 0
            },
            {
                "Liczba mandatow": 14,
                "Glosy wazne": 654455,
                "Siedziba": "Wrocław",
                "Wojewodztwo": "dolnośląskie",
                "PiS": "34.67",
                "KO": "32.80",
                "Lewica": "15.41",
                "PSL": "6.46",
                "Konfederacja": "7.45",
                "PL2050": 0
            },
            {
                "Liczba mandatow": 12,
                "Glosy wazne": 459982,
                "Siedziba": "Bydgoszcz",
                "Wojewodztwo": "kujawsko-pomorskie",
                "PiS": "36.43",
                "KO": "31.05",
                "Lewica": "15.17",
                "PSL": "9.02",
                "Konfederacja": "7.05",
                "PL2050": 0
            },
            {
                "Liczba mandatow": 13,
                "Glosy wazne": 452330,
                "Siedziba": "Toruń",
                "Wojewodztwo": "kujawsko-pomorskie",
                "PiS": "40.38",
                "KO": "26.42",
                "Lewica": "14.83",
                "PSL": "10.88",
                "Konfederacja": "6.33",
                "PL2050": 0
            },
            {
                "Liczba mandatow": 15,
                "Glosy wazne": 565597,
                "Siedziba": "Lublin",
                "Wojewodztwo": "lubelskie",
                "PiS": "55.39",
                "KO": "19.30",
                "Lewica": "9.10",
                "PSL": "7.81",
                "Konfederacja": "7.07",
                "PL2050": 0
            },
            {
                "Liczba mandatow": 12,
                "Glosy wazne": 401318,
                "Siedziba": "Chełm",
                "Wojewodztwo": "lubelskie",
                "PiS": "59.50",
                "KO": "14.80",
                "Lewica": "6.83",
                "PSL": "11.86",
                "Konfederacja": "5.84",
                "PL2050": 0
            },
            {
                "Liczba mandatow": 12,
                "Glosy wazne": 437917,
                "Siedziba": "Zielona Góra",
                "Wojewodztwo": "lubuskie",
                "PiS": "34.30",
                "KO": "31.27",
                "Lewica": "15.61",
                "PSL": "11.63",
                "Konfederacja": "7.19",
                "PL2050": 0
            },
            {
                "Liczba mandatow": 10,
                "Glosy wazne": 415540,
                "Siedziba": "Łódź",
                "Wojewodztwo": "łódzkie",
                "PiS": "32.90",
                "KO": "35.82",
                "Lewica": "20.10",
                "PSL": "4.53",
                "Konfederacja": "6.65",
                "PL2050": 0
            },
            {
                "Liczba mandatow": 9,
                "Glosy wazne": 346326,
                "Siedziba": "Piotrków Trybunalski",
                "Wojewodztwo": "łódzkie",
                "PiS": "56.21",
                "KO": "15.64",
                "Lewica": "10.95",
                "PSL": "10.44",
                "Konfederacja": "6.76",
                "PL2050": 0
            },
            {
                "Liczba mandatow": 12,
                "Glosy wazne": 460239,
                "Siedziba": "Sieradz",
                "Wojewodztwo": "łódzkie",
                "PiS": "49.81",
                "KO": "20.48",
                "Lewica": "11.98",
                "PSL": "10.29",
                "Konfederacja": "5.88",
                "PL2050": 0
            },
            {
                "Liczba mandatow": 8,
                "Glosy wazne": 316214,
                "Siedziba": "Kraków",
                "Wojewodztwo": "małopolskie",
                "PiS": "53.48",
                "KO": "23.04",
                "Lewica": "8.51",
                "PSL": "7.90",
                "Konfederacja": "7.06",
                "PL2050": 0
            },
            {
                "Liczba mandatow": 14,
                "Glosy wazne": 649287,
                "Siedziba": "Kraków",
                "Wojewodztwo": "małopolskie",
                "PiS": "39.56",
                "KO": "30.48",
                "Lewica": "13.01",
                "PSL": "7.27",
                "Konfederacja": "7.99",
                "PL2050": 0
            },
            {
                "Liczba mandatow": 10,
                "Glosy wazne": 370199,
                "Siedziba": "Nowy Sącz",
                "Wojewodztwo": "małopolskie",
                "PiS": "65.80",
                "KO": "13.83",
                "Lewica": "6.07",
                "PSL": "7.35",
                "Konfederacja": "6.95",
                "PL2050": 0
            },
            {
                "Liczba mandatow": 9,
                "Glosy wazne": 347088,
                "Siedziba": "Tarnów",
                "Wojewodztwo": "małopolskie",
                "PiS": "59.59",
                "KO": "14.00",
                "Lewica": "5.94",
                "PSL": "13.35",
                "Konfederacja": "7.11",
                "PL2050": 0
            },
            {
                "Liczba mandatow": 10,
                "Glosy wazne": 370561,
                "Siedziba": "Płock",
                "Wojewodztwo": "mazowieckie",
                "PiS": "52.45",
                "KO": "16.85",
                "Lewica": "8.76",
                "PSL": "15.17",
                "Konfederacja": "5.24",
                "PL2050": 0
            },
            {
                "Liczba mandatow": 9,
                "Glosy wazne": 335009,
                "Siedziba": "Radom",
                "Wojewodztwo": "mazowieckie",
                "PiS": "57.82",
                "KO": "17.15",
                "Lewica": "7.43",
                "PSL": "10.20",
                "Konfederacja": "5.89",
                "PL2050": 0
            },
            {
                "Liczba mandatow": 12,
                "Glosy wazne": 452906,
                "Siedziba": "Siedlce",
                "Wojewodztwo": "mazowieckie",
                "PiS": "59.76",
                "KO": "13.94",
                "Lewica": "6.45",
                "PSL": "11.94",
                "Konfederacja": "6.49",
                "PL2050": 0
            },
            {
                "Liczba mandatow": 20,
                "Glosy wazne": 1381917,
                "Siedziba": "Warszawa",
                "Wojewodztwo": "mazowieckie",
                "PiS": "27.49",
                "KO": "42.05",
                "Lewica": "18.19",
                "PSL": "4.75",
                "Konfederacja": "7.51",
                "PL2050": 0
            },
            {
                "Liczba mandatow": 12,
                "Glosy wazne": 598727,
                "Siedziba": "Warszawa",
                "Wojewodztwo": "mazowieckie",
                "PiS": "40.89",
                "KO": "28.61",
                "Lewica": "13.09",
                "PSL": "8.60",
                "Konfederacja": "6.63",
                "PL2050": 0
            },
            {
                "Liczba mandatow": 11,
                "Glosy wazne": 406439,
                "Siedziba": "Opole",
                "Wojewodztwo": "opolskie",
                "PiS": "37.64",
                "KO": "26.71",
                "Lewica": "11.74",
                "PSL": "10.31",
                "Konfederacja": "5.70",
                "PL2050": 0
            },
            {
                "Liczba mandatow": 11,
                "Glosy wazne": 390581,
                "Siedziba": "Krosno",
                "Wojewodztwo": "podkarpackie",
                "PiS": "63.36",
                "KO": "15.94",
                "Lewica": "6.04",
                "PSL": "7.85",
                "Konfederacja": "6.81",
                "PL2050": 0
            },
            {
                "Liczba mandatow": 15,
                "Glosy wazne": 588786,
                "Siedziba": "Rzeszów",
                "Wojewodztwo": "podkarpackie",
                "PiS": "62.38",
                "KO": "14.39",
                "Lewica": "6.59",
                "PSL": "7.79",
                "Konfederacja": "8.25",
                "PL2050": 0
            },
            {
                "Liczba mandatow": 14,
                "Glosy wazne": 520578,
                "Siedziba": "Białystok",
                "Wojewodztwo": "podlaskie",
                "PiS": "52.04",
                "KO": "21.04",
                "Lewica": "9.09",
                "PSL": "9.33",
                "Konfederacja": "6.96",
                "PL2050": 0
            },
            {
                "Liczba mandatow": 12,
                "Glosy wazne": 528829,
                "Siedziba": "Gdańsk",
                "Wojewodztwo": "pomorskie",
                "PiS": "32.10",
                "KO": "41.31",
                "Lewica": "13.47",
                "PSL": "5.90",
                "Konfederacja": "7.21",
                "PL2050": 0
            },
            {
                "Liczba mandatow": 14,
                "Glosy wazne": 580722,
                "Siedziba": "Słupsk",
                "Wojewodztwo": "pomorskie",
                "PiS": "36.43",
                "KO": "35.85",
                "Lewica": "12.47",
                "PSL": "7.94",
                "Konfederacja": "7.30",
                "PL2050": 0
            },
            {
                "Liczba mandatow": 9,
                "Glosy wazne": 389256,
                "Siedziba": "Bielsko-Biała",
                "Wojewodztwo": "śląskie",
                "PiS": "46.76",
                "KO": "27.20",
                "Lewica": "11.48",
                "PSL": "7.13",
                "Konfederacja": "7.48",
                "PL2050": 0
            },
            {
                "Liczba mandatow": 7,
                "Glosy wazne": 284517,
                "Siedziba": "Częstochowa",
                "Wojewodztwo": "śląskie",
                "PiS": "44.28",
                "KO": "22.63",
                "Lewica": "15.59",
                "PSL": "8.68",
                "Konfederacja": "6.07",
                "PL2050": 0
            },
            {
                "Liczba mandatow": 9,
                "Glosy wazne": 340647,
                "Siedziba": "Katowice",
                "Wojewodztwo": "śląskie",
                "PiS": "37.75",
                "KO": "32.61",
                "Lewica": "13.38",
                "PSL": "5.99",
                "Konfederacja": "7.67",
                "PL2050": 0
            },
            {
                "Liczba mandatow": 9,
                "Glosy wazne": 333836,
                "Siedziba": "Bielsko-Biała",
                "Wojewodztwo": "śląskie",
                "PiS": "48.28",
                "KO": "27.71",
                "Lewica": "9.68",
                "PSL": "5.64",
                "Konfederacja": "7.17",
                "PL2050": 0
            },
            {
                "Liczba mandatow": 12,
                "Glosy wazne": 469633,
                "Siedziba": "Katowice",
                "Wojewodztwo": "śląskie",
                "PiS": "39.19",
                "KO": "37.20",
                "Lewica": "11.92",
                "PSL": "4.37",
                "Konfederacja": "7.33",
                "PL2050": 0
            },
            {
                "Liczba mandatow": 9,
                "Glosy wazne": 335431,
                "Siedziba": "Katowice",
                "Wojewodztwo": "śląskie",
                "PiS": "37.13",
                "KO": "29.66",
                "Lewica": "21.90",
                "PSL": "4.85",
                "Konfederacja": "6.45",
                "PL2050": 0
            },
            {
                "Liczba mandatow": 16,
                "Glosy wazne": 569891,
                "Siedziba": "Kielce",
                "Wojewodztwo": "świętokrzyskie",
                "PiS": "55.18",
                "KO": "16.65",
                "Lewica": "9.95",
                "PSL": "9.88",
                "Konfederacja": "5.95",
                "PL2050": 0
            },
            {
                "Liczba mandatow": 8,
                "Glosy wazne": 250819,
                "Siedziba": "Elbląg",
                "Wojewodztwo": "warmińsko-mazurskie",
                "PiS": "40.86",
                "KO": "28.43",
                "Lewica": "11.64",
                "PSL": "10.89",
                "Konfederacja": "5.66",
                "PL2050": 0
            },
            {
                "Liczba mandatow": 10,
                "Glosy wazne": 331684,
                "Siedziba": "Olsztyn",
                "Wojewodztwo": "warmińsko-mazurskie",
                "PiS": "38.82",
                "KO": "26.46",
                "Lewica": "13.84",
                "PSL": "13.19",
                "Konfederacja": "6.97",
                "PL2050": 0
            },
            {
                "Liczba mandatow": 12,
                "Glosy wazne": 459152,
                "Siedziba": "Kalisz",
                "Wojewodztwo": "wielkopolskie",
                "PiS": "42.48",
                "KO": "24.72",
                "Lewica": "13.43",
                "PSL": "12.80",
                "Konfederacja": "6.57",
                "PL2050": 0
            },
            {
                "Liczba mandatow": 9,
                "Glosy wazne": 353041,
                "Siedziba": "Konin",
                "Wojewodztwo": "wielkopolskie",
                "PiS": "47.29",
                "KO": "20.48",
                "Lewica": "15.04",
                "PSL": "9.81",
                "Konfederacja": "6.74",
                "PL2050": 0
            },
            {
                "Liczba mandatow": 9,
                "Glosy wazne": 349051,
                "Siedziba": "Piła",
                "Wojewodztwo": "wielkopolskie",
                "PiS": "35.64",
                "KO": "30.60",
                "Lewica": "13.28",
                "PSL": "13.86",
                "Konfederacja": "6.62",
                "PL2050": 0
            },
            {
                "Liczba mandatow": 10,
                "Glosy wazne": 514527,
                "Siedziba": "Poznań",
                "Wojewodztwo": "wielkopolskie",
                "PiS": "25.33",
                "KO": "45.38",
                "Lewica": "16.49",
                "PSL": "6.20",
                "Konfederacja": "6.61",
                "PL2050": 0
            },
            {
                "Liczba mandatow": 8,
                "Glosy wazne": 271711,
                "Siedziba": "Koszalin",
                "Wojewodztwo": "zachodniopomorskie",
                "PiS": "36.83",
                "KO": "32.31",
                "Lewica": "15.44",
                "PSL": "9.43",
                "Konfederacja": "5.98",
                "PL2050": 0
            },
            {
                "Liczba mandatow": 12,
                "Glosy wazne": 470529,
                "Siedziba": "Szczecin",
                "Wojewodztwo": "zachodniopomorskie",
                "PiS": "35.11",
                "KO": "35.71",
                "Lewica": "15.25",
                "PSL": "7.40",
                "Konfederacja": "6.53",
                "PL2050": 0
            }
        ]
        # when
        election = SeatsCounter(parties=parties)
        election.count()
        # then
        for i in range(0, len(district_support)):
            expected = district_support[i]
            given = election.districts_updated[i]
            for given_p in given.support:
                assert given_p.support, expected[given_p.name]


    def test_districts(self):
        """This test is awkward."""
        assert len(DISTRICTS), 41
