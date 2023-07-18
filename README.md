<p align="center">
<img src="https://raw.githubusercontent.com/bohdanbobrowski/pyrlament/master/assets/pyRLAMENT_icon.svg" width="300" alt="pyRLAMENT Library logo" />
</p>

[![Licence](https://img.shields.io/github/license/Ileriayo/markdown-badges?style=for-the-badge)](./LICENSE)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)


# pyRLAMENT

Python library for visualizing seats in the Sejm of the Republic of Poland. So far, a very early version, and its main goal is to practice the capabilities of the python language on various platforms (web/mobile/desktop).

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

Known bug: for some reason png output is missing logotype. 

<p align="center">
<img src="https://raw.githubusercontent.com/bohdanbobrowski/pyrlament/master/assets/pyrlament_sample.png" alt="pyRLAMENT example" />
</p>

## Implemented and planned features

Here are my plans (some already implemented) for this library:

- [x] count seats basing on election support
- [x] cover code with unit tests
- [ ] 5% and 8% support threshold
- [ ] check if all support does not reach 100%
- [x] draw svg with seats
- [x] randomise seats colors
- [x] split seats between parties
- [ ] improve seats placement (it's a bit messy)
- [x] svg output
- [ ] fix png output
- [x] [build webapp using Flask](https://www.pyrlament.pl)
- [ ] build mobile app using Kivy
- [ ] build desktop app using Kivy
- [ ] cli interface for library