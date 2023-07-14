<img src="https://raw.githubusercontent.com/bohdanbobrowski/pyrlament/master/assets/pyRLAMENT_logo.svg" width="400" alt="pyRLAMENT Library logo" />

# pyRLAMENT

Python library for visualizing seats in the Sejm of the Republic of Poland. So far, a very early version, and its main goal is to practice the capabilities of the python language on various platforms (web/mobile/desktop).

## SeatsCounter:

## SeatsGenerator:

    from pyrlament.generator import SeatsGenerator
    
    g = SeatsGenerator()
    g.randomize()
    with open('pyrlament.svg', 'w') as f:
        f.write(g.svg())

<img src="https://raw.githubusercontent.com/bohdanbobrowski/pyrlament/master/assets/pyrlament_sample.svg" width="100%" alt="pyRLAMENT example" />

 


