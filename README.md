<p align="center">
<img src="https://raw.githubusercontent.com/bohdanbobrowski/pyrlament/master/assets/pyRLAMENT_icon.svg" width="300" alt="pyRLAMENT Library logo" />
</p>

[![Licence](https://img.shields.io/github/license/Ileriayo/markdown-badges?style=for-the-badge)](./LICENSE)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)


# pyRLAMENT

Python library for visualizing seats in the Sejm of the Republic of Poland. So far still in development. Its main goal is to practice the capabilities of Python on various platforms (web/mobile/desktop).

## Dev environment installation

    python -m venv .venv
    source .venv/venv/activate
    pip install -e .[dev]

## SeatsCounter:

    from pyrlament import SeatsCounter
    from pyrlament.data import Party

    polls_02_2026 = [
        Party(name="Razem", support=3.1, color="870f57"),
        Party(name="Lewica", support=8.0, color="d6001c"),
        Party(name="KO", support=32.5, threshold=8, color="f68f2e"),
        Party(name="Polska 2050", support=2.0, color="f9c408"),
        Party(name="PSL", support=4.8, color="3cb63a"),
        Party(name="Konfederacja", support=13.0, color="1a304f"),
        Party(name="PiS", support=22.7, threshold=8, color="5778a2"),
        Party(name="Konfederacja Korony Polskiej", support=9.9, color="a37a16"),
    ]
    election = SeatsCounter(parties=polls_02_2026, include_german_minority=False)
    election.count()

As a result of the operation of the `count` method, the `parties` parameter will contain information about the seats in the parliament, ex.:

    for party in election.parties:
        print(f"{party.name}: {party.seats}")

...should print:

    Razem: 0
    Lewica: 37
    KO: 196
    Polska 2050: 0
    PSL: 0
    Konfederacja: 62
    PiS: 119
    Konfederacja Korony Polskiej: 45

## SeatsGenerator:

    from pyrlament import SeatsGenerator 
    
    g = SeatsGenerator(parties=election.parties)
    g.randomize()
    with open('pyrlament.svg', 'w') as f:
        f.write(g.svg())

#### SVG example:

<img src="https://raw.githubusercontent.com/bohdanbobrowski/pyrlament/master/assets/pyrlament_sample.svg" width="100%" alt="pyRLAMENT example" />

#### PNG example:

<p align="center">
<img src="https://raw.githubusercontent.com/bohdanbobrowski/pyrlament/master/assets/pyrlament_sample.png" alt="pyRLAMENT example" />
</p>

## Tests coverage

    coverage report --format=markdown

| Name                      |    Stmts |     Miss |   Cover |
|-------------------------- | -------: | -------: | ------: |
| pyrlament/\_\_init\_\_.py |        4 |        0 |    100% |
| pyrlament/configs.py      |       12 |        0 |    100% |
| pyrlament/counter.py      |       96 |        1 |     99% |
| pyrlament/data.py         |       54 |        0 |    100% |
| pyrlament/generator.py    |      298 |       72 |     76% |
| **TOTAL**                 |  **464** |   **73** | **84%** |

## Implemented and planned features

Here are my plans (some already implemented) for this library:

- [x] count seats basing on election support
- [x] cover code with unit tests
- [x] 5% and 8% support threshold
- [x] validate support does not reach 100%
- [x] draw svg with seats
- [x] randomise seats colors
- [x] split seats between parties
- [x] svg/png output
- [x] [build webapp using Flask](https://www.pyrlament.pl)
- [ ] improve seats drwaing and placement (it's buggy)
- [ ] command line interface for library
- [ ] build mobile/desktop app using Kivy
