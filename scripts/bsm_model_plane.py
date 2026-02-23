import numpy as np
import matplotlib.pyplot as plt
import os


def compute_model_plane():

    n1 = 10
    n2 = 14

    b4_values = np.linspace(0, 1, n1)
    x_values = np.linspace(33, 47, n2)

    X, B4 = np.meshgrid(x_values, b4_values)

    M_H = np.zeros_like(X)
    KAPPA = np.zeros_like(X)
    WIDTH_H = np.zeros_like(X)
    LhhH = np.zeros_like(X)
    LhHH = np.zeros_like(X)
    LHHH = np.zeros_like(X)

    v = 246
    mh = 125.09
    lam = 0.18

    for i in range(n1):
        for j in range(n2):

            x = X[i, j]
            b4 = B4[i, j]

            a1 = -32000 / x
            b3 = -560 * np.sqrt(b4)

            ms_2 = b3*x + 2*b4*x**2 - a1*v**2/(4*x)
            mhp_2 = 2*lam*v**2

            a2 = (1/(2*x))*(-2/v*np.sqrt(
                2*ms_2*lam*v**2 - 2*mh**2*lam*v**2 +
                mh**4 - mh**2*ms_2
            ) - a1)

            mhps_2 = v/2*(a1 + 2*a2*x)

            mH = np.sqrt(0.5*(mhp_2+ms_2+(np.abs(mhp_2-ms_2))
                              *np.sqrt(1+(2*mhps_2/(mhp_2-ms_2))**2)))

            if not (458 <= mH <= 660):
                M_H[i, j] = np.nan
                continue

            M_H[i, j] = mH

            alpha = np.arccos(
                np.cos(0.5*np.arcsin(2*mhps_2/(mH**2-mh**2)))
            )

            lhhH = (1/(4*v))*(
                (a1+2*a2*x)*np.cos(alpha)**3
            )

            lhhhSM = 0.129
            kappa = lhhH / lhhhSM

            KAPPA[i, j] = kappa
            LhhH[i, j] = lhhH

    return X, B4, M_H, KAPPA, LhhH


def plot_plane(X, B4, quantity, label, filename):

    plt.figure(figsize=(8, 6))
    scatter = plt.scatter(X, B4, c=quantity, cmap='viridis')
    cbar = plt.colorbar(scatter)
    cbar.set_label(label)

    plt.xlabel("x (GeV)")
    plt.ylabel("b4")
    plt.tight_layout()

    output_path = os.path.join(
        "..", "results", "plots", filename
    )

    plt.savefig(output_path, dpi=300)
    plt.close()


def main():

    X, B4, M_H, KAPPA, LhhH = compute_model_plane()

    plot_plane(X, B4, M_H, "mH (GeV)", "bsm_mH_plane.png")
    plot_plane(X, B4, KAPPA, "kappa_lambda", "bsm_kappa_plane.png")
    plot_plane(X, B4, LhhH, "lambda_hhH", "bsm_lambda_plane.png")

    print("BSM model plane computed successfully.")


if __name__ == "__main__":
    main()
