# atomic-wsra-waves

Notebooks to perform [Wide Swath Radar Altimeter (WSRA)](https://psl.noaa.gov/technology/wide-swath-radar-altimeter/) wave validation during the [Atlantic Tradewind Ocean–Atmosphere Mesoscale Interaction Campaign (ATOMIC)](https://psl.noaa.gov/atomic/).  These notebooks use the Python package [PyWSRA](https://github.com/jacobrdavis/PyWSRA) (which is under active development!).

To follow along with the analysis, the notebooks should be run in the following order:

1. `io.ipynb`
2. `calculate.ipynb`
3. `compare.ipynb`

The notebooks can be run in any order, since notebooks which depend on other notebooks (i.e., `compare.ipynb`) call the neccessary dependencies in order.  The module `sharedfunctions.py` is called by the notebooks as needed and does not need to be run manually.
