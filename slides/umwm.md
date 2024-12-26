<section>

## The University of Miami Wave Model
</section>

<section>

## The University of Miami Wave Model (UMWM)

* Created by late Prof. Mark Donelan in the 2000s
* Initially a single self-contained MATLAB script
* Later adapted to Fortran+MPI for distributed parallel computing and coupling with other models
* Maintained and available via: https://github.com/umwm/umwm
* https://umwm.org
</section>


<section>

## Design principles

* Simple and small
* Opinionated source functions
* Expose all wind-wave and wave-current vector fluxes
* Easy coupling with other models via ESMF
</section>


<section>

## UMWM physics
</section>


<section>

## Showcase of applications

* Donelan et al. (2012)
* Curcic et al. (2016)
* Chen and Curcic (2016)
* GEOS-UMWM
* Barr et al. (2023)
</section>


<section>

## New implementation of UMWM

15 years later, new design principles emerge:

* Portable to GPUs
* Easy to integrate with ML training flows
* Allow constructing a hierarchy of wave models of various complexity
</section>