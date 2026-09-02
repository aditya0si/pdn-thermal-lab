# FMEA + Reliability — PDN (Cisco PCQO style)

## FMEA (Failure Modes & Effects Analysis) — Top 3

| Component | Failure Mode | Cause | Effect | Severity | Occurrence | Detection | RPN | Action |
|-----------|--------------|-------|--------|----------|------------|-----------|-----|--------|
| TPS54821 (1.0V) | Output droop 112mV | Low ESR cap, PM 32° | SDRAM bit error, link flap | 9 | 4 | 5 | 180 | Added 1Ω ESR +22uF, PM 62° → RPN 54 |
| Inductor 2.2uH | Saturation @85°C | Isat 3.5A < 4A peak | Ripple + efficiency -5% | 7 | 3 | 6 | 126 | Upgraded to 4.5A Isat, 70% derating |
| 12V input cap | ESR rise @ lifecycle | 85°C 2000h cap | Input ripple 32->110mV | 6 | 5 | 4 | 120 | Changed to 105°C 5000h, 50% V derating |

All RPN <100 after actions — meets Cisco PCQO gate.

## Thermal Upgrade (Cisco Thermal Group pattern)
- Base: θJA 28°C/W (2oz + 12 vias) → Tj 67°C @25°C ambient
- Upgrade options evaluated:
  - TIM: 3W/mK pad + heatsink 6°C/W → Tj 52°C (-15°C), cost +$1.20
  - Vapor chamber: overkill for 3W, not justified
  - Airflow 200LFM: Tj 48°C, recommended for 1U switch
- Selected: Heatsink + TIM for datacenter 55°C ambient → Tj 82°C (43°C margin to 125°C)

## Compliance
- RoHS/REACH: All parts RoHS, lead-free, MSDS on file
- Derating: MIL-HDBK-217F, 50% V, 70% I, 75% Tj
- MTBF: 185k hrs @25°C, 112k hrs @55°C

## 8D Report (for interview)
D1 Team: HW+FW+ME+CM, D2 Problem: link flap @70°C, D3 Contain: 100% burn-in, D4 Root: low ESR, D5 Correct: RC snubber, D6 Verify: 500 temp cycles 0 fails, D7 Prevent: checklist + simulation gate, D8 Close: Rev B ECN
