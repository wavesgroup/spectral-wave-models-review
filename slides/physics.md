<section>

## Spectral wave model physics

### (a.k.a source functions)

$$
S_{tot} = S_{in} + S_{ds} + S_{nl}\ +\ ...
$$
</section>


<section>

## Wave growth by wind ($S_{in}$)

* Several partly competing theories and interpretations:
Jeffreys (1924), Phillips (1957), Miles (1957), Belcher & Hunt (1993), etc.
* All share the idea that waves grow by the air pressure gradient between
the two faces of a wave crest
* Modern $S_{in}$ functions also provide a mechanism for dissipation when swell
outruns wind
</section>


<section>

## $S_{in}$ in a nutshell

$$
S_{in}(k,\theta) \propto \frac{\rho_a}{\rho_w} \left( \frac{u_x}{c_p} \cos\varphi - 1 \right)^n \omega F(k,\theta)
$$

$u_x$ is a scaling velocity characteristic of the air
(e.g. friction velocity $u_*$, $U_{\lambda/2}$, etc.)

$\varphi$ is the the wind-wave direction difference
</section>


<section>

## Nonlinear transfer ($S_{nl}$)

* Energy exchanges between the resonant quadruplet of waves:

$$
\omega_1 + \omega_2 = \omega_3 + \omega_4
$$

$$
\mathbf{k}_1 + \mathbf{k}_2 = \mathbf{k}_3 + \mathbf{k}_4
$$

* Exact but costly transfer described by the Boltzmann integral (Hasselmann, 1962; 1963)
* Computationally efficient approximations available:
    - Webb-Resio-Tracy & Two-Scale Approximation: algorithmic optimizations to exact $S_{nl}$
    - Discrete Interaction Approximation (DIA, Hasselmann et al., 1985)
    - Generalized Multiple DIA (Tolman, 2010)
</section>


<section>

## Wave dissipation by whitecapping ($S_{ds}$)

* Highly nonlinear in steepness
* Early theories (Hasselmann, 1974; Phillips, 1985) assumed whitecapping is
local in wavenumber space
* Donelan (2001) added a nonlocal term (based on cumulative mean square slope)
to account for preferential steepening of short waves by longer waves.
* Modern $S_{ds}$ functions (Ardhuin et al., 2010; Rogers et al., 2012; Donelan et al., 2012; Romero, 2019)
all use some combination of saturation-based dissipation and cumulative steepening
by longer waves.

</section>


<section>

## Source terms are integral to wind-wave (form) and wave-current (dissipative) momentum fluxes

$$
\tau_{form} = \rho_w g \int \int S_{in}(k,\theta) \frac{F(k,\theta)}{C_p}\ dk\ d\theta
$$

$$
\tau_{diss} = \rho_w g \int \int S_{ds}(k,\theta) \frac{F(k,\theta)}{C_p}\ dk\ d\theta
$$


$\tau_{form}$ and $\tau_{diss}$ are part of the surface boundary conditions for
weather and ocean circulation models.
</section>