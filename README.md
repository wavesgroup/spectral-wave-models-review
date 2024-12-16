# spectral-wave-models-review

Slides for Milan's keynote at ASI-2025 at the University of Melbourne.

**Title:** Everything you wanted to know about spectral wave models but were afraid to ask

**Abstract:**
Phase-averaged spectral wave models are modern, computationally efficient methods for
predicting the distribution of ocean surface waves across scales—from lakes and
estuaries to global swell patterns. Rather than solving for the elevation at scales
smaller than individual waves, as phase-resolved models do, spectral wave models
predict a probability distribution of wave action in frequency-direction space at
each geographical location. These models are run operationally by national centers
around the world in support of marine safety and operations, coastal
infrastructure, remote sensing interpretation, and more.

In this talk, we will review (a) the history behind modern third-generation wave
models; (b) how they work under the hood; and (c) the state-of-the-art of wave
model source functions, which continue to improve to this day. After the review, we
will explore practical applications of the University of Miami Wave Model, designed
for easy coupling with weather and ocean circulation models. I will conclude with a
personal outlook on spectral wave models in the context of current scientific and
technological frontiers: (1) momentum-conserving wind-wave-current coupling; (2)
emerging heterogeneous hardware architectures; and (3) machine learning methods to
emulate and accelerate spectral.

Slides are hosted [here](https://wavesgroup.github.io/spectral-wave-models-review).

Slides are made with [reveal.js](https://github.com/hakimel/reveal.js)
and the associated code is subject to its license.
A copy of the reveal.js server is included in this repository for convenience,
so you can run the slides locally like this:

```
npm install
npm start
```
