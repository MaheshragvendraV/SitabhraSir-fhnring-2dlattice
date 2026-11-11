# Prof. Sinha's suggestion: change the dimension of the lattice.
# 20 x 20 square lattice, each oscillator coupled to its 4 neighbours through v (periodic edges).
# Run:  python lattice2d.py      (about 20 seconds)

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from fhn import alpha, k, eps, period


def lattice(L, b, Dv, periods, seed):
    n = L * L
    T0 = period(b)
    rng = np.random.default_rng(seed)
    u0 = rng.uniform(-0.2, 1.0, n)
    v0 = rng.uniform(-0.05, 0.25, n)

    def f(t, y):
        u = y[:n].reshape(L, L)
        v = y[n:].reshape(L, L)
        # average v of the 4 neighbours: up, down, left, right
        neighbours = (np.roll(v, 1, axis=0) + np.roll(v, -1, axis=0) +
                      np.roll(v, 1, axis=1) + np.roll(v, -1, axis=1)) / 4
        du = u*(1 - u)*(u - alpha) - v
        dv = eps*(k*u - v - b) + Dv*(neighbours - v)
        return np.concatenate([du.ravel(), dv.ravel()])

    t = np.linspace(0, periods*T0, 600)
    sol = solve_ivp(f, (0, t[-1]), np.concatenate([u0, v0]), method="LSODA", t_eval=t, rtol=1e-6, atol=1e-8)
    return sol.t / T0, sol.y[:n]


L = 20
fig, axes = plt.subplots(1, 2, figsize=(9, 4.2))
for ax, Dv in zip(axes, [7e-4, 3.5e-3]):
    t, u = lattice(L, b=0.175, Dv=Dv, periods=30, seed=0)
    size = np.ptp(u[:, t > 25], axis=1)                # how much each node still oscillates
    pic = ax.imshow(u[:, -1].reshape(L, L), cmap="viridis", vmin=-0.3, vmax=1)
    ax.set_title(f"Dv = {Dv}:  {np.mean(size > 0.5)*100:.0f}% still oscillating")
    ax.axis("off")
    fig.colorbar(pic, ax=ax, label="u")
    print(f"Dv = {Dv}: {np.mean(size > 0.5)*100:.0f}% of nodes still oscillating")

plt.tight_layout()
plt.savefig("figures/lattice2d.png", dpi=200)
plt.show()
