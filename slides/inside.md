<section>

## How do spectral wave models work?
</section>


<section>

## Fundamental principles

1. Small-amplitude waves over slowly-varying currents and bathymetry
2. Solve for the wave energy PDF, not instantaneous elevation
3. Discretize the spectrum in frequency-directional space
</section>



<section>

## Governing equations

Conservation of wave action, $\mathcal{N} \equiv \mathcal{E} / \sigma$ (Whitham, 1965):

$$
\frac{\partial \mathcal{N}}{\partial t} + \nabla\left(C_g \mathcal{N}\right) = 0
$$

$\mathcal{N}$ is (mostly) conserved for small-amplitude waves on slowly-varying
currents (Bretherton & Garrett, 1968)
</section>

<section>

## Governing equations (cont.)

Dispersion relationship for small-amplitude gravity-capillary waves:

$$
\omega^2 = \left(gk + \frac{\sigma k^3}{\rho_w}\right) \tanh(kd)
$$

Determines how different wavelengths travel at different speeds.

The capillary term determines the wind speed threshold of wave growth.

</section>


<section>

## Wave action density balance in spectral space

If wave action is expressed as $\mathcal{N}(\mathbf{x}, k, \theta)$, then

$$
\frac{\partial \mathcal{N}}{\partial t} +
\frac{\partial}{\partial \mathbf{x}} \left(\dot{\mathbf{x}} \mathcal{N}\right) +
\frac{\partial}{\partial k} \left(\dot{k} \mathcal{N}\right) +
\frac{\partial}{\partial \theta} \left(\dot{\theta} \mathcal{N}\right) = 0
$$

* $\frac{\partial}{\partial \mathbf{x}} \left(\dot{\mathbf{x}} \mathcal{N}\right)$: propagation ($\dot{\mathbf{x}} \equiv C_g$)
* $\frac{\partial}{\partial k} \left(\dot{k} \mathcal{N}\right)$: wavenumber modulation by currents
* $\frac{\partial}{\partial \theta} \left(\dot{\theta} \mathcal{N}\right)$: refraction by depth and currents

</section>

<section>

## Waves also grow, dissipate, and cascade energy to longer scales

$$
\frac{\partial \mathcal{N}}{\partial t} +
\frac{\partial}{\partial \mathbf{x}} \left(\dot{\mathbf{x}} \mathcal{N}\right) +
\frac{\partial}{\partial k} \left(\dot{k} \mathcal{N}\right) +
\frac{\partial}{\partial \theta} \left(\dot{\theta} \mathcal{N}\right)
= S_{tot}
$$

where $S_{tot}$ represents all sources and sinks of wave action:

$$
S_{tot} = S_{in} + S_{ds} + S_{nl} + S_{ice} + ...
$$

</section>


<section>

## The good, the bad, and the ugly of spectral wave models
</section>

<section>

## The good

* Small-amplitude theory works surprisingly well
* One prognostic equation (wave action balance)
* Non-chaotic, unlike weather and ocean circulation
* Dynamics (propagation and refraction) are known and cheap
* Nonlinear transfer is known; although expensive when exact, good approximations exist
* Largely wind-driven
</section>

<section>

## The bad

* **Highly multidimensional**: Every grid point has $\mathcal{O}(10^3)$ degrees of freedom
* **Computationally dense**: All source terms evaluated for all frequencies and directions
</section>

<section>

## The ugly

* Source functions are many, complex, and not well known
* We don't yet fully understand how waves grow or dissipate
* Expressing growth and dissipation in a phase-averaged, spectral form
requires a parameterization, whether theoretical or empirical
</section>