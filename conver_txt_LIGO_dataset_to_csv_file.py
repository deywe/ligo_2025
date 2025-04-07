import os
import numpy as np
import pandas as pd

# ================================================================
# 🔍 Step 1: Search for .txt file in current folder
# ================================================================

# Automatically find the first .txt file in the current directory
txt_files = [f for f in os.listdir() if f.lower().endswith(".txt")]

if not txt_files:
    raise FileNotFoundError("❌ No .txt file found in this folder.")
    
input_file = txt_files[0]
print(f"📁 Loading input file: {input_file}")

# ================================================================
# 📥 Step 2: Read LIGO strain data from ASCII .txt (1 column)
# ================================================================

with open(input_file, "r") as file:
    lines = file.readlines()

# ✅ Filter out header lines starting with '#' and convert to float
strain_data = np.array([float(line.strip()) for line in lines if not line.startswith("#")])

# ================================================================
# ⏱ Step 3: Build time series (assuming 16384 Hz sample rate)
# ================================================================

Fs = 16384  # LIGO's standard sampling rate in Hz
time = np.arange(0, len(strain_data)) / Fs

# ================================================================
# 🧾 Step 4: Export to DataFrame (and optionally add extra cols)
# ================================================================

df = pd.DataFrame({
    "tempo": time,
    "amplitude_ligo": strain_data,
    "hist_reparos": np.random.randint(1, 10, size=len(time)),
    "severidade": np.random.randint(1, 3, size=len(time)),
    "condicoes": np.random.randint(1, 3, size=len(time)),
    "impacto": np.random.randint(1, 5, size=len(time)),
})

# Optional prediction logic (used in Harpia-based pipelines)
df["previsao_harpia"] = df["hist_reparos"] * 0.5 + df["impacto"] * 0.8
df["sphy_sem_prev"] = np.exp(- df["tempo"] * 0.1)
df["sphy_com_prev"] = df["sphy_sem_prev"] * 1.2

# ================================================================
# 💾 Step 5: Save to CSV
# ================================================================
output_file = "dados_ligo.csv"
df.to_csv(output_file, index=False)
print(f"✅ File saved successfully as: {output_file}")
