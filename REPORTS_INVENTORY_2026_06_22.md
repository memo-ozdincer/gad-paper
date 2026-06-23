# Reports & sources inventory (2026-06-22)

Every real report we prepared, its companion MDs, and the actual sources behind
it (tex + build script + figures dir + data). Newest first. All paths relative
to repo root `GAD_plus/`. Data CSVs live in `analysis_2026_04_29/`.

---

## ★ LATEST — the fmax-study report (work off this)

**`BENCHMARK_REPORT_2026-05-16.pdf`** — *GAD vs Sella vs Hybrid GAD–Newton*, HIP, Transition1x **test split n=287**. Has the comprehensive fmax table (9 methods × 6 noise × 5 thresholds) + the fmax-plateau study.

| Component | Path |
|---|---|
| Source (edit this) | `BENCHMARK_REPORT_2026-05-16.tex` |
| Figure generator | `scripts/build_pdf_2026_05_16.py` (+ `scripts/plotting_style.py`) |
| Aggregator (CSVs) | `scripts/integrate_comprehensive_2026_05_16.py` |
| Figures | `figures_2026_05_16/` |
| Data | `analysis_2026_04_29/master_2026_05_11.csv`, `analysis_2026_04_29/threshold_sweep_2026_05_16.csv` |
| Companion MDs | `PAPER_READINESS_2026_05_16.md` (section map), `HYBRID_FINDINGS_CATALOG.md` (receipts), `FINDING_GAD_PLATEAU_INTRINSIC_2026_05_16.md`, `FINDING_HYBRID_REACTANT_2026_05_16.md`, `STATUS_2026_05_16_COMPREHENSIVE.md` |

## Hybrid GAD–Newton reports

| Report PDF | Source tex | Figures | Build | Companion MDs |
|---|---|---|---|---|
| `HYBRID_REPORT_2026-05-11.pdf` | `HYBRID_REPORT_2026-05-11.tex` | `figures_2026_05_11/` + `figures/` | `scripts/build_pdf_2026_05_11.py` | `HYBRID_FINDINGS_CATALOG.md`, `LIVE_STATUS.md` |
| `HYBRID_GAD_NEWTON_2026-05-09.pdf` | `HYBRID_GAD_NEWTON_2026-05-09.tex` | `figures/` | (figures pre-built) | `HYBRID_FINDINGS_CATALOG.md` |
| `HYBRID_GAD_NEWTON_2026-05-04.pdf` | `HYBRID_GAD_NEWTON_2026-05-04.tex` | `figures/` | — | `HYBRID_FINDINGS_CATALOG.md` |

## IRC comprehensive reports (⚠ train-300, older split — see gaps)

| Report PDF | Source tex | Figures | Build |
|---|---|---|---|
| `IRC_COMPREHENSIVE_2026-04-28.pdf` (+ `-28v2`, `-28-reduced`) | `IRC_COMPREHENSIVE_2026-04-28*.tex` | `figures/` | `scripts/figures_2026_04_28.py`, `figures_2026_04_28v2.py` |
| `IRC_COMPREHENSIVE_2026-04-20.pdf` | `IRC_COMPREHENSIVE_2026-04-20.tex` | `figures/` | `scripts/figures_master_2026_04_20.py`, `scripts/analyze_full_2026_04_20.py` |
| `IRC_COMPREHENSIVE_2026-04-17.pdf` | `IRC_COMPREHENSIVE_2026-04-17.tex` | `figures/` | `scripts/figures_comprehensive.py` |
| `IRC_TEST_2026-04-29.pdf` | `IRC_TEST_2026-04-29.tex` | `figures/` | `scripts/figures_test_2026_04_29.py` |
| `IRC_RESULTS_2026-04-15.pdf`, `-16.pdf` | matching `.tex` | `figures/` | `scripts/figures_sella_*.py`, `figures_irc_bars.py` |

## Original

`EXPERIMENTS.pdf` ← `EXPERIMENTS.tex` — the first full writeup.

## Supporting MDs (not tied to one report)
`DATA_REFERENCE.md`, `IRC_OVERVIEW.md`, `HANDOFF_IRC.md`, `EXPERIMENT_LOG.md`,
`PAPER_INSIGHTS.md`, `LIVE_STATUS.md`, `BACKBURNER.md`, `CLAUDE.md`.

---

## Gaps others may find

1. **`LITERATURE_REVIEW_AND_SYNTHESIS.tex` (3338 lines, 147 KB) has NO compiled PDF.** A large related-work/synthesis draft never built. High-value for the paper's intro/related-work — compile it (`pdflatex`) and review; it likely needs a figures pass.
2. **`references/noisyTS.tex`** — the LMHE comparison paper source (Fig-3, 0–15 pm positioning). Related-work anchor; not yet folded into any report.
3. **Split mismatch across reports.** The latest (05-16) is **test-287**; the 04-xx IRC_COMPREHENSIVE reports are **train-300**. Don't mix cells across the two — cite numbers only from 05-16 for the paper.
4. **No single compiled "paper".** These are *reports*; the manuscript (abstract/intro/methods prose/discussion) is unwritten. `PAPER_READINESS_2026_05_16.md` has the section map.
5. **Headline prose understates the result.** 05-16 TeX TL;DR says GAD wins IRC TOPO at high noise but underplays that GAD **also** wins raw TS-conv there (+17.4 pp @ 200 pm). Crossover table is in `gad-paper/README.md` / `PAPER_PACKAGE_2026_06_22.md`.
6. **Orphan source line.** 05-16 §Sources still lists `runs/starting_geom_300/` (train-300, removed section) — scrub.
7. **SCINE dropped** from the paper (high conv but IRC/TOPO ~0 above 10 pm). Latest SCINE writeup `SCINE_XTB_FINDINGS_2026_05_15.md` is MD-only, never compiled — leave as-is unless revisited.
8. **Coordinate step resolved**, not a gap: Cartesian step + MW Eckart projection is canonical (`projection.py` `61119c2`); ≤0.35 pp effect on test-287, reported numbers stand. Full A/B: `FINDING_CART_VS_MW_STEP_2026_06_10.md`.

> A pre-extracted minimal writing-only copy of the latest report also exists at
> `gad-paper/` (compiles standalone) — use it or ignore it; the canonical sources
> are the ones listed above.
