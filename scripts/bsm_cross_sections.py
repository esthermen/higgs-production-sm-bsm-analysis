import numpy as np
import matplotlib.pyplot as plt
import os
import csv


ENERGIES = ["500GeV", "1000GeV", "1500GeV"]
PROCESSES = ["h1h1", "h1h2", "h2h2"]

LUMINOSITIES = {
    "500GeV": 4e6,
    "1000GeV": 8e6,
    "1500GeV": 2.5e6,
}

HBB = 0.584


def load_cross_section(energy, process):
    path = os.path.join(
        "..", "data", "raw", "bsm", energy, f"{process}.txt"
    )
    return np.loadtxt(path)


def save_scatter(x, b4, values, title, cbar_label, filename):

    plt.figure(figsize=(8, 6))
    scatter = plt.scatter(x, b4, c=values, cmap="viridis")
    cbar = plt.colorbar(scatter)
    cbar.set_label(cbar_label)

    plt.xlabel("x (GeV)")
    plt.ylabel("b4")
    plt.title(title)
    plt.tight_layout()

    output_path = os.path.join(
        "..", "results", "plots", filename
    )

    plt.savefig(output_path, dpi=300)
    plt.close()


def compute_events(process, sigma, energy):

    L = LUMINOSITIES[energy]

    if process == "h1h1":
        return sigma * L * HBB**2
    elif process == "h1h2":
        return sigma * L * HBB
    else:
        return sigma * L


def generate_summary_csv():

    output_file = os.path.join(
        "..", "data", "processed", "bsm_summary.csv"
    )

    with open(output_file, mode="w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "Energy",
            "Process",
            "MaxSigma",
            "MeanSigma",
            "MaxEvents",
            "Max_x",
            "Max_b4",
        ])

        for energy in ENERGIES:
            for process in PROCESSES:

                data = load_cross_section(energy, process)

                x = data[:, 0]
                b4 = data[:, 1]
                sigma = data[:, 2] * 1000  # fb

                events = compute_events(process, sigma, energy)

                max_index = np.argmax(sigma)

                writer.writerow([
                    energy,
                    process,
                    np.nanmax(sigma),
                    np.nanmean(sigma),
                    np.nanmax(events),
                    x[max_index],
                    b4[max_index],
                ])

    print("Summary CSV generated.")


def main():
    generate_summary_csv()


if __name__ == "__main__":
    main()
