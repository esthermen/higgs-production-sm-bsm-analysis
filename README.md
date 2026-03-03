![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Physics](https://img.shields.io/badge/Field-Computational%20Physics-red)
![Status](https://img.shields.io/badge/Status-Research%20Project-success)

# Energy Dependence of Scalar Pair Production in an Extended Higgs Sector

This repository presents a computational study of scalar pair production in an extended Higgs sector model at electron–positron colliders.

The analysis focuses on the energy scaling behaviour and relative hierarchy of production channels involving light and heavy scalar states. Event generation was performed using MadGraph5_aMC@NLO, and numerical post-processing was developed in Python.

---

## Scientific Objectives

The primary goals of this project are:

- To compute production cross sections for:
  - h1h1  
  - h1h2  
  - h2h2  
- To analyze their dependence on center-of-mass energy (500, 1000, 1500 GeV)
- To estimate expected event yields assuming fixed integrated luminosity
- To compare relative production strengths between scalar channels

The focus is not on a direct SM vs BSM comparison, but rather on the internal hierarchy and energy dependence within the extended scalar sector.

---

## Methodology

- Matrix element generation using MadGraph5_aMC@NLO  
- Extraction of cross sections from simulation output  
- Statistical post-processing using NumPy  
- Log-scale visualization for hierarchical comparison  
- Energy scaling analysis across fixed √s values  

All numerical quantities are derived from matrix-element-level simulations, without detector effects, focusing exclusively on parton-level production dynamics.

NaN values arising from kinematic restrictions are handled using nan-aware statistical estimators.

---

## Results Overview

### BSM Results

![BSM Example](results/plots/bsm_h1h1_500GeV.png)

The light-scalar channel (h1h1) dominates at lower energies due to kinematic accessibility and coupling structure, while mixed and heavy channels increase in relevance at √s = 1500 GeV, reflecting the opening of phase space for heavier scalar production.

### SM Validation

![SM Validation](results/plots/sm_energy_scan.png)

The Standard Model calculation was used as a validation benchmark against previously established results, ensuring consistency of the simulation and post-processing pipeline.

---

## Computational Aspects

The analysis pipeline is fully modular, separating:

- Model parameter computation  
- Cross-section post-processing  
- Statistical aggregation  
- Visualization  

This structure ensures reproducibility and facilitates extension to additional parameter scans or alternative collider configurations.

---

## Project Structure

```
higgs-production-sm-bsm-analysis/

├── model/               # Theoretical description of the model  
├── scripts/             # Python analysis scripts  
├── data/  
│   ├── raw/             # MadGraph output files  
│   │   ├── sm/  
│   │   └── bsm/  
│   │       ├── 500GeV/  
│   │       ├── 1000GeV/  
│   │       └── 1500GeV/  
│   └── processed/       # Processed numerical summaries  
│  
└── results/  
    ├── plots/           # Generated figures  
    └── tables/          # Numerical comparison tables  
```

---

## Reproducibility

All numerical results and plots in this repository can be reproduced by running:

```bash
python scripts/bsm_cross_sections.py
python scripts/process_energy_analysis.py
```

The analysis assumes raw cross section outputs generated with MadGraph5_aMC@NLO.

---

## Potential Extensions

- Differential cross section analysis  
- Parameter scan over scalar masses  
- Comparison with EFT approximations  
- Collider luminosity scaling studies  

---

## Full Thesis

The complete undergraduate thesis is available here:

[Download PDF](docs/TFG_Esther_Menendez_Ibanez.pdf)

---

## Author

Esther Menéndez Ibáñez  
BSc Physics  
Specialization in Computational Physics and Numerical Simulation
