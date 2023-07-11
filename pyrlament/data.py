from typing import Dict, List, Optional

from pydantic import BaseModel

DEPUTIES = 460


class Party(BaseModel):
    name: str
    votes: float
    threshold: int = 5
    seats: Optional[int] = None


class ArchivalSupport(BaseModel):
    name: str
    support: float
    year: int


def sg(year: int, support: Dict) -> List[ArchivalSupport]:
    """Support generator."""
    output = []
    for party_name in support:
        output.append(
            ArchivalSupport(name=party_name, support=support[party_name], year=year)
        )
    return output


class District(BaseModel):
    mandates: int
    votes: int
    capital: str
    voivodeship: str
    archive: List[ArchivalSupport]


GERMAN_MINORITY = Party(
    name="Mniejszość niemiecka",
    votes=1,
    threshold=0,
    seats=1,
)

DISTRICTS = [
    District(
        mandates=12,
        votes=432436,
        capital="Legnica",
        voivodeship="dolnośląskie",
        archive=[],
    ),
    District(
        mandates=8,
        votes=283002,
        capital="Wałbrzych",
        voivodeship="dolnośląskie",
        archive=[],
    ),
    District(
        mandates=14,
        votes=654455,
        capital="Wrocław",
        voivodeship="dolnośląskie",
        archive=[],
    ),
    District(
        mandates=12,
        votes=459982,
        capital="Bydgoszcz",
        voivodeship="kujawsko-pomorskie",
        archive=[],
    ),
    District(
        mandates=13,
        votes=452330,
        capital="Toruń",
        voivodeship="kujawsko-pomorskie",
        archive=[],
    ),
    District(
        mandates=15,
        votes=565597,
        capital="Lublin",
        voivodeship="lubelskie",
        archive=[],
    ),
    District(
        mandates=12,
        votes=401318,
        capital="Chełm",
        voivodeship="lubelskie",
        archive=[],
    ),
    District(
        mandates=12,
        votes=437917,
        capital="Zielona Góra",
        voivodeship="lubuskie",
        archive=[],
    ),
    District(
        mandates=10,
        votes=415540,
        capital="Łódź",
        voivodeship="łódzkie",
        archive=[],
    ),
    District(
        mandates=9,
        votes=346326,
        capital="Piotrków Trybunalski",
        voivodeship="łódzkie",
        archive=[],
    ),
    District(
        mandates=12,
        votes=460239,
        capital="Sieradz",
        voivodeship="łódzkie",
        archive=[],
    ),
    District(
        mandates=8,
        votes=316214,
        capital="Kraków",
        voivodeship="małopolskie",
        archive=[],
    ),
    District(
        mandates=14,
        votes=649287,
        capital="Kraków",
        voivodeship="małopolskie",
        archive=[],
    ),
    District(
        mandates=10,
        votes=370199,
        capital="Nowy Sącz",
        voivodeship="małopolskie",
        archive=[],
    ),
    District(
        mandates=9,
        votes=347088,
        capital="Tarnów",
        voivodeship="małopolskie",
        archive=[],
    ),
    District(
        mandates=10,
        votes=370561,
        capital="Płock",
        voivodeship="mazowieckie",
        archive=[],
    ),
    District(
        mandates=9,
        votes=335009,
        capital="Radom",
        voivodeship="mazowieckie",
        archive=[],
    ),
    District(
        mandates=12,
        votes=452906,
        capital="Siedlce",
        voivodeship="mazowieckie",
        archive=[],
    ),
    District(
        mandates=20,
        votes=1381917,
        capital="Warszawa",
        voivodeship="mazowieckie",
        archive=[],
    ),
    District(
        mandates=12,
        votes=598727,
        capital="Warszawa",
        voivodeship="mazowieckie",
        archive=[],
    ),
    District(
        mandates=11,
        votes=406439,
        capital="Opole",
        voivodeship="opolskie",
        archive=[],
    ),
    District(
        mandates=11,
        votes=390581,
        capital="Krosno",
        voivodeship="podkarpackie",
        archive=[],
    ),
    District(
        mandates=15,
        votes=588786,
        capital="Rzeszów",
        voivodeship="podkarpackie",
        archive=[],
    ),
    District(
        mandates=14,
        votes=520578,
        capital="Białystok",
        voivodeship="podlaskie",
        archive=[],
    ),
    District(
        mandates=12,
        votes=528829,
        capital="Gdańsk",
        voivodeship="pomorskie",
        archive=[],
    ),
    District(
        mandates=14,
        votes=580722,
        capital="Słupsk",
        voivodeship="pomorskie",
        archive=[],
    ),
    District(
        mandates=9,
        votes=389256,
        capital="Bielsko-Biała",
        voivodeship="śląskie",
        archive=[],
    ),
    District(
        mandates=7,
        votes=284517,
        capital="Częstochowa",
        voivodeship="śląskie",
        archive=[],
    ),
    District(
        mandates=9,
        votes=340647,
        capital="Katowice",
        voivodeship="śląskie",
        archive=[],
    ),
    District(
        mandates=9,
        votes=333836,
        capital="Bielsko-Biała",
        voivodeship="śląskie",
        archive=[],
    ),
    District(
        mandates=12,
        votes=469633,
        capital="Katowice",
        voivodeship="śląskie",
        archive=[],
    ),
    District(
        mandates=9,
        votes=335431,
        capital="Katowice",
        voivodeship="śląskie",
        archive=[],
    ),
    District(
        mandates=16,
        votes=569891,
        capital="Kielce",
        voivodeship="świętokrzyskie",
        archive=[],
    ),
    District(
        mandates=8,
        votes=250819,
        capital="Elbląg",
        voivodeship="warmińsko-mazurskie",
        archive=[],
    ),
    District(
        mandates=10,
        votes=331684,
        capital="Olsztyn",
        voivodeship="warmińsko-mazurskie",
        archive=[],
    ),
    District(
        mandates=12,
        votes=459152,
        capital="Kalisz",
        voivodeship="wielkopolskie",
        archive=[],
    ),
    District(
        mandates=9,
        votes=353041,
        capital="Konin",
        voivodeship="wielkopolskie",
        archive=[],
    ),
    District(
        mandates=9,
        votes=349051,
        capital="Piła",
        voivodeship="wielkopolskie",
        archive=[],
    ),
    District(
        mandates=10,
        votes=514527,
        capital="Poznań",
        voivodeship="wielkopolskie",
        archive=[],
    ),
    District(
        mandates=8,
        votes=271711,
        capital="Koszalin",
        voivodeship="zachodniopomorskie",
        archive=[],
    ),
    District(
        mandates=12,
        votes=470529,
        capital="Szczecin",
        voivodeship="zachodniopomorskie",
        archive=[],
    ),
]
