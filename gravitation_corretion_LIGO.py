# NOTE: This example uses simulated data and a simplified correction model for illustrative purposes only.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ================================================================
# 📢 STEP 1: LOADING LIGO EXPERIMENTAL DATA
# ================================================================

# Simulated data for demonstration (REPLACE WITH ACTUAL FILE IF AVAILABLE!)
# df = pd.read_csv("dados_ligo.csv")  # 🔹 Uncomment this line if you have the real CSV
time = np.linspace(0, 1, 1000)  # Simulated 1 second with 1000 samples
original_amplitude = np.sin(2 * np.pi * 30 * time) + 0.3 * np.sin(2 * np.pi * 90 * time)

# ================================================================
# 📢 STEP 2: GRAVITATIONAL CORRECTION (INFLUENCE OF EARTH, MOON, SUN, AND JUPITER)
# ================================================================

# 🔹 Gravitational constants
G = 6.67430e-11  # Gravitational constant (m³/kg/s²)
M_EARTH = 5.972e24  # Mass of Earth (kg)
R_EARTH = 6.371e6  # Radius of Earth (m)
M_MOON = 7.348e22  # Mass of Moon (kg)
D_EARTH_MOON = 3.844e8  # Distance Earth-Moon (m)
M_SUN = 1.989e30  # Mass of Sun (kg)
D_EARTH_SUN = 1.496e11  # Distance Earth-Sun (m)
M_JUPITER = 1.898e27  # Mass of Jupiter (kg)
D_EARTH_JUPITER = 7.785e11  # Distance Earth-Jupiter (m)

# 🔹 Calculation of concurrent gravitational forces using Newton's Universal Law of Gravitation
F_earth = G * M_EARTH / R_EARTH**2
F_moon = G * M_MOON / D_EARTH_MOON**2
F_sun = G * M_SUN / D_EARTH_SUN**2
F_jupiter = G * M_JUPITER / D_EARTH_JUPITER**2

# 🔹 Applying gravitational correction to the wave amplitude
correction_factor = 1 + (F_earth + F_moon + F_sun + F_jupiter) / F_earth
corrected_amplitude = original_amplitude / correction_factor

# ================================================================
# 📢 STEP 3: PLOTTING THE SIGNAL COMPARISON GRAPH
# ================================================================

plt.figure(figsize=(10, 6))

# 🔹 Plotting the original amplitude of gravitational waves
plt.plot(time, original_amplitude, label="Original Amplitude (LIGO)", color="red", linestyle="--", linewidth=2)

# 🔹 Plotting the corrected version of the amplitude
plt.plot(time, corrected_amplitude, label="Corrected Amplitude (After Gravitational Correction)", color="blue", linewidth=2)

# 🔧 Adjusting axes, title, and legend
plt.xlabel("Time (s)")
plt.ylabel("Gravitational Wave Amplitude")
plt.title("Grav. Influence Correction on Waves Detected by LIGO")
plt.legend(loc="upper right")
plt.grid(True, linestyle="--", alpha=0.6)

# 📁 Saving the generated graph
plt.savefig("Gravitational_Correction_LIGO.png", dpi=300)

# 📡 Display the graph on the screen
plt.show()

