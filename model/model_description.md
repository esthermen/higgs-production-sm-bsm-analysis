# Model Description

## Standard Model (SM)

In the Standard Model, Higgs production processes are studied as a function of the center-of-mass energy. Cross sections are obtained using MadGraph event generation and post-processed in Python.

The SM analysis includes multiple production channels extracted from a single energy scan file.

## Extended Scalar Sector Model (BSM)

The extended model introduces an additional scalar degree of freedom, leading to two physical Higgs states:

- h1 (light scalar)
- h2 (heavy scalar)

We study scalar pair production in electron-positron collisions:

- e⁺ e⁻ → h1 h1
- e⁺ e⁻ → h1 h2
- e⁺ e⁻ → h2 h2

Cross sections are evaluated at discrete center-of-mass energies:

- 500 GeV
- 1000 GeV
- 1500 GeV

The event generation is performed using MadGraph, and numerical analysis is carried out in Python.
