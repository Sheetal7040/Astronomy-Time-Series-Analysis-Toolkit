# Plotting the light curve
# Light curve containing time and flux

import matplotlib.pyplot as plt


def plot_lightcurve(data):
    plt.figure(figsize=(10, 5))
    plt.plot(data["time"], data["flux"], ".", markersize=1)
    plt.xlabel("Time(BTJD days)")
    plt.ylabel("Flux (electrons/s)")
    plt.title("Light Curve")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
