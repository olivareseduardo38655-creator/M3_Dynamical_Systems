# M3: Dynamical Systems & Chaos Analysis Framework

![Python](https://img.shields.io/badge/Python-3.10-3776AB?style=flat&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-Scientific_Viz-3F4F75?style=flat&logo=plotly&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-Vectorized_Computing-013243?style=flat&logo=numpy&logoColor=white)
![Status](https://img.shields.io/badge/Status-Production_Ready-success?style=flat)

## Descripción Ejecutiva

Este proyecto implementa un marco computacional avanzado para el análisis de **Sistemas Dinámicos No Lineales**. Su propósito principal es cuantificar los límites de la predictibilidad en entornos complejos (similares a mercados financieros o cadenas de suministro) mediante la simulación numérica de modelos de caos determinista.

El sistema transforma abstracciones matemáticas (Mapa Logístico, Atractor de Lorenz y Geometría Fractal) en herramientas de inteligencia de negocios, permitiendo a los tomadores de decisiones visualizar la transición del orden al caos y comprender los riesgos inherentes a las proyecciones de largo plazo debido a la sensibilidad a las condiciones iniciales (Efecto Mariposa).

## Objetivos Técnicos

1.  **Arquitectura Modular (Clean Code):** Implementación de patrones de diseño de software desacoplados, separando la lógica matemática (`src/systems`), la visualización y la interfaz de usuario.
2.  **Computación Numérica de Alto Rendimiento:** Utilización de vectorización con NumPy para la simulación masiva de trayectorias (Diagramas de Bifurcación con >100,000 puntos) y resolución de ecuaciones diferenciales con SciPy.
3.  **Visualización Interactiva 3D:** Desarrollo de dashboards dinámicos para la exploración del espacio de fase en sistemas continuos y discretos.
4.  **Simulación Estocástica:** Generación de estructuras fractales auto-similares mediante procesos aleatorios iterativos (Juego del Caos).

## Arquitectura del Sistema

El flujo de datos sigue una estructura lineal desde la parametrización del usuario hasta la renderización gráfica, asegurando la integridad de los cálculos numéricos.

```mermaid
graph LR
    User["Usuario / Stakeholder"] -->|Input Params| UI["Streamlit Dashboard"]
    UI -->|Request| Logic["Logic Core (src)"]

    subgraph "Logic Core"
        Logic --> Discrete["Discrete Systems Engine"]
        Logic --> Continuous["ODE Solver Engine"]
        Logic --> Stochastic["Stochastic Engine"]
    end

    Discrete -->|Vectorized Calc| NumPy["NumPy / SciPy"]
    Continuous -->|Integration| NumPy
    Stochastic -->|Iteration| NumPy

    NumPy -->|Data Arrays| Viz["Plotly Visualization Layer"]
    Viz -->|Render| UI
