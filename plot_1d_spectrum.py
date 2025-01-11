import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import xarray as xr
import matplotlib
from scipy.signal import detrend
from spectrum import power_spectrum


matplotlib.rcParams['font.size'] = 16

ds = xr.open_dataset("data/CLASI_ASIS_L3_phase4_Romeo_2023020318.nc")

n0 = 130000
n1 = 136000

eta = detrend(ds.elevation[0,n0:n1])


fig = plt.figure(figsize=(16, 6))
ax = fig.add_subplot(111)
ax.plot(ds.time[n0:n1] - ds.time[n0], eta)
ax.set_xticks(np.arange(0, 360, 60))
ax.set_xlim(0, 300)
ax.set_ylim(-0.8, 0.8)
ax.grid()
ax.set_xlabel("Time (s)")
ax.set_ylabel("Elevation (m)")
plt.savefig("assets/elevation_time_series.png", dpi=150)
plt.close()

F, f = power_spectrum(detrend(ds.elevation[0].values), 1/20, binsize=128)

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)
ax.loglog(f, F)
ax.set_xlim(0.04, 5)
ax.set_ylim(1e-6, 1e0)
ax.grid()
ax.set_xlabel("Frequency (Hz)")
ax.set_ylabel("Variance density (m²/Hz)")
plt.savefig("assets/elevation_spectrum.png", dpi=200)
plt.close()
