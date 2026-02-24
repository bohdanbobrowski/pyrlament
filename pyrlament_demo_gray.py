from pyrlament import SeatsGenerator

def demo():
    g = SeatsGenerator(parties=[], legend=False)
    g.gray()
    g.save_svg("assets/pyrlament_sample_gray.svg")
    g.save_png("assets/pyrlament_sample_gray.png")

if __name__ == "__main__":
    demo()
