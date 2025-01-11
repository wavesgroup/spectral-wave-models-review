<section>

## Why a spectral approach to wave modeling?
</section>

<section>

### A common view of the ocean surface

<img src="assets/ocean-wave-surface.jpg" style="width: 60%;">

$\rightarrow$ Many waves of many scales in many directions!
</section>


<section>

## Why not just solve the RANS equations for waves?

* Models exist (e.g. shallow water equations, Boussinesq, etc.)
* Computationally prohibitive: resolving the shortest ($\mathcal{O}(0.1\ m)$ and
the longest ($\mathcal{O}(100\ m)$ waves spans 3 orders of magnitude
* Basin scales of interest may span $\mathcal{O}(10^2-10^4\ km)$
* Time scales of interest ($\mathcal{O}(days)$)
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

TODO make this an animation
</section>

<section>

### Integrated wave quantities from a spectral wave model (ecWAM)

![](assets/era5_Tp_2024-09-01.png)

TODO make this an animation
</section>