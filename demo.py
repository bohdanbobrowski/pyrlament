from pyrlament import SeatsCounter, SeatsGenerator
from pyrlament.data import Party

election2019 = [
    Party(name="PiS", support=43.59, threshold=8, color="FF69B4"),
    Party(name="KO", support=27.4, threshold=8, color="008000"),
    Party(name="Lewica", support=12.56, color="4B0082"),
    Party(name="PSL", support=8.55, color="9400D3"),
    Party(name="Konfederacja", support=6.81, color="FE2020"),
]
election = SeatsCounter(parties=election2019)
election.count()

for party in election.parties:
    print(f"{party.name}: {party.seats}")

g = SeatsGenerator(parties=election.parties)
g.colorize()
g.save_svg("assets/pyrlament_sample.svg")
g.save_png("assets/pyrlament_sample.png")
