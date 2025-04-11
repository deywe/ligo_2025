import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftfreq

# ================================================================
# 📢 STEP 1: LOADING LIGO DATA
# ================================================================

# Simulated data for testing (REPLACE WITH YOUR ACTUAL FILE!)
# df = pd.read_csv("dados_ligo.csv")   # Uncomment if you have the real file
time = np.linspace(0, 1, 1000)  # Simulated 1 second with 1000 points
amplitude = np.sin(2 * np.pi * 30 * time) + 0.5 * np.sin(2 * np.pi * 80 * time)

# ================================================================
# 📢 STEP 2: APPLYING FOURIER TRANSFORM (FFT)
# ================================================================

# Applying FFT to decompose the time series into frequencies
frequencies = fftfreq(len(time), d=np.mean(np.diff(time)))  # X-axis (frequencies)
fft_amplitude = np.abs(fft(amplitude))  # Absolute value of the spectrum for analysis

# Filtering only positive frequencies (avoiding mirroring)
frequencies = frequencies[:len(frequencies) // 2]
fft_amplitude = fft_amplitude[:len(fft_amplitude) // 2]

# ================================================================
# 📢 STEP 3: PLOTTING THE FOURIER TRANSFORM GRAPH
# ================================================================

plt.figure(figsize=(10, 6))
plt.plot(frequencies, fft_amplitude, color='purple', linewidth=2.5)  # Main graph line
plt.fill_between(frequencies, fft_amplitude, color='purple', alpha=0.3)  # Adding volume below the curve

# Axis configurations and graph title
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude of the Fourier Transform")
plt.title("Fourier Spectrum of Gravitational Waves - LIGO")
plt.grid(True, linestyle="--", alpha=0.6)

# Saving the generated plot
plt.savefig("FFT_LIGO_SPHY.png", dpi=300)

# Display on screen for quick verification
plt.show()

