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

    election2019 = {
        Party(name="PiS", support=43.59, threshold=8),
        Party(name="KO", support=27.4, threshold=8),
        Party(name="Lewica", support=12.56),
        Party(name="PSL", label="Polska 2050-PSL", support=10.8, threshold=8, color="DCB44B"),
        Party(name="Konfederacja", support=6.81),
    }
    election = SeatsCounter(parties=election2019)
    election.count()

As a result of the operation of the `count` method, the `parties` parameter will contain information about the seats in the parliament, ex.:

    for party in election.parties:
        print(f"{party.name}: {party.seats}")

...should print:

    PiS: 235,
    KO: 134,
    Lewica: 49,
    PSL: 30
    Konfederacja: 11
    Mniejszość niemiecka: 1

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
| pyrlament/counter.py      |       98 |        1 |     99% |
| pyrlament/data.py         |       67 |        0 |    100% |
| pyrlament/generator.py    |      306 |      104 |     66% |
|                 **TOTAL** |  **487** |  **105** | **78%** |


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
