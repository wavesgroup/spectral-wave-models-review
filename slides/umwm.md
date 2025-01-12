<section>

## The University of Miami Wave Model


<div style="display: flex; justify-content: space-between;">
    <div style="flex: 1; padding-right: 10px;">
        <img src="assets/geos-umwm-swh.png" style="width: 100%;">
    </div>
    <div style="flex: 1; padding-left: 10px;">
        <img src="assets/geos-umwm-dwp.png" style="width: 100%;">
    </div>
</div>

<h4>Snapshots of significant height and dominant period from UMWM coupled to NASA's global GEOS model</h4>

</section>

<section>

## The University of Miami Wave Model (UMWM)

* Originated by Mark Donelan in the 2000s
* Initially a single self-contained MATLAB script
* Later adapted to Fortran+MPI for distributed parallel computing and coupling with weather and ocean models
* Maintained and available at: https://github.com/umwm/umwm
* https://umwm.org

<div class="reference"><a href="https://doi.org/10.1029/2011JC007787">Donelan et al. (2012)</a></div>
</section>


<section>

## Design principles

* Simple, small (< 5K lines of code), parallel, and fast
* Easy to run
* Source function forms based on laboratory and tuned to field data
* Expose all wind-wave and wave-current vector fluxes
* Tailored to coupling with other models
</section>


<section>

## UMWM physics, in a nutshell

$$
S_{in}(k,\theta) =
\mathcal{A} \frac{\rho_a}{\rho_w}
\left(\frac{U_{\lambda/2}}{C_p} - 1\right)
\left|\frac{U_{\lambda/2}}{C_p} - 1\right|
\omega F(k,\theta)
$$


$$
S_{ds}(k, \theta) =
\mathcal{B} [1 + \mathcal{C} \chi ^2(k,\theta)]^2 [F(k,\theta) k^4]^\frac{5}{2} \omega F(k,\theta)
$$

$$
S_{nl}(k,\theta) = \mathcal{D} S_{ds}(k,\theta) \frac{\partial F}{\partial k}
$$

where $\mathcal{A}$, $\mathcal{B}$, $\mathcal{C}$, $\mathcal{D}$ are tunable coefficients.
</section>


<section>

## Example UMWM applications in the field

* Coupled atmosphere-wave-ocean prediction (Chen and Curcic, 2016; Li et al., 2018; Dietrich et al., 2018)
* Wave contributions to Lagrangian transport in hurricanes (Curcic et al., 2016) 
* Implemented in NASA's global GEOS model for whitecaps and aerosol production (Darmenov et al., 2018)
* Waves on methane lakes of Titan (Hayes et al., 2013)
* Impacts of sea-spray on fluxes in hurricanes (Barr et al., 2023)
</section>


<section>

## New implementation of UMWM in progress

15 years later, new requirements emerge:

* Portable to GPUs
* Easy to integrate with machine learning training flows
* Allow constructing a hierarchy of wave models of various complexity
* Generalizable to other planets
</section>