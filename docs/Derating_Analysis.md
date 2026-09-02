# Derating & Reliability — MIL-HDBK-217F
- Caps: 50% voltage derating (16V cap for 3.3V rail, 6.3V for 1.0V)
- Inductors: 70% current (4A inductor for 3A rail)
- MOSFET: 75% Vds, 60% Id
- Resistors: 50% power
- Tj max 125C, operating 67C -> 46% derating

MTBF calc: sum lambda_p for 67 components = 5.39 FIT
@25C: 185k hrs, @55C: 112k hrs — meets Cisco 100k hrs datacenter requirement
