<img src="https://raw.githubusercontent.com/bohdanbobrowski/pyrlament/master/static/img/pyRLAMENT_logo.svg" width="400" alt="pyRLAMENT" />

# pyRLAMENT

_Python library visualizing the distribution of seats in the Polish Sejm_

## Running dev environment

```bash
git clone git@github.com:bohdanbobrowski/pyrlament.git
cd pyrlament
poetry install --with dev
poetry shell
cp env_example .env
source .env
flask run
```