import streamlit as st
import plotly.graph_objects as go
import numpy as np
import sys
import os

# Agregamos el directorio raiz para importar nuestros modulos de logica
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importamos TODOS nuestros sistemas
from src.systems.discrete import LogisticMap
from src.systems.continuous import LorenzSystem
from src.systems.fractals import ChaosGame

# -----------------------------------------------------------------------------
# CONFIGURACIÓN DE PÁGINA Y CSS
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="M3: Dynamical Systems Analysis",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    /* Tipografia General - Forzando Serif elegante */
    body, .stMarkdown, p, li {
        font-family: 'Georgia', 'Garamond', serif !important;
        font-size: 18px;
        color: #111111;
        text-align: justify;
    }
    h1, h2, h3 {
        font-family: 'Arial', sans-serif;
        color: #2c3e50;
    }
    /* Cajas de texto */
    .observation-box {
        background-color: #ffffff;
        border-left: 4px solid #457B9D;
        padding: 20px;
        margin: 20px 0;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
        border-radius: 5px;
    }
    .prescription-box {
        background-color: #f1f8e9;
        border-left: 4px solid #2e7d32;
        padding: 20px;
        margin: 20px 0;
        border-radius: 5px;
    }
    /* Tablas */
    .logic-table {
        width: 100%;
        border-collapse: collapse;
        margin: 25px 0;
        font-family: 'Georgia', serif;
        font-size: 16px;
        text-align: left;
    }
    .logic-table th, .logic-table td {
        padding: 12px 15px;
        border: 1px solid #ddd;
    }
    .logic-table th {
        background-color: #f8f9fa;
        font-weight: bold;
        color: #333;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# HEADER
# -----------------------------------------------------------------------------
st.title("Análisis de Dinámica No Lineal y Complejidad")
st.markdown("**Informe Técnico M3** | Applied Mathematics Division")
st.markdown("---")

# -----------------------------------------------------------------------------
# ESTRUCTURA DE TABS (NARRATIVA COMPLETA)
# -----------------------------------------------------------------------------
tab_names = [
    "I. Planteamiento", 
    "II. Sistemas Discretos (Tiempo)", 
    "III. Mapa de Bifurcación (Estructura)",
    "IV. Sensibilidad (Riesgo)",
    "V. Sistemas Continuos (Lorenz 3D)",
    "VI. Geometría Fractal (Emergencia)",
    "VII. Matriz Estratégica",
    "VIII. Conclusiones"
]
tabs = st.tabs(tab_names)

# --- TAB 1: PLANTEAMIENTO ---
with tabs[0]:
    st.header("I. Definición del Problema")
    st.markdown("""
    <div class="report-text">
    La predicción en sistemas complejos enfrenta una limitación fundamental: la no linealidad. 
    Este estudio desafía la noción de que inputs pequeños generan outputs pequeños.
    <br><br>
    <b>Objetivo:</b> Modelar y visualizar cómo reglas simples e iterativas pueden generar 
    comportamientos caóticos impredecibles, pero que paradójicamente contienen un orden geométrico oculto.
    </div>
    """, unsafe_allow_html=True)

# --- TAB 2: EVOLUCIÓN TEMPORAL ---
with tabs[1]:
    st.header("II. Análisis Descriptivo: Series de Tiempo")
    col_ctrl, col_viz = st.columns([1, 3])
    with col_ctrl:
        st.subheader("Parámetros")
        r_param = st.slider("Tasa de Crecimiento (r)", 0.0, 4.0, 3.2, 0.01, key="t2_r")
        steps = st.slider("Iteraciones", 50, 200, 100, key="t2_s")
    with col_viz:
        model = LogisticMap(r=r_param)
        data = model.simulate(x0=0.1, steps=steps)
        fig = go.Figure()
        fig.add_trace(go.Scatter(y=data, mode='lines+markers', line=dict(color='#2c3e50', width=1.5), marker=dict(size=4, color='#E63946'), name='Trayectoria'))
        fig.update_layout(title=f"Evolución Temporal (r = {r_param})", xaxis_title="Tiempo (t)", yaxis_title="Estado (x)", template="plotly_white", height=450)
        st.plotly_chart(fig, use_container_width=True)
    diagnosis = "Estabilidad" if r_param < 3.0 else "Periodicidad" if r_param < 3.56 else "Caos"
    st.markdown(f"""<div class="observation-box"><b>Discusión:</b> Régimen detectado: {diagnosis}.</div>""", unsafe_allow_html=True)

# --- TAB 3: BIFURCACIÓN ---
with tabs[2]:
    st.header("III. Estructura Global del Caos")
    if st.button("Generar Diagrama de Bifurcación"):
        with st.spinner("Calculando estructura..."):
            r_v, x_v = LogisticMap.generate_bifurcation_data(2.5, 4.0, 1000, 100, 800)
            fig = go.Figure(go.Scattergl(x=r_v, y=x_v, mode='markers', marker=dict(size=1, color='black', opacity=0.1)))
            fig.update_layout(title="Diagrama de Bifurcación", xaxis_title="r", yaxis_title="x", template="plotly_white", height=600, showlegend=False)
            st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Presione el botón para visualizar la ruta al caos.")

# --- TAB 4: SENSIBILIDAD ---
with tabs[3]:
    st.header("IV. Sensibilidad a Condiciones Iniciales")
    col_ctrl, col_viz = st.columns([1, 3])
    with col_ctrl:
        r_bf = st.slider("Parámetro r", 3.5, 4.0, 3.9, 0.01, key="t4_r")
        eps = st.select_slider("Error Inicial", options=[1e-5, 1e-4, 1e-3], value=1e-5)
    with col_viz:
        m = LogisticMap(r=r_bf)
        tb = m.simulate(0.2, 60)
        tp = m.simulate(0.2 + eps, 60)
        fig = go.Figure()
        fig.add_trace(go.Scatter(y=tb, name='Base', line=dict(color='#2c3e50')))
        fig.add_trace(go.Scatter(y=tp, name='Perturbado', line=dict(color='#E63946', dash='dash')))
        fig.update_layout(title="Divergencia Exponencial", template="plotly_white", height=500)
        st.plotly_chart(fig, use_container_width=True)
    st.markdown("""<div class="prescription-box" style="border-left-color: #ff9800;"><b>Riesgo:</b> La divergencia rápida confirma la imposibilidad de predicción a largo plazo (Horizonte de Lyapunov limitado).</div>""", unsafe_allow_html=True)

# --- TAB 5: LORENZ 3D ---
with tabs[4]:
    st.header("V. Sistemas Continuos: Atractor de Lorenz")
    col_ctrl, col_viz = st.columns([1, 3])
    with col_ctrl:
        rho = st.slider("Rayleigh (Caos > 24.7)", 0.0, 50.0, 28.0, 0.5)
        dur = st.slider("Duración", 10, 50, 30)
    with col_viz:
        traj = LorenzSystem(rho=rho).simulate(1.0, 1.0, 1.0, dur)
        fig = go.Figure(go.Scatter3d(x=traj[:,0], y=traj[:,1], z=traj[:,2], mode='lines', line=dict(color=traj[:,2], colorscale='Viridis', width=2), opacity=0.8))
        fig.update_layout(title="Espacio de Fase 3D", scene=dict(bgcolor='white'), height=600, margin=dict(t=0,b=0,l=0,r=0))
        st.plotly_chart(fig, use_container_width=True)

# --- TAB 6: FRACTALES (NUEVO) ---
with tabs[5]:
    st.header("VI. Geometría Fractal: Orden en el Azar")
    st.markdown("""
    <div class="report-text">
    ¿Puede el azar puro generar orden? Esta simulación utiliza el "Juego del Caos". 
    Reglas: Partimos de un punto aleatorio y en cada paso nos movemos la mitad de la distancia hacia un vértice elegido al azar.
    </div>
    """, unsafe_allow_html=True)
    
    col_fr_ctrl, col_fr_viz = st.columns([1, 3])
    
    with col_fr_ctrl:
        st.subheader("Simulación Estocástica")
        n_points = st.slider("Número de Puntos (Iteraciones)", 1000, 50000, 10000, step=1000, key="t6_n")
        st.write("Aumente el número de puntos para ver emerger la estructura nítida.")
        
    with col_fr_viz:
        # Instanciamos y ejecutamos el juego
        chaos_game = ChaosGame()
        fractal_points = chaos_game.generate_points(n_steps=n_points)
        
        fig_fr = go.Figure()
        fig_fr.add_trace(go.Scattergl(
            x=fractal_points[:, 0],
            y=fractal_points[:, 1],
            mode='markers',
            marker=dict(
                size=1.5,
                color='#2A9D8F', # Un color verde azulado elegante
                opacity=0.6
            ),
            name='Punto Iterado'
        ))
        
        fig_fr.update_layout(
            title="Emergencia del Triángulo de Sierpinski",
            xaxis=dict(visible=False), # Ocultamos ejes para limpieza visual
            yaxis=dict(visible=False, scaleanchor="x", scaleratio=1), # Mantener aspecto cuadrado
            template="plotly_white",
            height=600,
            showlegend=False,
             margin=dict(t=50,b=20,l=20,r=20)
        )
        st.plotly_chart(fig_fr, use_container_width=True)
        
    st.markdown("""
    <div class="observation-box">
        <b>Conclusión Visual:</b><br>
        Aunque cada paso individual es impredecible (aleatorio), la estructura global que emerge es perfectamente determinista y auto-similar (fractal). 
        Esto demuestra que sistemas ruidosos o caóticos pueden estar acotados por "atractores" geométricos rígidos.
    </div>
    """, unsafe_allow_html=True)

# --- TAB 7: ESTRATEGIA ---
with tabs[6]:
    st.header("VII. Matriz de Decisión Estratégica")
    st.markdown("""
    <table class="logic-table">
        <thead><tr><th>Fase</th><th>Hallazgo Técnico</th><th>Implicación de Negocio</th></tr></thead>
        <tbody>
            <tr><td><b>Diagnóstica</b></td><td>Presencia de Atractores Extraños y Fractales.</td><td>El sistema es impredecible localmente, pero tiene una estructura global acotada.</td></tr>
            <tr><td><b>Prescriptiva</b></td><td>Fallo de predicción puntual (Efecto Mariposa).</td><td>Abandonar la predicción a largo plazo. Invertir en adaptabilidad y redundancia.</td></tr>
        </tbody>
    </table>
    <div class="prescription-box"><b>Estrategia Final:</b> No intente predecir el próximo "punto aleatorio" del mercado. En su lugar, comprenda la forma del "atractor" (los límites del sistema) y construya estrategias robustas que sobrevivan dentro de toda esa estructura.</div>
    """, unsafe_allow_html=True)

# --- TAB 8: CONCLUSIONES ---
with tabs[7]:
    st.header("VIII. Síntesis Final")
    st.markdown("""<div class="report-text">Hemos demostrado matemáticamente que el caos no es desorden absoluto. Es un comportamiento complejo generado por reglas simples, sensible a condiciones iniciales, pero confinado en estructuras fractales elegantes. Comprender esto es el primer paso para navegar la incertidumbre real.</div>""", unsafe_allow_html=True)
