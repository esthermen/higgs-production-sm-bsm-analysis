# Higgs Production in SM and Extended Scalar Models

This repository contains a computational analysis of scalar production processes in the Standard Model (SM) and in an extended scalar sector model.

The study is based on event generation performed with MadGraph and numerical post-processing developed in Python.

---

## Project Structure

higgs-production-sm-bsm-analysis/

│  
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

---

## Physics Scope

Energy-dependent production analysis of scalar bosons.

### Standard Model (SM)
- Multi-channel Higgs production energy scan.

### Extended Scalar Sector (BSM)
Study of scalar pair production in electron-positron collisions:
- e⁺ e⁻ → h1 h1  
- e⁺ e⁻ → h1 h2  
- e⁺ e⁻ → h2 h2  

Evaluated at:
- 500 GeV  
- 1000 GeV  
- 1500 GeV  

---

## Tools Used

- MadGraph5_aMC@NLO  
- Python 3  
- NumPy  
- Matplotlib  

---

## 📄 Full Thesis

The complete undergraduate thesis is available here:

[Download PDF](docs/TFG_Esther_Menendez_Ibanez.pdf)

---
## Author

Esther Menéndez Ibáñez  
BSc Physics  
Computational Physics & Simulation
