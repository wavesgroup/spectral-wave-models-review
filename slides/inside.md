<section>

## How do spectral wave models work?
</section>

<section>

## Problem: Why can't we just solve the RANS equations for waves?

* Computationally prohibitive: resolving the shortest ($\mathcal{O}(0.1\ m)$ and
the longest ($\mathcal{O}(100\ m)$ waves spans 3 orders of magnitude
* Basin scale ($\mathcal{O}(100\ km)$ and
* Time scale ($\mathcal{O}(1\ day)$)
</section>


<section>

## Fundamental principles

* Small-amplitude waves over slowly-varying currents and bathymetry
* Solve for the wave energy probability distribution, not for instantaneous elevation
</section>



<section>

## Governing equations

Conservation of wave action, $\mathcal{N} \equiv \mathcal{E} / \sigma$:

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

## Wave action balance in Fourier space

If wave action is expressed in Fourier space as $\mathcal{N}(\mathbf{x}, k, \theta)$, then

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

## Analogy to RANS

</section>


<section>

## The good, the bad, and the ugly of spectral wave models
</section>

<section>

## The good

* One prognostic equation (wave action balance)
* Largely wind-driven
* Linear equation (no chaos)
</section>

<section>

## The bad

* **Highly multidimensional**: Every grid point has $\mathcal{O}(10^3)$ degrees of freedom
* **Computationally dense**: All source terms evaluated everywhere, for all directions and frequencies
</section>

<section>

## The ugly

* Sources and sinks
* We don't fully understand how waves grow
* We don't fully understand how waves dissipate
</section>