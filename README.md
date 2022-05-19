<img src="https://raw.githubusercontent.com/bohdanbobrowski/pyrlament/master/assets/pyRLAMENT_logo_RAW.svg?token=GHSAT0AAAAAABUXNW53T4ZD6JW36CHRLSPGYUGB33Q" width="400" alt="pyRLAMENT" />

# pyRLAMENT

_Python library visualizing the distribution of seats in the Polish Sejm_

## Running dev environment

```bash
git clone git@github.com:bohdanbobrowski/pyrlament.git
cd pyrlament
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp env_example .env
source .env
flask run
```