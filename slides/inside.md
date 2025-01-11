<section>

## How do spectral wave models work?
</section>


<section>

## Fundamental principles

* Small-amplitude waves over slowly-varying currents and bathymetry
* Solve for the wave energy probability distribution, not for instantaneous elevation
</section>



<section>

## Governing equations

Conservation of wave action, $\mathcal{N} \equiv \mathcal{E} / \sigma$ (Whitham, 1965):

$$
\frac{\partial \mathcal{N}}{\partial t} + \nabla\left(C_g \mathcal{N}\right) = 0
$$

$\mathcal{N}$ is (mostly) conserved for small-amplitude waves on slowly-varying
currents (Bretherton & Garrett, 1968)

Zakharov (1968) also independently found that wave energy is a Hamiltonian.

</section>

<section>

## Governing equations (cont.)

Dispersion relationship for small-amplitude gravity waves:

$$
\sigma^2 = gk\tanh(kh)
$$

Determines how waves of different wavelengths travel at different speeds.

Optionally, may include surface tension effects for the gravity-capillary wave regime.

</section>


<section>

## Wave action balance in spectral space

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

## Waves not only propagate but also grow, dissipate, and evolve in the wavenumber space

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
* Expressing growth and dissipation in a phase-averaged, spectral form will
inevitably require a parameterization
</section>
