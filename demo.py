"""
This file is usable for debugging.
"""

from pyrlament import SeatsCounter, SeatsGenerator
from pyrlament.data import Party

election2019 = [
    Party(name="Lewica", support=9.4, color="8A281E"),
    Party(name="KO", support=27.4, threshold=8, color="C53F29"),
    Party(name="PSL", label="Polska 2050-PSL", support=10.8, threshold=8, color="DCB44B"),
    Party(name="Konfederacja", support=15.7, color="719AB7"),
    Party(name="PiS", support=35.1, threshold=8, color="5778A2"),
]
election = SeatsCounter(parties=election2019)
election.count()

for party in election.parties:
    print(f"{party.name}: {party.seats}")

g = SeatsGenerator(parties=election.parties)
g.colorize()
# g.colorize_by_sequence()
g.save_svg("assets/pyrlament_sample.svg")
g.convert_svg_to_png("assets/pyrlament_sample.svg", "assets/pyrlament_sample.png")
