from pyrlament import SeatsCounter, SeatsGenerator
from pyrlament.data import Party

PARTIES = [
    Party(name="Razem", support=3.1, color="870f57"),
    Party(name="Lewica", support=8.0, color="d6001c"),
    Party(name="KO", support=32.5, threshold=8, color="f68f2e"),
    Party(name="Polska 2050", support=2.0, color="f9c408"),
    Party(name="PSL", support=4.8, color="3cb63a"),
    Party(name="Konfederacja", support=13.0, color="1a304f"),
    Party(name="PiS", support=22.7, threshold=8, color="5778a2"),
    Party(name="Konfederacja Korony Polskiej", support=9.9, color="a37a16"),
]
CAPTION = "Źródło: United Surveys by IBRIS dla Wirtualnej Polski (13-15/02/2026)"


def demo():
    election = SeatsCounter(parties=PARTIES)
    election.count()
    g = SeatsGenerator(parties=election.parties, caption=CAPTION)
    g.colorize()
    g.save_svg("assets/pyrlament_sample.svg")
    g.save_png("assets/pyrlament_sample.png")

    g2 = SeatsGenerator(parties=[], legend=False)
    g2.gray()
    g2.save_svg("assets/pyrlament_sample_gray.svg")
    g2.save_png("assets/pyrlament_sample_gray.png")

if __name__ == "__main__":
    demo()
