import sys
sys.path.append(".")

from astrotime.loader import load_lightcurve
from astrotime.plotting import plot_lightcurve
lc = load_lightcurve("data/lightcurve_dataset.csv")
plot_lightcurve(lc)