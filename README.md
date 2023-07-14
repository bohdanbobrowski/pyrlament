<p align="center">
<img src="https://raw.githubusercontent.com/bohdanbobrowski/pyrlament/master/assets/pyRLAMENT_logo.svg" width="400" alt="pyRLAMENT Library logo" />
</p>

# pyRLAMENT

Python library for visualizing seats in the Sejm of the Republic of Poland. So far, a very early version, and its main goal is to practice the capabilities of the python language on various platforms (web/mobile/desktop).

## SeatsCounter:

    from pyrlament import SeatsCounter
    from pyrlament.data import Party

    election2019 = {
        Party(name="PiS", support=43.59, threshold=8),
        Party(name="KO", support=27.4, threshold=8),
        Party(name="Lewica", support=12.56),
        Party(name="PSL", support=8.55),
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
    
    g = SeatsGenerator()
    g.randomize()
    with open('pyrlament.svg', 'w') as f:
        f.write(g.svg())

<img src="https://raw.githubusercontent.com/bohdanbobrowski/pyrlament/master/assets/pyrlament_sample.svg" width="100%" alt="pyRLAMENT example" />

 


