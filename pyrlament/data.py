from typing import Dict, List, Optional

from pydantic import BaseModel

DEPUTIES = 460


class Party(BaseModel):
    name: str
    support: float
    threshold: int = 5
    seats: Optional[int] = None


class PartySupport(BaseModel):
    name: str
    support: float
    year: Optional[int]


class PartySupportList(BaseModel):
    support: List[PartySupport]

    def add_support(
        self, party_name: str, party_support: float, year: Optional[int] = None
    ):
        pass
        # ps = PartySupport(name=party_name, support=party_support, year=year)
        # self.support.append(ps)

    def get_support(self, party_name: str) -> Optional[PartySupport]:
        result = None
        for party_support in self.support:
            if party_support.name == party_name:
                result = party_support
        return result

    def _generate_support(self, support: Dict, year: Optional[int] = None):
        for party_name in support:
            self.add_support(party_name, support[party_name], year)

    def __init__(self, *args, **kwargs):
        if len(args) == 2 and isinstance(args[0], int) and isinstance(args[1], dict):
            self._generate_support(support=args[1], year=args[0])
        if len(args) == 1 and isinstance(args[0], dict):
            self._generate_support(support=args[0])
        super().__init__(**kwargs)



class District(PartySupportList):
    mandates: int
    votes: int
    capital: str
    voivodeship: str


GENERAL_SUPPORT = PartySupportList(
    2019,
    {
        "PiS": 43.59,
        "KO": 27.4,
        "Lewica": 12.56,
        "PSL": 8.55,
        "Konfederacja": 6.81,
    },
)

GERMAN_MINORITY = Party(
    name="Mniejszość niemiecka",
    support=1,
    threshold=0,
    seats=1,
)

DISTRICTS = [
    District(
        mandates=12,
        votes=432436,
        capital="Legnica",
        voivodeship="dolnośląskie",
        support=sg(
            2019,
            {
                "PiS": 42.4,
                "KO": 25.02,
                "Lewica": 16.43,
                "PSL": 7.17,
                "Konfederacja": 5.85,
            },
        ),
    ),
    District(
        mandates=8,
        votes=283002,
        capital="Wałbrzych",
        voivodeship="dolnośląskie",
        support=sg(
            2019,
            {
                "PiS": 40.54,
                "KO": 32.09,
                "Lewica": 12.53,
                "PSL": 7.25,
                "Konfederacja": 5.42,
            },
        ),
    ),
    District(
        mandates=14,
        votes=654455,
        capital="Wrocław",
        voivodeship="dolnośląskie",
        support=sg(
            2019,
            {
                "PiS": 34.67,
                "KO": 32.8,
                "Lewica": 15.41,
                "PSL": 6.46,
                "Konfederacja": 7.45,
            },
        ),
    ),
    District(
        mandates=12,
        votes=459982,
        capital="Bydgoszcz",
        voivodeship="kujawsko-pomorskie",
        support=sg(
            2019,
            {
                "PiS": 36.43,
                "KO": 31.05,
                "Lewica": 15.17,
                "PSL": 9.02,
                "Konfederacja": 7.05,
            },
        ),
    ),
    District(
        mandates=13,
        votes=452330,
        capital="Toruń",
        voivodeship="kujawsko-pomorskie",
        support=sg(
            2019,
            {
                "PiS": 40.38,
                "KO": 26.42,
                "Lewica": 14.83,
                "PSL": 10.88,
                "Konfederacja": 6.33,
            },
        ),
    ),
    District(
        mandates=15,
        votes=565597,
        capital="Lublin",
        voivodeship="lubelskie",
        support=sg(
            2019,
            {
                "PiS": 55.39,
                "KO": 19.3,
                "Lewica": 9.1,
                "PSL": 7.81,
                "Konfederacja": 7.07,
            },
        ),
    ),
    District(
        mandates=12,
        votes=401318,
        capital="Chełm",
        voivodeship="lubelskie",
        support=sg(
            2019,
            {
                "PiS": 59.5,
                "KO": 14.8,
                "Lewica": 6.83,
                "PSL": 11.86,
                "Konfederacja": 5.84,
            },
        ),
    ),
    District(
        mandates=12,
        votes=437917,
        capital="Zielona Góra",
        voivodeship="lubuskie",
        support=sg(
            2019,
            {
                "PiS": 34.3,
                "KO": 31.27,
                "Lewica": 15.61,
                "PSL": 11.63,
                "Konfederacja": 7.19,
            },
        ),
    ),
    District(
        mandates=10,
        votes=415540,
        capital="Łódź",
        voivodeship="łódzkie",
        support=sg(
            2019,
            {
                "PiS": 32.9,
                "KO": 35.82,
                "Lewica": 20.1,
                "PSL": 4.53,
                "Konfederacja": 6.65,
            },
        ),
    ),
    District(
        mandates=9,
        votes=346326,
        capital="Piotrków Trybunalski",
        voivodeship="łódzkie",
        support=sg(2019, {}),
    ),
    District(
        mandates=12,
        votes=460239,
        capital="Sieradz",
        voivodeship="łódzkie",
        support=sg(
            2019,
            {
                "PiS": 56.21,
                "KO": 15.64,
                "Lewica": 10.95,
                "PSL": 10.44,
                "Konfederacja": 6.76,
            },
        ),
    ),
    District(
        mandates=8,
        votes=316214,
        capital="Kraków",
        voivodeship="małopolskie",
        support=sg(
            2019,
            {
                "PiS": 49.81,
                "KO": 20.48,
                "Lewica": 11.98,
                "PSL": 10.29,
                "Konfederacja": 5.88,
            },
        ),
    ),
    District(
        mandates=14,
        votes=649287,
        capital="Kraków",
        voivodeship="małopolskie",
        support=sg(
            2019,
            {
                "PiS": 39.56,
                "KO": 30.48,
                "Lewica": 13.01,
                "PSL": 7.27,
                "Konfederacja": 7.99,
            },
        ),
    ),
    District(
        mandates=10,
        votes=370199,
        capital="Nowy Sącz",
        voivodeship="małopolskie",
        support=sg(
            2019,
            {
                "PiS": 65.8,
                "KO": 13.83,
                "Lewica": 6.07,
                "PSL": 7.35,
                "Konfederacja": 6.95,
            },
        ),
    ),
    District(
        mandates=9,
        votes=347088,
        capital="Tarnów",
        voivodeship="małopolskie",
        support=sg(
            2019,
            {
                "PiS": 59.59,
                "KO": 14,
                "Lewica": 5.94,
                "PSL": 13.35,
                "Konfederacja": 7.11,
            },
        ),
    ),
    District(
        mandates=10,
        votes=370561,
        capital="Płock",
        voivodeship="mazowieckie",
        support=sg(
            2019,
            {
                "PiS": 52.45,
                "KO": 16.85,
                "Lewica": 8.76,
                "PSL": 15.17,
                "Konfederacja": 5.24,
            },
        ),
    ),
    District(
        mandates=9,
        votes=335009,
        capital="Radom",
        voivodeship="mazowieckie",
        support=sg(
            2019,
            {
                "PiS": 57.82,
                "KO": 17.15,
                "Lewica": 7.43,
                "PSL": 10.2,
                "Konfederacja": 5.89,
            },
        ),
    ),
    District(
        mandates=12,
        votes=452906,
        capital="Siedlce",
        voivodeship="mazowieckie",
        support=sg(
            2019,
            {
                "PiS": 59.76,
                "KO": 13.94,
                "Lewica": 6.45,
                "PSL": 11.94,
                "Konfederacja": 6.49,
            },
        ),
    ),
    District(
        mandates=20,
        votes=1381917,
        capital="Warszawa",
        voivodeship="mazowieckie",
        support=sg(
            2019,
            {
                "PiS": 27.49,
                "KO": 42.05,
                "Lewica": 18.19,
                "PSL": 4.75,
                "Konfederacja": 7.51,
            },
        ),
    ),
    District(
        mandates=12,
        votes=598727,
        capital="Warszawa",
        voivodeship="mazowieckie",
        support=sg(
            2019,
            {
                "PiS": 40.89,
                "KO": 28.61,
                "Lewica": 13.09,
                "PSL": 8.6,
                "Konfederacja": 6.63,
            },
        ),
    ),
    District(
        mandates=11,
        votes=406439,
        capital="Opole",
        voivodeship="opolskie",
        support=sg(
            2019,
            {
                "PiS": 37.64,
                "KO": 26.71,
                "Lewica": 11.74,
                "PSL": 10.31,
                "Konfederacja": 5.7,
            },
        ),
    ),
    District(
        mandates=11,
        votes=390581,
        capital="Krosno",
        voivodeship="podkarpackie",
        support=sg(
            2019,
            {
                "PiS": 63.36,
                "KO": 15.94,
                "Lewica": 6.04,
                "PSL": 7.85,
                "Konfederacja": 6.81,
            },
        ),
    ),
    District(
        mandates=15,
        votes=588786,
        capital="Rzeszów",
        voivodeship="podkarpackie",
        support=sg(
            2019,
            {
                "PiS": 62.38,
                "KO": 14.39,
                "Lewica": 6.59,
                "PSL": 7.79,
                "Konfederacja": 8.25,
            },
        ),
    ),
    District(
        mandates=14,
        votes=520578,
        capital="Białystok",
        voivodeship="podlaskie",
        support=sg(
            2019,
            {
                "PiS": 52.04,
                "KO": 21.04,
                "Lewica": 9.09,
                "PSL": 9.33,
                "Konfederacja": 6.96,
            },
        ),
    ),
    District(
        mandates=12,
        votes=528829,
        capital="Gdańsk",
        voivodeship="pomorskie",
        support=sg(
            2019,
            {
                "PiS": 32.1,
                "KO": 41.31,
                "Lewica": 13.47,
                "PSL": 5.9,
                "Konfederacja": 7.21,
            },
        ),
    ),
    District(
        mandates=14,
        votes=580722,
        capital="Słupsk",
        voivodeship="pomorskie",
        support=sg(
            2019,
            {
                "PiS": 36.43,
                "KO": 35.85,
                "Lewica": 12.47,
                "PSL": 7.94,
                "Konfederacja": 7.3,
            },
        ),
    ),
    District(
        mandates=9,
        votes=389256,
        capital="Bielsko-Biała",
        voivodeship="śląskie",
        support=sg(
            2019,
            {
                "PiS": 46.76,
                "KO": 27.2,
                "Lewica": 11.48,
                "PSL": 7.13,
                "Konfederacja": 7.48,
            },
        ),
    ),
    District(
        mandates=7,
        votes=284517,
        capital="Częstochowa",
        voivodeship="śląskie",
        support=sg(
            2019,
            {
                "PiS": 44.28,
                "KO": 22.63,
                "Lewica": 15.59,
                "PSL": 8.68,
                "Konfederacja": 6.07,
            },
        ),
    ),
    District(
        mandates=9,
        votes=340647,
        capital="Katowice",
        voivodeship="śląskie",
        support=sg(
            2019,
            {
                "PiS": 37.75,
                "KO": 32.61,
                "Lewica": 13.38,
                "PSL": 5.99,
                "Konfederacja": 7.67,
            },
        ),
    ),
    District(
        mandates=9,
        votes=333836,
        capital="Bielsko-Biała",
        voivodeship="śląskie",
        support=sg(
            2019,
            {
                "PiS": 48.28,
                "KO": 27.71,
                "Lewica": 9.68,
                "PSL": 5.64,
                "Konfederacja": 7.17,
            },
        ),
    ),
    District(
        mandates=12,
        votes=469633,
        capital="Katowice",
        voivodeship="śląskie",
        support=sg(
            2019,
            {
                "PiS": 39.19,
                "KO": 37.2,
                "Lewica": 11.92,
                "PSL": 4.37,
                "Konfederacja": 7.33,
            },
        ),
    ),
    District(
        mandates=9,
        votes=335431,
        capital="Katowice",
        voivodeship="śląskie",
        support=sg(
            2019,
            {
                "PiS": 37.13,
                "KO": 29.66,
                "Lewica": 21.9,
                "PSL": 4.85,
                "Konfederacja": 6.45,
            },
        ),
    ),
    District(
        mandates=16,
        votes=569891,
        capital="Kielce",
        voivodeship="świętokrzyskie",
        support=sg(
            2019,
            {
                "PiS": 55.18,
                "KO": 16.65,
                "Lewica": 9.95,
                "PSL": 9.88,
                "Konfederacja": 5.95,
            },
        ),
    ),
    District(
        mandates=8,
        votes=250819,
        capital="Elbląg",
        voivodeship="warmińsko-mazurskie",
        support=sg(
            2019,
            {
                "PiS": 40.86,
                "KO": 28.43,
                "Lewica": 11.64,
                "PSL": 10.89,
                "Konfederacja": 5.66,
            },
        ),
    ),
    District(
        mandates=10,
        votes=331684,
        capital="Olsztyn",
        voivodeship="warmińsko-mazurskie",
        support=sg(
            2019,
            {
                "PiS": 38.82,
                "KO": 26.46,
                "Lewica": 13.84,
                "PSL": 13.19,
                "Konfederacja": 6.97,
            },
        ),
    ),
    District(
        mandates=12,
        votes=459152,
        capital="Kalisz",
        voivodeship="wielkopolskie",
        support=sg(
            2019,
            {
                "PiS": 42.48,
                "KO": 24.72,
                "Lewica": 13.43,
                "PSL": 12.8,
                "Konfederacja": 6.57,
            },
        ),
    ),
    District(
        mandates=9,
        votes=353041,
        capital="Konin",
        voivodeship="wielkopolskie",
        support=sg(
            2019,
            {
                "PiS": 47.29,
                "KO": 20.48,
                "Lewica": 15.04,
                "PSL": 9.81,
                "Konfederacja": 6.74,
            },
        ),
    ),
    District(
        mandates=9,
        votes=349051,
        capital="Piła",
        voivodeship="wielkopolskie",
        support=sg(
            2019,
            {
                "PiS": 35.64,
                "KO": 30.6,
                "Lewica": 13.28,
                "PSL": 13.86,
                "Konfederacja": 6.62,
            },
        ),
    ),
    District(
        mandates=10,
        votes=514527,
        capital="Poznań",
        voivodeship="wielkopolskie",
        support=sg(
            2019,
            {
                "PiS": 25.33,
                "KO": 45.38,
                "Lewica": 16.49,
                "PSL": 6.2,
                "Konfederacja": 6.61,
            },
        ),
    ),
    District(
        mandates=8,
        votes=271711,
        capital="Koszalin",
        voivodeship="zachodniopomorskie",
        support=sg(
            2019,
            {
                "PiS": 36.83,
                "KO": 32.31,
                "Lewica": 15.44,
                "PSL": 9.43,
                "Konfederacja": 5.98,
            },
        ),
    ),
    District(
        mandates=12,
        votes=470529,
        capital="Szczecin",
        voivodeship="zachodniopomorskie",
        support=sg(
            2019,
            {
                "PiS": 35.11,
                "KO": 35.71,
                "Lewica": 15.25,
                "PSL": 7.4,
                "Konfederacja": 6.53,
            },
        ),
    ),
]
