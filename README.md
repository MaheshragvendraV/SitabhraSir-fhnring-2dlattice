Patterns in coupled FitzHugh-Nagumo oscillators
Reproducing some figures from R. Janaki, S. N. Menon, R. Singh, S. Sinha, Lateral inhibition provides a unifying framework for spatiotemporal pattern formation in media comprising relaxation oscillators, Phys. Rev. E 99, 052216 (2019).

Maheshragavendra V, B.Sc. Applied Science (1st year), PSG College of Technology

Model
du/dt = u(1-u)(u-alpha) - v
dv/dt = eps(k u - v - b) + Dv (average v of neighbours - v)
alpha = 0.139, k = 0.6, eps = 0.001. Only v is coupled. Random initial conditions. Time is in units of the period of one uncoupled oscillator.

Files
fhn.py - the model and a ring of N oscillators
patterns.py - ring of 20: synchronised, travelling front, oscillation death and chimera
lattice2d.py - 20 x 20 lattice with 4 neighbours, weak and strong coupling
Run
pip install numpy scipy matplotlib
python patterns.py
python lattice2d.py
Results
Ring: synchronised oscillation, travelling front (GS), oscillation death (SPOD) and a chimera. At b = 0.175, Dv = 0.0018 the same parameters give GS or SPOD depending only on the random start.
2D lattice: at Dv = 0.0007 all nodes keep oscillating; at Dv = 0.0035 all stop, in a checkerboard-like pattern.
