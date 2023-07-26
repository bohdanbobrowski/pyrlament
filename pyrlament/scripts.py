from pyrlament import SeatsCounter, SeatsGenerator
from pyrlament.data import Party


def demo():
    election2019 = [
        Party(name="Lewica", support=7, color="8a281e"),
        Party(name="KO", support=32, threshold=8, color="c53f29"),
        Party(name="PSL", label="Polska 2050-PSL", support=5, threshold=5, color="dcb44b"),
        Party(name="Konfederacja", support=8, color="719ab7"),
        Party(name="PiS", support=33, threshold=8, color="5778a2"),
    ]
    election = SeatsCounter(parties=election2019)
    election.count()

    total = 0
    for party in election.parties:
        print(f"{party.name}: {party.seats}")
        total += party.seats
    print(f"RAZEM: {total}")

    g = SeatsGenerator(parties=election.parties, caption="Źródło: Kantar Public, 25.07.2023")
    g.colorize()
    g.save_svg("assets/pyrlament_sample.svg")
    g.save_png("assets/pyrlament_sample.png")
