import numpy as np

class ChaosGame:
    """
    Implementación del 'Juego del Caos' para generar fractales geométricos.
    Demuestra cómo reglas estocásticas simples pueden generar estructuras altamente ordenadas
    como el Triángulo de Sierpinski.
    """

    def __init__(self, vertices: np.ndarray = None):
        """
        Inicializa el juego con los vértices "atractores".
        Si no se proveen, usa un triángulo equilátero estándar.
        
        Args:
            vertices (np.ndarray, optional): Matriz de (N, 2) con las coordenadas de los vértices.
        """
        if vertices is None:
            # Triángulo equilátero por defecto
            self.vertices = np.array([
                [0.0, 0.0],
                [1.0, 0.0],
                [0.5, np.sqrt(3)/2]
            ])
        else:
            self.vertices = vertices
            
        self.n_vertices = self.vertices.shape[0]

    def generate_points(self, n_steps: int, compression_factor: float = 0.5) -> np.ndarray:
        """
        Ejecuta la simulación del juego del caos.
        
        Args:
            n_steps (int): Número total de puntos a generar.
            compression_factor (float): Qué tanto nos acercamos al vértice elegido (0.5 = mitad de camino).
            
        Returns:
            np.ndarray: Matriz de (n_steps, 2) con las coordenadas X, Y de los puntos generados.
        """
        # Pre-localizamos memoria para velocidad (Optimization Senior)
        points = np.zeros((n_steps, 2))
        
        # Punto inicial aleatorio dentro del área aproximada
        current_point = np.random.rand(2)
        
        # Elegimos aleatoriamente qué vértice usaremos en cada paso por adelantado
        random_vertices_indices = np.random.randint(0, self.n_vertices, size=n_steps)
        
        # Iteración principal (El núcleo del juego)
        for i in range(n_steps):
            # 1. Elegir el vértice objetivo basado en el índice aleatorio
            target_vertex = self.vertices[random_vertices_indices[i]]
            
            # 2. Moverse una fracción del camino hacia ese vértice
            # Nueva posición = Actual + (Vector dirección * factor)
            current_point = current_point + (target_vertex - current_point) * compression_factor
            
            # 3. Guardar el punto
            points[i] = current_point
            
        # Descartamos los primeros puntos (transitorio) para limpiar la imagen
        cutoff = int(n_steps * 0.01) # Descartar el primer 1%
        return points[cutoff:]
