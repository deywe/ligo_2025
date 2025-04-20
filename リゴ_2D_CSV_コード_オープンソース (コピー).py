import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

# 🗂️ Diretórios
output_dir = "resultados_amplitude_correta"
os.makedirs(output_dir, exist_ok=True)

# ================================================================
# 📦 STEP 1: LOADING LIGO EXPERIMENTAL DATA
# ================================================================

arquivo_csv = "dados_ligo.csv"
df = pd.read_csv(arquivo_csv, engine='python')
df.columns = df.columns.str.strip().str.lower()

# Captura das colunas reais
time = df["tempo"].values
original_amplitude = df["amplitude_ligo"].values

# ================================================================
# 🌌 STEP 2: GRAVITATIONAL CORRECTION
# ================================================================

G = 6.67430e-11
M_EARTH = 5.972e24
R_EARTH = 6.371e6
M_MOON = 7.348e22
D_EARTH_MOON = 3.844e8
M_SUN = 1.989e30
D_EARTH_SUN = 1.496e11
M_JUPITER = 1.898e27
D_EARTH_JUPITER = 7.785e11

F_earth = G * M_EARTH / R_EARTH**2
F_moon = G * M_MOON / D_EARTH_MOON**2
F_sun = G * M_SUN / D_EARTH_SUN**2
F_jupiter = G * M_JUPITER / D_EARTH_JUPITER**2

correction_factor = 1 + (F_earth + F_moon + F_sun + F_jupiter) / F_earth
corrected_amplitude = original_amplitude / correction_factor

# ================================================================
# 📈 STEP 3: PLOTTING THE COMPARATIVE GRAPH
# ================================================================

plt.figure(figsize=(10, 6))

# Original signal
plt.plot(time, original_amplitude, label="Original LIGO Amplitude", linestyle="--", color="crimson", linewidth=1.8)

# Corrected signal
plt.plot(time, corrected_amplitude, label="Corrected Amplitude (Gravitational)", linestyle="-", color="navy", linewidth=2)

plt.xlabel("Time (s)")
plt.ylabel("Gravitational Wave Amplitude")
plt.title("Comparison: Original vs. Corrected LIGO Amplitude by Gravitational Forces")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)

# Output
plt.tight_layout()
filename = os.path.join(output_dir, "corrigido_ligo_vs_original.png")
plt.savefig(filename, dpi=300)
plt.show()
