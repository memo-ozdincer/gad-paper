#!/usr/bin/env python3
"""Two figures missing from the committed suite, in the repo's Dark2 style
(matches scripts/build_figures_new.py): fig_reactant_scope, fig_rmsd_vs_noise."""
import os, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np, pandas as pd
_HERE = os.path.dirname(os.path.abspath(__file__))
_CANDS = [os.path.join(_HERE, "..", "analysis_2026_04_29"),                                  # repo-relative (scripts/..)
          "/sessions/determined-blissful-hamilton/mnt/new/gad-paper/analysis_2026_04_29",   # sandbox fallback
          "/tmp/gad/analysis_2026_04_29"]
CSV = next((c for c in _CANDS if os.path.exists(os.path.join(c, "reactant_0pm_2026_05_16.csv"))), _CANDS[0])
OUT = os.environ.get("FIG_OUT", os.path.join(_HERE, "..", "figures_new"))  # repo: <root>/figures_new
os.makedirs(OUT, exist_ok=True)
C = {"GAD": "#1b9e77", "Hybrid": "#7570b3", "Sella": "#d95f02"}
plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False,
                     "figure.dpi": 140, "savefig.bbox": "tight", "axes.grid": True,
                     "grid.alpha": 0.25, "legend.frameon": False})
NO = [10, 30, 50, 100, 150, 200]
def save(fig, n): fig.savefig(f"{OUT}/{n}.pdf"); fig.savefig(f"{OUT}/{n}.png", dpi=130); plt.close(fig)

# ---- fig_reactant_scope ----
rc = pd.read_csv(f"{CSV}/reactant_0pm_2026_05_16.csv")
items = [("Sella cartesian Eckart untuned Hess.Freq.=1", "Sella", C["Sella"]),
         ("GAD dt=0.005", "GAD", C["GAD"]),
         ("Hybrid damped Eckart eig tr=0.05", "Hybrid", C["Hybrid"])]
labs, vals, cols, ns = [], [], [], []
for cfg, disp, col in items:
    r = rc[rc.config == cfg]
    if len(r):
        labs.append(disp); vals.append(float(r.fmax_010.values[0])); cols.append(col); ns.append(int(r.n.values[0]))
fig, ax = plt.subplots(figsize=(5.6, 4.3))
b = ax.bar(labs, vals, color=cols, width=0.62)
for rect, v, nn in zip(b, vals, ns):
    ax.text(rect.get_x()+rect.get_width()/2, v+1.5, f"{v:.0f}%\n(n={nn})", ha="center", fontsize=10, fontweight="bold")
ax.set(ylabel="convergence from reactant start (%)", ylim=(0, 100),
       title="Scope boundary: from a reactant start\nthe GAD family is weak; Sella wins")
save(fig, "fig_reactant_scope")

# ---- fig_rmsd_vs_noise ----
rm = pd.read_csv(f"{CSV}/rmsd_to_known_ts_compare.csv")
RMAP = {"GAD": "plain GAD dt=0.005", "Sella": "Sella libdef", "Hybrid": "hybrid Eckart damped tr=0.05"}
fig, ax = plt.subplots(1, 2, figsize=(11, 4.3), sharex=True)
for k, fam in RMAP.items():
    d = rm[rm.family == fam].set_index("noise_pm").reindex(NO)
    ax[0].plot(NO, d.rmsd_med, "-o", color=C[k], lw=2.2, ms=6, label=k)
    ax[1].plot(NO, d.rmsd_p95, "-o", color=C[k], lw=2.2, ms=6, label=k)
ax[0].set(title="(a) median RMSD to true TS", ylabel="RMSD (Å)", xlabel="noise (pm)")
ax[1].set(title="(b) 95th-percentile RMSD", ylabel="RMSD (Å)", xlabel="noise (pm)")
ax[0].legend()
save(fig, "fig_rmsd_vs_noise")

# ---- fig_saddle_convergence (secondary metric: n_neg=1 & fmax<0.01 vs noise) ----
CONV = {"GAD":    [89.2, 88.5, 85.4, 71.1, 55.1, 40.8],   # dt=0.003 (matches IRC config)
        "Sella":  [92.7, 92.0, 88.2, 70.7, 54.0, 27.2],   # cart+Eckart untuned d=1
        "Hybrid": [85.4, 85.0, 81.5, 66.9, 50.9, 33.1]}   # damped Eckart tr=0.05
fig, ax = plt.subplots(figsize=(5.8, 4.4))
for k in ["GAD", "Sella", "Hybrid"]:
    ax.plot(NO, CONV[k], "-o", color=C[k], lw=2.2, ms=6, label=k)
ax.set(xlabel="initial-guess noise (pm)",
       ylabel=r"saddle-convergence rate (%)",
       title=r"Secondary metric: $n_{neg}{=}1 \wedge F_{max}{<}0.01$",
       ylim=(0, 100))
ax.legend()
save(fig, "fig_saddle_convergence")
print("wrote fig_reactant_scope, fig_rmsd_vs_noise, fig_saddle_convergence to", OUT)
