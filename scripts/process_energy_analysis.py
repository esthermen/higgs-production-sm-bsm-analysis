import numpy as np
import os
import csv


ENERGIES = ["500GeV", "1000GeV", "1500GeV"]
PROCESSES = ["h1h1", "h1h2", "h2h2"]


def load_cross_section(energy, process):
    path = os.path.join(
        "..", "data", "raw", "bsm", energy, f"{process}.txt"
    )
    return np.loadtxt(path)


def generate_process_energy_table():

    output_path = os.path.join(
        "..", "results", "tables", "bsm_process_energy_comparison.csv"
    )

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, mode="w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "Energy",
            "SigmaMax_h1h1",
            "SigmaMax_h1h2",
            "SigmaMax_h2h2",
            "Ratio_h1h2_over_h1h1",
            "Ratio_h2h2_over_h1h1"
        ])

        for energy in ENERGIES:

            sigmas = {}

            for process in PROCESSES:
                data = load_cross_section(energy, process)
                sigma = data[:, 2] * 1000  # convert to fb
                print(energy, process, np.nanmax(sigma))
                sigmas[process] = np.nanmax(sigma)

            ratio_12 = sigmas["h1h2"] / sigmas["h1h1"]
            ratio_22 = sigmas["h2h2"] / sigmas["h1h1"]

            writer.writerow([
                energy,
                sigmas["h1h1"],
                sigmas["h1h2"],
                sigmas["h2h2"],
                ratio_12,
                ratio_22
            ])

    print("Process vs Energy comparison table generated.")


if __name__ == "__main__":
    generate_process_energy_table()
