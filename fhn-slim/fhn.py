# FitzHugh-Nagumo oscillators coupled through the slow variable v
# Model from Janaki, Menon, Singh & Sinha, Phys. Rev. E 99, 052216 (2019)

import numpy as np
from scipy.integrate import solve_ivp
from scipy.signal import find_peaks

alpha, k, eps = 0.139, 0.6, 0.001      # parameters from the paper


def period(b):
    # period of ONE oscillator with no coupling (used as the unit of time, like the paper)
    def f(t, y):
        u, v = y
        return [u*(1 - u)*(u - alpha) - v, eps*(k*u - v - b)]
    sol = solve_ivp(f, (0, 40000), [0.1, 0], method="LSODA", max_step=2)
    peaks, _ = find_peaks(sol.y[0], height=0.5)
    return np.mean(np.diff(sol.t[peaks])[2:])


def ring(N, b, Dv, periods, seed):
    # ring of N oscillators, each coupled to its left and right neighbour through v
    T0 = period(b)
    rng = np.random.default_rng(seed)
    u0 = rng.uniform(-0.2, 1.0, N)          # random start
    v0 = rng.uniform(-0.05, 0.25, N)

    def f(t, y):
        u, v = y[:N], y[N:]
        neighbours = (np.roll(v, 1) + np.roll(v, -1)) / 2      # average v of left and right neighbour
        du = u*(1 - u)*(u - alpha) - v
        dv = eps*(k*u - v - b) + Dv*(neighbours - v)
        return np.concatenate([du, dv])

    t = np.linspace(0, periods*T0, 5000)
    sol = solve_ivp(f, (0, t[-1]), np.concatenate([u0, v0]), method="LSODA", t_eval=t, rtol=1e-7, atol=1e-9)
    return sol.t / T0, sol.y[:N]           # time in periods, and u of every node
