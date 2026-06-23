import pandas as pd

def load_lightcurve(filename):
    return pd.read_csv(filename)