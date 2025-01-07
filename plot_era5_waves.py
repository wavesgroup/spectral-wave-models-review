import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import xarray
import matplotlib

matplotlib.rcParams['font.size'] = 14
ds = xarray.open_zarr(
    'gs://gcp-public-data-arco-era5/ar/full_37-1h-0p25deg-chunk-1.zarr-v3',
    chunks=None,
    storage_options=dict(token='anon'),
)
ds = ds.sel(time=slice(ds.attrs['valid_time_start'], ds.attrs['valid_time_stop']))


time = "2024-09-01"

ds = ds.sel(time=time)

lon = ds.longitude
lat = ds.latitude
mask = ds.land_sea_mask
Hs = ds.significant_height_of_combined_wind_waves_and_swell
Tp = ds.peak_wave_period

Hs0 = ds.significant_height_of_wind_waves
Hs1 = ds.significant_wave_height_of_first_swell_partition
Hs2 = ds.significant_wave_height_of_second_swell_partition
Hs3 = ds.significant_wave_height_of_third_swell_partition

Tm0 = ds.mean_wave_period_based_on_first_moment_for_wind_waves
Tm1 = ds.mean_wave_period_of_first_swell_partition
Tm2 = ds.mean_wave_period_of_second_swell_partition
Tm3 = ds.mean_wave_period_of_third_swell_partition

fig = plt.figure(figsize=(12, 5))
ax = fig.add_subplot(111, aspect='equal')
im = ax.contourf(lon, lat, Hs[-1], np.arange(0, 10.5, 0.5), cmap=cm.inferno)
fig.colorbar(im, ax=ax, ticks=np.arange(0, 11, 1), shrink=0.8)
ax.contour(lon, lat, mask[-1], [0.5], colors='k', linewidths=0.5)
ax.set_ylim(-70, 80)
ax.set_xlim(0, 360)
ax.set_xticks(np.arange(0, 450, 90))
ax.set_title(f"ERA5 Significant wave height (m) on {time}")
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
fig.tight_layout()
plt.savefig(f"assets/era5_Hs_{time}.png", dpi=150)
plt.close()


fig = plt.figure(figsize=(12, 5))
ax = fig.add_subplot(111, aspect='equal')
im = ax.contourf(lon, lat, Tp[-1], np.arange(0, 19, 1), cmap=cm.inferno)
fig.colorbar(im, ax=ax, ticks=np.arange(0, 20, 2), shrink=0.8)
ax.contour(lon, lat, mask[-1], [0.5], colors='k', linewidths=0.5)
ax.set_ylim(-70, 80)
ax.set_xlim(0, 360)
ax.set_xticks(np.arange(0, 450, 90))
ax.set_title(f"ERA5 Peak wave period (s) on {time}")
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
fig.tight_layout()
plt.savefig(f"assets/era5_Tp_{time}.png", dpi=150)
plt.close()


fig, axes = plt.subplots(4, 2, figsize=(16, 14))

for ax in axes.flatten():
    ax.set_aspect('equal')

# Left column - Significant wave heights
heights = [Hs0, Hs1, Hs2, Hs3]
ylabels = ["Windsea", "Swell 1", "Swell 2", "Swell 3"]

# Right column - Mean periods
periods = [Tm0, Tm1, Tm2, Tm3]

# Add column titles only in top row
axes[0,0].set_title("Significant height (m)")
axes[0,1].set_title("Mean period (s)")

# Height ranges for each row
height_ranges = [
    (0, 10, 0.5, 1),  # Windsea: 0-10m
    (0, 8, 0.4, 1),   # Swell 1: 0-8m
    (0, 4, 0.2, 1), # Swell 2: 0-4m
    (0, 2, 0.1, 1) # Swell 3: 0-2m
]

for row in range(4):
    # Plot wave heights with different ranges
    vmin, vmax, step, tick_step = height_ranges[row]
    im_h = axes[row,0].contourf(lon, lat, heights[row][-1], np.arange(vmin, vmax+step, step), cmap=cm.inferno)
    fig.colorbar(im_h, ax=axes[row,0], ticks=np.arange(vmin, vmax+tick_step, tick_step), shrink=0.7)
    axes[row,0].contour(lon, lat, mask[-1], [0.5], colors='k', linewidths=0.5)
    axes[row,0].set_ylim(-70, 80)
    axes[row,0].set_xlim(0, 360)
    axes[row,0].set_xticks(np.arange(0, 450, 90))
    
    # Plot wave periods  
    im_p = axes[row,1].contourf(lon, lat, periods[row][-1], np.arange(0, 19, 1), cmap=cm.inferno)
    fig.colorbar(im_p, ax=axes[row,1], ticks=np.arange(0, 20, 2), shrink=0.7)
    axes[row,1].contour(lon, lat, mask[-1], [0.5], colors='k', linewidths=0.5)
    axes[row,1].set_ylim(-70, 80)
    axes[row,1].set_xlim(0, 360)
    axes[row,1].set_xticks(np.arange(0, 450, 90))

    # Add row labels on the left side
    axes[row,0].set_ylabel(ylabels[row])

plt.savefig(f"assets/era5_components_{time}.png", dpi=150, bbox_inches='tight')
plt.close()
