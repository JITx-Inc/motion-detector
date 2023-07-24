
# Z3 Solver

Solve parameters for bandpass inverting op amp

## Setup

1.  Install `virtualenv` if you don't have it
2.  python -m venv venv
3.  source venv/bin/activate
4.  pip install -r requirements.txt

## Run:

```
(venv) $> python single_supply.py
sat
[Cf = 1/6405600000,
 Rg = 19380/13,
 Cin = 13/12170640,
 R1 = 51000,
 R2 = 51000,
 Rf = 51000,
 /0 = [(1, 1/100) -> 100,
       (1, 1/20000) -> 20000,
       (51000, 102000) -> 1/2,
       (-51000, 19380/13) -> -650/19,
       else -> 0]]
```


# Simulation Files

Using the parameters above, I created simulations in [TINA](https://www.tina.com/)

1.  I've included the simulation files for both the MCP6001 variant and the TS971 variant.
2.  I've included outputs of the BODE plot and the transient response as images.
