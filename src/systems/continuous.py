import numpy as np
from scipy.integrate import odeint

class LorenzSystem:
    """
    Implementación del Atractor de Lorenz.
    Un sistema de ecuaciones diferenciales ordinarias que modela convección atmosférica.
    Conocido por su forma de 'mariposa' y comportamiento caótico.
    """

    def __init__(self, sigma: float = 10.0, rho: float = 28.0, beta: float = 8.0/3.0):
        """
        Inicializa los parámetros del sistema.
        
        Args:
            sigma (float): Número de Prandtl (viscosidad/difusividad térmica).
            rho (float): Número de Rayleigh (diferencia de temperatura). El caos aparece si rho > 24.74.
            beta (float): Factor geométrico del modelo.
        """
        self.sigma = sigma
        self.rho = rho
        self.beta = beta

    def _derivatives(self, state: list, t: float) -> list:
        """
        Calcula las derivadas parciales (dx/dt, dy/dt, dz/dt).
        Método interno utilizado por el solver.
        """
        x, y, z = state
        
        dx_dt = self.sigma * (y - x)
        dy_dt = x * (self.rho - z) - y
        dz_dt = x * y - self.beta * z
        
        return [dx_dt, dy_dt, dz_dt]

    def simulate(self, x0: float, y0: float, z0: float, duration: float, dt: float = 0.01) -> np.ndarray:
        """
        Resuelve el sistema de ecuaciones diferenciales en el tiempo.
        
        Args:
            x0, y0, z0 (float): Condiciones iniciales espaciales.
            duration (float): Tiempo total de simulación.
            dt (float): Paso de tiempo (delta t).
            
        Returns:
            np.ndarray: Array de forma (n_steps, 3) con las coordenadas x, y, z.
        """
        t = np.arange(0, duration, dt)
        initial_state = [x0, y0, z0]
        
        # odeint es el estándar industrial para integración numérica en Python
        trajectory = odeint(self._derivatives, initial_state, t)
        
        return trajectory
