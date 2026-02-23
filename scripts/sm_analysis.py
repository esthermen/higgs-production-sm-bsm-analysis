import numpy as np
import matplotlib.pyplot as plt
import os


CHANNELS = ["ZHH", "vvHH", "ZH", "vvH", "eeH", "eeHH", "ttH", "ttHH"]


def load_sm_data(file_path):
    """
    Load tab-separated SM cross section data.
    Each column corresponds to one production channel.
    """
    with open(file_path, "r") as f:
        lines = f.readlines()

    data = [list(map(float, line.strip().split("\t"))) for line in lines]
    data = np.array(data).T

    return data


def energy_range():
    """
    Define center-of-mass energy scan.
    """
    return 2 * np.linspace(0, 600, 200)


def plot_sm_cross_sections(E_range, data, output_path):
    """
    Plot all SM production channels.
    """
    plt.figure(figsize=(8, 6))

    for i in range(data.shape[0]):
        plt.plot(E_range, data[i], label=CHANNELS[i])

    plt.xlabel("Center-of-mass Energy (GeV)")
    plt.ylabel("Cross Section")
    plt.yscale("log")
    plt.legend()
    plt.grid(True, linestyle="--", linewidth=0.5)
    plt.tight_layout()

    plt.savefig(output_path, dpi=300)
    plt.close()


def main():

    input_file = "../data/raw/sm/xsecs.txt"
    output_plot = "../results/plots/sm_energy_scan.png"

    E_range = energy_range()
    data = load_sm_data(input_file)

    plot_sm_cross_sections(E_range, data, output_plot)

    print("SM energy scan processed successfully.")


if __name__ == "__main__":
    main()
