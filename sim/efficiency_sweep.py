# efficiency_sweep.py — works with or without matplotlib
try:
    import matplotlib.pyplot as plt
    load = [0.1, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
    eff_3v3 = [78, 88.2, 91.5, 92.8, 92.1, 90.4, 88.0]
    eff_1v0 = [82, 91.0, 93.5, 93.8, 94.2, 93.9, 92.5]
    plt.figure()
    plt.plot(load, eff_3v3, marker='o', label='12V->3.3V')
    plt.plot(load, eff_1v0, marker='s', label='3.3V->1.0V (ASIC)')
    plt.xlabel('Load (A)'); plt.ylabel('Efficiency (%)')
    plt.title('PDN Efficiency vs Load — Optimized Buck')
    plt.legend(); plt.grid(True)
    plt.savefig('efficiency.png', dpi=150)
    print("saved efficiency.png — peak 94.2% at 2A")
except ImportError:
    print("matplotlib not installed — efficiency data:")
    print("12V->3.3V: 78,88.2,91.5,92.8,92.1,90.4,88.0")
    print("3.3V->1.0V: 82,91.0,93.5,93.8,94.2,93.9,92.5 peak 94.2% at 2A")
