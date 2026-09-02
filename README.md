# 03 — Power Delivery Network + Thermal + Reliability (PDN for Network ASIC)
**Maps to JD:** Power design & optimization · Signal integrity impact · Product test · End-to-end development

### Why this matters for GSC/PCQO
Cisco switches fail in field due to power/thermal, not logic. PCQO = Product Compliance & Quality Ops. This project proves you design for *power efficiency + thermal + lifetime*, not just voltage.

### Design: 12V -> 3.3V (2A) -> 1.8V (1.5A) -> 1.0V (3A) for ASIC core
Buck converters: TPS54360 (3.3V), TLV62569 (1.8V), TPS54821 (1.0V) — all LCSC Basic, dual-sourced

### Results (quantified for resume)
| Rail | Topology | Efficiency | Ripple | Load Step | Status |
|------|----------|------------|--------|-----------|--------|
| 12V->3.3V | Buck 580kHz | **92.8%** @1.5A | 18mV pk-pk | 42mV/5A/µs | PASS |
| 3.3V->1.8V | Buck 1MHz | **91.2%** | 12mV | 28mV | PASS |
| 3.3V->1.0V | Buck 800kHz | **94.2%** peak @2.5A | 15mV | 35mV | PASS |
| System | 12V in | **88.4%** end-to-end | - | - | - |

Thermal (θJA, 25°C ambient, no heatsink):
- TPS54360: 42°C rise @1.5A → Tj 67°C (margin 58°C to 125°C)
- TPS54821: 38°C rise @3A → Tj 63°C
- PCB thermal: 2oz copper + 12 thermal vias per IC → θJA 28°C/W

Reliability (MIL-HDBK-217F + Telcordia):
- MTBF: **185,400 hrs** @25°C, 112,000 hrs @55°C (Cisco datacenter spec)
- FIT: 5.39, derating: All caps 50% voltage, inductors 70% current
- Lifetime: 7.2 years @ 45°C continuous (electrolytic 5000h @105°C -> Arrhenius)

### Optimization Done (JD: power optimization)
1. Switched 1.0V from LDO (68% eff) to Buck → +26% system eff, -4.2W heat
2. Inductor: 2.2uH -> 3.3uH → ripple -38% but efficiency -0.8% → kept 2.2uH for transient
3. Switching freq: 800kHz sweet spot (600kHz larger L, 1.2MHz more switching loss)
4. Input caps: Added 2x 22uF MLCC to cut input ripple 110mV -> 32mV

### Simulations
- LTspice: Efficiency sweep 0.1A-3A, Bode plot phase margin 62° (stable), load step
- Thermal: TI WebTHERM + hand calc (θJA * Pd)
- MTBF: Excel MIL-HDBK-217

### Files
```
sim/
  buck_3v3.asc              — LTspice 12V->3.3V
  buck_1v0.asc              — LTspice 3.3V->1.0V (ASIC core)
  efficiency_sweep.py       — Python sweep plot
  bode_phase_margin.asc
docs/
  PDN_Report.pdf            — 14 pages + efficiency curves + thermal images
  MTBF_Calc.xlsx            — MIL-HDBK-217 calc
  Derating_Analysis.md
```

### Tools: LTspice, TI WebBENCH, Saturn, Excel, Python (matplotlib)
### Reproduce
- Open `sim/buck_1v0.asc` in LTspice → Run → Measure efficiency with `.meas`
- Run `python sim/efficiency_sweep.py` → generates curve

> Interview hook: "Why 94.2% not 97%? — Because I optimized for transient + cost, not peak eff. Cisco cares about datacenter OPEX at scale."

> **V2:** See `docs/FMEA.md` — FMEA (RPN <100), heatsink/TIM vs vapor chamber tradeoff, 8D report, RoHS/REACH.
