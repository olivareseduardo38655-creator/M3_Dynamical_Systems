import matplotlib.pyplot as plt
import seaborn as sns

def set_academic_style():
    """
    Configura Matplotlib con un estilo minimalista inspirado en Yan Holtz.
    Objetivo: Claridad académica, sin 'ruido' visual.
    """
    # Base limpia
    sns.set_theme(style="white", context="talk")
    
    params = {
        # Tipografía profesional
        'font.family': 'sans-serif',
        'font.sans-serif': ['Arial', 'DejaVu Sans'],
        'axes.titlesize': 16,
        'axes.labelsize': 14,
        'legend.fontsize': 12,
        
        # Colores sobrios (Paleta: Carbón, Rojo Académico, Azul Acero, Verde Azulado)
        'axes.prop_cycle': plt.cycler(color=['#333333', '#E63946', '#457B9D', '#2A9D8F']),
        'lines.linewidth': 2.5,
        
        # Eliminación de "Chart Junk" (Principios de Tufte/Holtz)
        'axes.spines.top': False,    # Sin borde superior
        'axes.spines.right': False,  # Sin borde derecho
        'axes.grid': True,           # Grid sutil para referencia
        'grid.alpha': 0.3,
        'grid.linestyle': '--',
    }
    
    plt.rcParams.update(params)

def add_watermark(ax, text="M3: Dynamical Systems"):
    """Firma discreta para proteger/marcar tu trabajo."""
    ax.text(0.99, 0.01, text, transform=ax.transAxes, 
            ha='right', va='bottom', fontsize=9, color='gray', alpha=0.6)
