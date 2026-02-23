import numpy as np
import matplotlib.pyplot as plt
import os


ENERGIES = ["500GeV", "1000GeV", "1500GeV"]
PROCESSES = ["h1h1", "h1h2", "h2h2"]


def load_cross_section(energy, process):
    """
    Load cross section file for a given energy and process.
    Expected format: x   b4   sigma
    """
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


def cross_section_analysis():

    for energy in ENERGIES:
        for process in PROCESSES:

            data = load_cross_section(energy, process)

            x = data[:, 0]
            b4 = data[:, 1]
            sigma = data[:, 2] * 1000  # convert to fb

            title = f"{process} production at {energy}"
            filename = f"bsm_{process}_{energy}.png"

            save_scatter(
                x,
                b4,
                sigma,
                title,
                "Cross Section [fb]",
                filename,
            )

    print("Cross section plots generated.")


def event_estimation():

    # Luminosities in fb^-1
    luminosities = {
        "500GeV": 4e6,
        "1000GeV": 8e6,
        "1500GeV": 2.5e6,
    }

    hbb = 0.584  # branching ratio

    for energy in ENERGIES:
        for process in PROCESSES:

            data = load_cross_section(energy, process)

            x = data[:, 0]
            b4 = data[:, 1]
            sigma = data[:, 2]

            L = luminosities[energy]

            if process == "h1h1":
                events = sigma * L * hbb**2

            elif process == "h1h2":
                events = sigma * L * hbb

            else:  # h2h2
                events = sigma * L

            title = f"Expected events {process} at {energy}"
            filename = f"events_{process}_{energy}.png"

            save_scatter(
                x,
                b4,
                events,
                title,
                "Number of events",
                filename,
            )

    print("Event estimation plots generated.")


def main():

    cross_section_analysis()
    event_estimation()


if __name__ == "__main__":
    main()
