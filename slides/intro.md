<section>

## Intro to linear wave theory
### (Airy, 1845; Stokes 1847)

* Incompressible, irrotational and inviscid flow:

$$
\nabla \cdot \mathbf{u} = \nabla^2 \phi = 0
$$

* Apply boundary conditions:
  - Lateral (periodic)
  - Bottom kinematic (no slip)
  - Free surface dynamic (Bernoulli) and kinematic

</section>


<section>

## Linear wave theory solution

Surface elevation and velocity potential
$$
\eta = a \cos(kx - \omega t)
$$

$$
\phi = \frac{a g}{\omega} e^{kz} \sin(kx - \omega t)
$$

<img src="assets/fig_wave_potential.png" />
</section>


<section>

## Linear wave theory solution (cont.)

<img src="assets/fig_wave_velocities.png" />
</section>


<section>

## Waves induce net material transport
### (Stokes drift)

<video
  width=600
  data-autoplay
  loop
  src="assets/stokes_drift.mp4"
  type="video/mp4">
</video>

<div class="reference">Animation by Nick Pizzo (URI)</div>

</section>


<section>

## Why a spectral approach to wave modeling?
</section>

<section>

### A common view of the ocean surface

<img src="assets/ocean-wave-surface.jpg" style="width: 60%;">

$\rightarrow$ Many waves of many scales in many directions!
</section>


<section>

## Why not solve the RANS equations for waves?

* Models exist, e.g. shallow water equations, Boussinesq, etc.
* Computationally prohibitive: resolving the shortest ($\mathcal{O}(cm))$ and
the longest ($\mathcal{O}(100\ m))$ gravity waves spans 5 orders of magnitude
* Basin scales of interest may span $\mathcal{O}(10-10^4\ km)$
* Time scales of interest span $\mathcal{O}(days)$
</section>


<section>

### Measured surface elevation time series, $U_{10} \approx 10$ m/s, fetch $\approx$ 40 km

<img class="stretch" src="assets/elevation_time_series.png">
</section>


<section>

### Spectral representation of the same measurement

<div style="display: flex; justify-content: space-between; align-items: center;">
    <div style="width: 50%; height: auto;">
        <h4>Take a Fourier transform and a power to get variance density $\rightarrow$</h4>
        <img src="assets/elevation_time_series.png" style="width: 100%; height: auto;">
    </div>
    <div style="width: 50%; height: auto;">
        <img src="assets/elevation_spectrum.png" style="width: 100%; height: auto;">
    </div>
</div>
$\rightarrow$ Spectral wave models predict the probability distribution of wave energy,
rather than the surface elevation itself
</section>



<section>

### Waves not only come in different sizes, but also move in different directions

<div style="display: flex; justify-content: space-between; align-items: center;">
    <div style="width: 50%; height: auto;">
        <ul style="font-size: 0.8em;">
            <li>Wavenumber-directional distribution of wave variance</li>
            <p>
                <div><span style="color: black;">➜</span> wind direction</div>
                <div><span style="color: red;">➜</span> peak wave direction</div>
                <div><span style="color: green;">➜</span> mean wave direction</div>
            </p>
            <li>Complex seas often have multiple spectral peaks (windsea, one or more swells)</li>
            <li>This example is from a coupled simulation of Hurricane Sandy (2012)</li>
        </ul>
    </div>
    <div style="width: 50%; height: auto;">
        <img src="assets/umwm_2d_spectrum.png" style="width: 100%; height: auto;">
    </div>
</div>
<div class="reference"><a href="https://doi.org/10.1016/j.ocemod.2015.08.005">Chen & Curcic (2016)</a></div>
</section>

<section>

### Integrated wave quantities from a spectral wave model (ecWAM)

![](assets/era5_Hs_2024-09-01.png)
</section>

<section>

### Integrated wave quantities from a spectral wave model (ecWAM)

![](assets/era5_Tp_2024-09-01.png)
</section>


<section>

## What are spectral models useful for?

1. **Wave forecasting**: Navigation, human safety, coastal and offshore engineering, battlespace environment, recreation and tourism (e.g. surf), etc.
2. **Wave research**: Better understanding of wave physics and related processes
3. **Remote sensing**: Interpretation of remote sensing products (e.g. radar returns)
4. **Surface boundary conditions to circulation models**: Earth system coupling
</section>