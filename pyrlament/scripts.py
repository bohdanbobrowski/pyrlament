from pyrlament import SeatsCounter, SeatsGenerator
from pyrlament.data import Party


def demo():
    election2019 = [
        Party(name="Lewica", support=5, color="8a281e"),
        Party(name="KO", support=28, threshold=8, color="c53f29"),
        Party(name="PSL", label="Polska 2050-PSL", support=6, threshold=8, color="dcb44b"),
        Party(name="Konfederacja", support=9, color="719ab7"),
        Party(name="PiS", support=29, threshold=8, color="5778a2"),
    ]
    election = SeatsCounter(parties=election2019)
    election.count()

    for party in election.parties:
        print(f"{party.name}: {party.seats}")

    g = SeatsGenerator(parties=election.parties, caption="Źródło: CBOS, Lipiec 2023")
    g.colorize()
    g.save_svg("assets/pyrlament_sample.svg")
    g.save_png("assets/pyrlament_sample.png")
