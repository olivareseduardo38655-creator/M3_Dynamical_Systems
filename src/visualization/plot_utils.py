import matplotlib.pyplot as plt
import numpy as np
from typing import Optional
from src.visualization.plot_styles import add_watermark

def plot_trajectory(data: np.ndarray, r: float, title: Optional[str] = None) -> None:
    """
    Genera una visualizacion limpia de la evolucion temporal del sistema.
    
    Args:
        data (np.ndarray): Array con los valores de la serie de tiempo.
        r (float): Parametro de control utilizado.
        title (str, optional): Titulo personalizado para la grafica.
    """
    iterations = np.arange(len(data))
    
    plt.figure(figsize=(12, 6))
    
    # Graficamos la serie de tiempo con linea fina y marcadores discretos
    plt.plot(iterations, data, 'o-', markersize=4, linewidth=1, alpha=0.8, color='#404040')
    
    # Linea de referencia en el ultimo valor para visualizar convergencia
    last_val = data[-1]
    plt.axhline(y=last_val, color='#E63946', linestyle=':', alpha=0.5, label=f'Final state: {last_val:.4f}')
    
    # Configuracion de etiquetas
    final_title = title if title else f"System Evolution (Growth Rate r = {r})"
    plt.title(final_title)
    plt.xlabel("Time (Generations)")
    plt.ylabel("Population Ratio (x)")
    
    plt.legend(loc='upper right', frameon=True)
    plt.tight_layout()
    
    # Agregamos la firma del proyecto
    add_watermark(plt.gca())
    
    plt.show()
