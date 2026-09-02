# pdn-thermal-lab — Power Delivery & Thermal Lab

<p align="center">

[![Live Demo](https://img.shields.io/badge/Live%20Demo-GitHub%20Pages-0ea5e9?style=flat-square)](https://aditya0si.github.io/pdn-thermal-lab/)
  <img src="https://img.shields.io/badge/efficiency-94.2%25%20peak-success?style=flat-square" />
  <img src="https://img.shields.io/badge/system-88.4%25-blue?style=flat-square" />
  <img src="https://img.shields.io/badge/MTBF-185k%20hrs-purple?style=flat-square" />
  <img src="https://img.shields.io/badge/Tj-67%C2%B0C%20%40%2025%C2%B0C-orange?style=flat-square" />
  <img src="https://img.shields.io/badge/PM-62%C2%B0-informational?style=flat-square" />
</p>

<p align="center"><i>Power that stays flat under load and stays cool in a 1U box.</i></p>

### Rails (12V → 3.3V 2A → 1.8V 1.5A → 1.0V 3A ASIC core)
Buck: TPS54360 (3.3V), TLV62569 (1.8V), TPS54821 (1.0V) — all dual-sourced LCSC Basic.

| Rail | Eff | Ripple | Load step | Phase margin |
|------|-----|--------|-----------|--------------|
| 12→3.3V 580kHz | 92.8% @1.5A | 18mV | 42mV/5A/µs | 62° |
| 3.3→1.8V 1MHz | 91.2% | 12mV | 28mV | — |
| 3.3→1.0V 800kHz | **94.2% peak @2.5A** | 15mV | 35mV | 62° |
| **System** | **88.4%** | — | — | — |

Thermal: 2oz copper + 12 thermal vias/IC → θJA 28°C/W → Tj 67°C @25°C. With 3W/mK TIM + heatsink 6°C/W → Tj 52°C (-15°C). Fits 55°C datacenter ambient with 43°C margin.

Reliability: MIL-HDBK-217F, 50% V / 70% I derating, FIT 5.39, **MTBF 185k hrs @25°C / 112k hrs @55°C**, 7.2 yrs @45°C.

### Interactive Lab
→ **`viewer.html`** — efficiency vs load (drag current → eff), thermal slider (ambient → Tj), and MTBF explorer. All JS, no backend.

→ **`sim/buck_3v3.asc` / `buck_1v0.asc`** — LTspice: run transient + `.meas` ripple/eff, Bode for PM.

### Trade that matters
Swapped 1.0V from LDO (68% eff) to buck → +26% system eff, -4.2W heat. 2.2µH vs 3.3µH: chose 2.2µH for transient, not peak eff.

### Files
`sim/` — LTspice bucks, efficiency_sweep.py, Bode  
`docs/` — FMEA.md (RPN <100, 8D), Derating_Analysis.md

---
*Feeds pcb-dfm-dft and si-pi-lab — same PDN, same thermal constraints.*
