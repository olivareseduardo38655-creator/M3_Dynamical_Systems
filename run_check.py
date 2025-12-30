from src.systems.discrete import LogisticMap
from src.visualization.plot_styles import set_academic_style, add_watermark
import matplotlib.pyplot as plt

# 1. Activamos el estilo Yan Holtz
set_academic_style()

# 2. Simulamos el caos (r=3.9 es caos puro)
model = LogisticMap(r=3.9)
data = model.simulate(x0=0.1, steps=100)

# 3. Visualizamos
plt.figure(figsize=(10, 6))
plt.plot(data, '-', label=f'Crecimiento r={model.r}')
plt.title("Caos Determinista: Mapa Logístico")
plt.xlabel("Tiempo (Generaciones)")
plt.ylabel("Población Relativa")
add_watermark(plt.gca()) # Nuestra firma
plt.legend()
plt.tight_layout()

print("✅ Sistema listo. Generando gráfico...")
plt.show()
