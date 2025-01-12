<section>

## Frontier challenges and applications
</section>


<section>

## Accounting for waves and current shear in wind stress calculations

<div style="display: flex; justify-content: space-between;">
    <div style="flex: 1; padding-right: 10px;">
        <img src="assets/sctt_blm_fig02.png" alt="Wave-current interaction diagram">
    </div>
    <div style="flex: 2; padding-left: 10px;">
        <h4>Relative change in stress when accounting for waves and sheared current</h4>
        <img src="assets/sctt_blm_fig09.png" alt="Wave-current stress results">
    </div>
</div>

<div class="reference">Ortiz-Suslow et al. (2025), in review at Boundary-Layer Meteorology</div>
</section>


<section>

## Waves in alien seas

<div style="display: flex; justify-content: space-between;">
    <div style="flex: 1;">
        <ul style="font-size: 0.9em;">
            <li>Planet-agnostic spectral wave model development based on UMWM</li>
            <li>Generalize the code to run with arbitrary $g$, fluid densities and viscosities and surface tension</li>
            <li>Motivated by the recent discovery of waves on Titan's methane lakes</li>
            <li>
              Led by <a href="https://ugschneck.com">Una Schneck</a> (MIT, Planetary Sciences),
              and <a href="https://astro.cornell.edu/charlene-charlie-detelich">Charlie Detelich</a>
              and <a href="https://astro.cornell.edu/alexander-hayes">Alex Hayes</a> (Cornell U., Astronomy)</li>
        </ul>
    </div>
    <div style="flex: 1;">
        <h4>Sig. wave height at 100 km fetch on various planets</h4>
        <img src="assets/schneck_alien_waves.png" alt="Waves in alien seas">
    </div>
</div>

</section>


<section>

### Wave seasonality on Titan's methane lakes using UMWM

#### (Charlie Detelich and Alex Hayes, Cornell U.)

<div style="display: flex; justify-content: space-between;">
    <div style="flex: 1; padding-right: 10px;">
        <h4>Ontario Lachus</h4>
        <img src="assets/detelich_ontario_Hs.png" style="width: 100%;">
    </div>
    <div style="flex: 1; padding-left: 10px;">
        <h4>Ligeia Mare</h4>
        <img src="assets/detelich_ligeia_Hs.png" style="width: 100%;">
    </div>
</div>
</section>


<section>

## Running on emerging architectures (GPUs)

* Most spectral wave models are written in Fortran, mainly due to
  - Fortran's ease of use for scientists
  - Great support for high-performance computing.
* Emerging accelerator architectures like GPUs are rapidly evolving,
initially driven by the video game industry and more recently by AI.
* Fortran compiler vendors (NVIDIA, AMD, Intel) are slowly catching up with their
compilers generating code for GPUs.
* Software design of wave models needs to adapt to the new hardware.
</section>


<section>

## Why spectral wave models are a great fit for machine learning

* Source terms are computationally dense and expensive
  ($S_{ds}$ and $S_{nl}$ are in most cases non-local in spectral space)
* Can be emulated with neural networks (everything is a `matmul`!)
* `matmul` is already universally portable on GPUs, so manual porting may not be needed.
</section>


<section style="display: flex; flex-direction: column;">

<div style="flex: 8">

## neural-fortran: A parallel deep learning framework for Fortran applications

* Created to enable pure Fortran ML in Fortran applications
* Training and inference of arbitrarily deep dense and convolutional networks
* Optimizers: SGD, RMSProp, Adagrad, Adam, AdamW
* Data parallelism with Fortran 2018 collectives
* Used in over a dozen published studies from chemistry and combustion to weather and climate
* https://github.com/modern-fortran/neural-fortran

<div class="reference"><a href="https://doi.org/10.1145/3323057.3323059">Curcic (2019)</a></div>
</div>

<div style="flex: 3">
  <div style="display: flex; align-items: center; justify-content: center; gap: 20px;">
    <img height=90 style="margin: auto 0;" src="assets/nasa.png"></img>
    <img height=40 style="margin: auto 0;" src="assets/gsoc.png"></img>
    <img height=40 style="margin: auto 0;" src="assets/wur.svg"></img>
  </div>
</div>
</section>


<section>

## Single-core CPU performance in training

<img src="assets/benchmark_dense_mnist.png" width="80%"></img>

$\rightarrow$ neural-Fortran is 2x ahead of a leading ML framework on CPUs.
</section>