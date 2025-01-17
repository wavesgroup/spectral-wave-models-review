<section>

## A brief history of spectral wave models
</section>


<section>

## Gelci (1960): Technical Aspects of Numerical Forecasting of Swell

<div style="display: flex; justify-content: space-between; align-items: center;">
    <div style="flex: 1; padding-right: 20px;">
        <ul>
            <li>First spectral wave model</li>
            <li>Propagation on a sphere and growth due to wind</li>
            <li>4 frequencies, 9 directions, 13 wind speed values!</li>
            <li>Numerical design constrained by available hardware (i.e. grid had to fit the teletype)</li>
        </ul>
    </div>
    <div style="flex: 1;">
        <img src="assets/gelci1.jpg" style="width: 100%;">
    </div>
</div>
</section>

<section>

<img class="stretch" src="assets/gelci2.jpg">
</section>

<section>

<img class="stretch" src="assets/gelci3.jpg">
</section>


<section>

## Spectral model generations (Young, 1999)

<table style="width: 100%; border-collapse: collapse; font-size: 0.7em;">
    <tr>
        <td style="border: 1px solid black; padding: 10px; text-align: center; vertical-align: middle;"></td>
        <td style="border: 1px solid black; padding: 10px; text-align: center; vertical-align: middle;">$S_{in}$</td>
        <td style="border: 1px solid black; padding: 10px; text-align: center; vertical-align: middle;">$S_{nl}$</td>
        <td style="border: 1px solid black; padding: 10px; text-align: center; vertical-align: middle;">$S_{ds}$</td>
    </tr>
    <tr>
        <td style="border: 1px solid black; padding: 10px; text-align: center; vertical-align: middle;">First Generation</td>
        <td style="border: 1px solid black; padding: 10px; text-align: center; vertical-align: middle;">
            <ul>
                <li>Based on growth rate measurements</li>
                <li>Large in magnitude</li>
            </ul>
        </td>
        <td style="border: 1px solid black; padding: 10px; text-align: center; vertical-align: middle;"></td>
        <td style="border: 1px solid black; padding: 10px; text-align: center; vertical-align: middle;">
            <ul>
                <li>Saturation limit</li>
            </ul>
        </td>
    </tr>
    <tr>
        <td style="border: 1px solid black; padding: 10px; text-align: center; vertical-align: middle;">Second Generation</td>
        <td style="border: 1px solid black; padding: 10px; text-align: center; vertical-align: middle;">
            <ul>
                <li>Based on flux measurements</li>
                <li>Smaller than 1st generation</li>
            </ul>
        </td>
        <td style="border: 1px solid black; padding: 10px; text-align: center; vertical-align: middle;">
            <ul>
                <li>Parametric form</li>
                <li>Limited flexibility</li>
            </ul>
        </td>
        <td style="border: 1px solid black; padding: 10px; text-align: center; vertical-align: middle;">
            <ul>
                <li>Saturation limit, as in 1st Generation</li>
            </ul>
        </td>
    </tr>
    <tr>
        <td style="border: 1px solid black; padding: 10px; text-align: center; vertical-align: middle;">Third Generation</td>
        <td style="border: 1px solid black; padding: 10px; text-align: center; vertical-align: middle;">
            <ul>
                <li>Based on flux measurements</li>
                <li>Stress coupled to sea state</li>
            </ul>
        </td>
        <td style="border: 1px solid black; padding: 10px; text-align: center; vertical-align: middle;">
            <ul>
                <li>Approximate form of Boltzman integral</li>
            </ul>
        </td>
        <td style="border: 1px solid black; padding: 10px; text-align: center; vertical-align: middle;">
            <ul>
                <li>Explicit form</li>
            </ul>
        </td>
    </tr>
</table>

</section>


<section>

> All present second-generation models suffer from limitations in the parameterization of the nonlinear energy transfer.
>
> -- SWAMP Group, 1986
</section>

<section>

## Current generation wave models

### (a non-exhaustive summary)

* 1984: WAM Group formed by Klaus Hasselmann
  - Exact $S_{nl}$ and its Discrete Interaction Approximation (DIA)
  - Improved $S_{in}$ and $S_{ds}$
* 1991: WAVEWATCH with treatment of unsteady depths and currents
* 1999: SWAN with improved nearshore dynamics and triad interactions
* 2012: UMWM, Donelan $S_{in}$ and $S_{ds}$, and back to a simple, advective $S_{nl}$
for computational efficiency
</section>


<section>

## What are spectral models useful for in 2025?

1. **Wave forecasting**: Navigation, human safety, coastal and offshore engineering, battlespace environment, recreation and tourism (e.g. surf), etc.
2. **Wave research**: Better understanding of wave physics and related processes
3. **Remote sensing**: Interpretation of remote sensing products (satellite, aerial, ground radars etc.)
4. **Surface boundary conditions to circulation models**: Earth system coupling
</section>
