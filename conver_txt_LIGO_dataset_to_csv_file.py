import os
import numpy as np
import pandas as pd

# ⚙️ Configurações iniciais
np.random.seed(42)  # Para resultados reprodutíveis
Fs = 4096  # Frequência de amostragem usada no LIGO para treinamentos reduzidos
output_file = "dados_ligo.csv"

# 🔎 Localiza primeiro arquivo .txt na pasta atual
txt_files = [f for f in os.listdir() if f.lower().endswith(".txt")]
if not txt_files:
    raise FileNotFoundError("❌ Nenhum arquivo .txt encontrado.")

input_file = txt_files[0]
print(f"🧪 Convertendo arquivo: {input_file}")

# 📥 Leitura dos dados
raw = []
with open(input_file, "r") as f:
    for line in f:
        if line.startswith("#") or not line.strip():
            continue
        parts = line.strip().split()
        try:
            floats = [float(p) for p in parts]
            raw.append(floats)
        except:
            continue

data = np.array(raw)
print(f"✅ Total de linhas válidas: {len(data)}")

# ⚙️ Interpretação como tempo, amplitude (ou apenas amplitude)
if data.shape[1] == 2:
    tempo, amplitude = data[:, 0], data[:, 1]
else:
    amplitude = data[:, 0]
    tempo = np.arange(0, len(amplitude)) / Fs

# 🎲 Geração dos campos adicionais (iguais ao pipeline real)
N = len(tempo)

hist_reparos = np.random.randint(1, 10, size=N)
severidade = np.random.randint(1, 5, size=N)
condicoes = np.random.randint(1, 5, size=N)
impacto = np.random.randint(1, 5, size=N)

# 🔮 Equação preditiva simbiótica HARPIA (replicando a otimização original)
previsao_harpia = (
    (hist_reparos * 0.2) +
    (severidade * 0.4) +
    (condicoes * 0.3) +
    (impacto * 0.5) * np.exp(-tempo / 12)
)

# ✨ Campos simbiotizados SPHY
angulo = 2 * np.pi * tempo
phi1 = np.sin(angulo) * amplitude
phi2 = np.cos(angulo) * amplitude

epsilon = 1e-9
max_amp = np.abs(amplitude).max() + epsilon
coerencia = 1 - (np.abs(phi1 - phi2) / max_amp)

sphy_sem_prev = np.abs(phi1 - phi2) * coerencia
sphy_com_prev = sphy_sem_prev * (1 + previsao_harpia / 10)

# ⬇️ Monta DataFrame
df = pd.DataFrame({
    "tempo": tempo,
    "amplitude_ligo": amplitude,
    "hist_reparos": hist_reparos,
    "severidade": severidade,
    "condicoes": condicoes,
    "impacto": impacto,
    "previsao_harpia": previsao_harpia,
    "sphy_sem_prev": sphy_sem_prev,
    "sphy_com_prev": sphy_com_prev
})

# 💾 Salva CSV
df.to_csv(output_file, index=False)
print(f"✅ Dataset salvo: {output_file}")
