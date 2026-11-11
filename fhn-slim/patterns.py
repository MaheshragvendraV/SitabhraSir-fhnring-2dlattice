# Reproduces the ring patterns of Fig. 2(a) in Janaki et al. (2019): ring of 20 oscillators
# Run:  python patterns.py      (about 30 seconds)

import matplotlib.pyplot as plt
from fhn import ring

cases = [  # (b, Dv, seed, name)
    (0.05,  2.5e-3, 0, "synchronised"),
    (0.175, 1.8e-3, 0, "travelling front (GS)"),
    (0.175, 1.8e-3, 2, "oscillation death (SPOD), same b and Dv!"),
    (0.10,  2.5e-3, 0, "chimera"),
]

fig, axes = plt.subplots(2, 2, figsize=(11, 6))
for ax, (b, Dv, seed, name) in zip(axes.flat, cases):
    t, u = ring(20, b, Dv, periods=50, seed=seed)
    last = t > 40                                     # show only the last 10 periods
    pic = ax.pcolormesh(t[last], range(20), u[:, last], cmap="viridis", vmin=-0.3, vmax=1)
    ax.set_title(f"{name}\nb = {b}, Dv = {Dv}, seed = {seed}")
    ax.set_xlabel("time (periods)")
    ax.set_ylabel("node")
    fig.colorbar(pic, ax=ax, label="u")

plt.tight_layout()
plt.savefig("figures/ring_patterns.png", dpi=200)
plt.show()
