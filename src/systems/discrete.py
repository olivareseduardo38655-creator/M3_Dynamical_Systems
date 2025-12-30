import numpy as np

class LogisticMap:
    """
    Modelo del Mapa Logístico: x_{n+1} = r * x_n * (1 - x_n)
    Un ejemplo clásico de cómo la no linealidad simple genera caos complejo.
    """
    
    def __init__(self, r: float):
        """
        Args:
            r (float): Tasa de crecimiento. 
                       r < 3 (Estable), 3 < r < 3.56 (Oscilatorio), r > 3.57 (Caos).
        """
        self.r = r

    def simulate(self, x0: float, steps: int) -> np.ndarray:
        """
        Simula la evolución temporal del sistema para una sola trayectoria.
        
        Args:
            x0 (float): Población inicial (0 a 1).
            steps (int): Número de generaciones.
            
        Returns:
            np.ndarray: Array con la historia de la población.
        """
        trajectory = np.zeros(steps)
        trajectory[0] = x0
        
        for t in range(1, steps):
            prev_x = trajectory[t-1]
            trajectory[t] = self.r * prev_x * (1 - prev_x)
            
        return trajectory

    @staticmethod
    def generate_bifurcation_data(min_r: float, max_r: float, steps: int, last_n: int, resolution: int) -> tuple[np.ndarray, np.ndarray]:
        """
        Genera los datos masivos para el diagrama de bifurcación.
        Utiliza vectorización de NumPy para alto rendimiento (Senior Optimization).
        
        Args:
            min_r (float): Valor mínimo de r.
            max_r (float): Valor máximo de r.
            steps (int): Total de iteraciones por cada r.
            last_n (int): Cuántas iteraciones finales guardamos (para ver los atractores).
            resolution (int): Cuántos puntos de r vamos a simular (densidad del eje X).
            
        Returns:
            tuple: (valores_r, valores_x) listos para graficar.
        """
        # Creamos un array con todos los valores de r a probar simultáneamente
        r_values = np.linspace(min_r, max_r, resolution)
        
        # Estado inicial aleatorio para todos los r (vectorizado)
        x = np.random.rand(resolution)
        
        # Iteramos para estabilizar el sistema (transitorio)
        # No guardamos estos datos, solo dejamos que el sistema evolucione
        transient_steps = steps - last_n
        for _ in range(transient_steps):
            x = r_values * x * (1 - x)
            
        # Ahora guardamos los últimos 'last_n' estados para la gráfica
        r_points = []
        x_points = []
        
        for _ in range(last_n):
            x = r_values * x * (1 - x)
            # Guardamos los pares (r, x)
            r_points.append(r_values)
            x_points.append(x)
            
        # Aplanamos los arrays para facilitar el plot (format scatter)
        return np.array(r_points).flatten(), np.array(x_points).flatten()
